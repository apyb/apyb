from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):

    ROLE_NOT_A_MEMBER = 0
    ROLE_MEMBER = 1
    ROLE_PRESIDENT = 2
    ROLE_FINANCIAL_DIRECTOR = 3
    ROLE_TECHNOLOGY_DIRECTOR = 4
    ROLE_MARKETING_DIRECTOR = 5
    ROLE_DELIBERATIVE_COUNCIL = 6
    ROLE_FISCAL_COUNCIL = 7
    ROLE_ALTERNATE = 8
    ROLE_CHOICES = (
        (ROLE_NOT_A_MEMBER, _('Not a member')),
        (ROLE_MEMBER, _('Member')),
        (ROLE_PRESIDENT, _('President')),
        (ROLE_FINANCIAL_DIRECTOR, _('Financial Director')),
        (ROLE_TECHNOLOGY_DIRECTOR, _('Technology Director')),
        (ROLE_MARKETING_DIRECTOR, _('Marketing Director')),
        (ROLE_DELIBERATIVE_COUNCIL, _('Deliberative Council')),
        (ROLE_FISCAL_COUNCIL, _('Fiscal Council')),
        (ROLE_ALTERNATE, _('Alternate')),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile',
        on_delete=models.CASCADE
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=ROLE_NOT_A_MEMBER
    )

    github_username = models.CharField(max_length=39, blank=True)
    thumbnail_url = models.URLField()
