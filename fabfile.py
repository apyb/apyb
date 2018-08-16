#!/usr/bin/env python

import os
import time

from fabric.api import env, puts, run, sudo


def production():
    env.app_name = 'apyb.python.org.br'
    env.hosts = [env.app_name]
    env.user = 'apyb'
    env.app_path = os.path.abspath(f'/srv/{env.app_name}')
    env.deploy_path = os.path.join(env.app_path, 'www')
    env.current_path = os.path.join(env.deploy_path, 'current')
    env.releases_path = os.path.join(env.deploy_path, 'releases')
    env.shared_path = os.path.join(env.deploy_path, 'shared')
    env.shared_files = [
        'apyb/apyb/settings/local.py',
        'apyb/apyb/media',
    ]
    env.releases_limit = 3
    env.git_origin = 'https://github.com/humrochagf/apyb.git'
    env.git_branch = 'master'
    env.virtualenv = os.path.join(env.app_path, 'activate')


def deploy():
    start = time.time()

    _setup()
    _checkout()
    _shared_path()
    _project_requirements()
    _releases()
    _symlink()
    _cleanup()
    _reload_project()

    final = time.time()
    total = final - start
    puts(f'execution finished in {total}s')


def rollback():
    start = time.time()

    _setup()
    _releases()
    _rollback_code()

    final = time.time()
    total = final - start
    puts(f'execution finished in {total}s')


def _setup():
    run(f'mkdir -p {env.releases_path}')
    run(f'mkdir -p {env.shared_path}')


def _checkout():
    env.current_release = os.path.join(
        env.releases_path, time.strftime('%Y%m%d%H%M%S')
    )
    run(
        f'git clone -q -b {env.git_branch} -o deploy '
        f'--depth 1 {env.git_origin} {env.current_release}'
    )


def _shared_path():
    for shared_file in env.shared_files:
        origin = os.path.join(env.shared_path, shared_file)
        destiny = os.path.join(env.current_release, shared_file)

        run(f'ln -nfs {origin} {destiny}')


def _project_requirements():
    manage_file = os.path.join(env.current_release, 'apyb', 'manage.py')
    env.django = f'python {manage_file}'
    env.workon = f'source {env.virtualenv}'

    # update python packages
    requirements_file = os.path.join(env.current_release, 'requirements.txt')
    run(f'{env.workon};pip install -r {requirements_file}')

    # update static media
    run(f'{env.workon};{env.django} collectstatic --noinput')

    # run migrations
    run(f'{env.workon};{env.django} migrate --noinput')


def _releases():
    env.releases = sorted(run(f'ls -x {env.releases_path}').split())


def _symlink():
    run(f'ln -nfs {env.current_release} {env.current_path}')


def _cleanup():
    if len(env.releases) > env.releases_limit:
        directories = reversed(env.releases)
        del directories[:env.releases_limit]
        directories = ' '.join([
            os.path.join(env.releases_path, release) for release in directories
        ])

        run(f'rm -rf {directories}')


def _reload_project():
    # restart apyb uwsgi service
    run(f'find {env.current_release} -name "*.pyc" -delete')
    sudo(f'service apyb restart')


def _rollback_code():
    if len(env.releases) > 1:
        env.current_release = os.path.join(
            env.releases_path, env.releases[-1]
        )
        env.previous_release = os.path.join(
            env.releases_path, env.releases[-2]
        )

        run(f'ln -nfs {env.previous_release} {env.current_path}')
        run(f'rm -rf {env.current_release}')
