# makefile

PROJECT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))apyb

.PHONY: install
install: # standard python installation
	pip install -r requirements.txt

.PHONY: install.hack
install.hack: # install development requirements
	pip install -r requirements-dev.txt

.PHONY: deploy
deploy: # deploy to production
	fab production deploy

.PHONY: lint
lint: # lint code
	cd $(PROJECT) && flake8 .

.PHONY: test
test: # run tests
	cd $(PROJECT) && python manage.py test

.PHONY: cover
cover: # coverage tests
	cd $(PROJECT) && coverage run manage.py test
