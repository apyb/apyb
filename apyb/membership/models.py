from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProfileQuerySet(models.QuerySet):

    def president(self):
        try:
            return self.get(role=Profile.ROLE_PRESIDENT)
        except ObjectDoesNotExist:
            return None

    def financial_director(self):
        try:
            return self.get(role=Profile.ROLE_FINANCIAL_DIRECTOR)
        except ObjectDoesNotExist:
            return None

    def technology_director(self):
        try:
            return self.get(role=Profile.ROLE_TECHNOLOGY_DIRECTOR)
        except ObjectDoesNotExist:
            return None

    def marketing_director(self):
        try:
            return self.get(role=Profile.ROLE_MARKETING_DIRECTOR)
        except ObjectDoesNotExist:
            return None

    def deliberative_council_members(self):
        return self.filter(role=Profile.ROLE_DELIBERATIVE_COUNCIL)

    def fiscal_council_members(self):
        return self.filter(role=Profile.ROLE_FISCAL_COUNCIL)

    def alternate_members(self):
        return self.filter(role=Profile.ROLE_ALTERNATE)

    def members(self):
        return self.exclude(role=Profile.ROLE_NOT_A_MEMBER)

    def board_members(self):
        return self.filter(role__in=Profile.BOARD_ROLES)


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

    UNIQUE_ROLES = (
        ROLE_PRESIDENT,
        ROLE_FINANCIAL_DIRECTOR,
        ROLE_TECHNOLOGY_DIRECTOR,
        ROLE_MARKETING_DIRECTOR,
    )

    BOARD_ROLES = (
        ROLE_PRESIDENT,
        ROLE_FINANCIAL_DIRECTOR,
        ROLE_TECHNOLOGY_DIRECTOR,
        ROLE_MARKETING_DIRECTOR,
        ROLE_DELIBERATIVE_COUNCIL,
        ROLE_FISCAL_COUNCIL,
        ROLE_ALTERNATE,
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

    objects = ProfileQuerySet.as_manager()

    @property
    def is_president(self):
        return self.role == self.ROLE_PRESIDENT

    @property
    def is_financial_director(self):
        return self.role == self.ROLE_FINANCIAL_DIRECTOR

    @property
    def is_technology_director(self):
        return self.role == self.ROLE_TECHNOLOGY_DIRECTOR

    @property
    def is_marketing_director(self):
        return self.role == self.ROLE_MARKETING_DIRECTOR

    @property
    def is_deliberative_council_member(self):
        return self.role == self.ROLE_DELIBERATIVE_COUNCIL

    @property
    def is_fiscal_council_member(self):
        return self.role == self.ROLE_FISCAL_COUNCIL

    @property
    def is_alternate_member(self):
        return self.role == self.ROLE_ALTERNATE

    @property
    def is_member(self):
        return self.role != self.ROLE_NOT_A_MEMBER

    @property
    def is_board_member(self):
        return self.role in self.BOARD_ROLES

    def _ensure_unique_board(self):
        if self.role in self.UNIQUE_ROLES:
            Profile.objects.exclude(
                pk=self.pk
            ).filter(
                role=self.role
            ).update(
                role=self.ROLE_MEMBER
            )

    def save(self, *args, **kwargs):
        self._ensure_unique_board()

        super().save(*args, **kwargs)
