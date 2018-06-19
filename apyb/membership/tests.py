from django.test import TestCase
from model_mommy import mommy

from .models import Profile


class ProfileTestCase(TestCase):

    def test_is_president(self):
        president = mommy.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertTrue(president.is_president)

    def test_is_not_a_president(self):
        not_president = mommy.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(not_president.is_president)

    def test_only_one_president(self):
        mommy.make(Profile, role=Profile.ROLE_PRESIDENT)
        mommy.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertEqual(
            Profile.objects.filter(role=Profile.ROLE_PRESIDENT).count(), 1
        )

    def test_old_president_back_to_member(self):
        old_president = mommy.make(Profile, role=Profile.ROLE_PRESIDENT)
        mommy.make(Profile, role=Profile.ROLE_PRESIDENT)

        old_president.refresh_from_db()

        self.assertEqual(old_president.role, Profile.ROLE_MEMBER)

    def test_get_president(self):
        president = mommy.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertEqual(Profile.objects.president(), president)

    def test_get_president_none(self):
        self.assertIsNone(Profile.objects.president())
