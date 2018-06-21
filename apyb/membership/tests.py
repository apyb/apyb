from django.test import TestCase
from model_mommy import mommy

from .models import Profile


class ProfileTestCase(TestCase):

    # president tests

    def test_is_president(self):
        profile = mommy.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertTrue(profile.is_president)

    def test_is_not_president(self):
        profile = mommy.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_president)

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
        mommy.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.president())

    # financial director tests

    def test_is_financial_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertTrue(profile.is_financial_director)

    def test_is_not_financial_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_financial_director)

    def test_only_one_financial_director(self):
        mommy.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)
        mommy.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_FINANCIAL_DIRECTOR).count(),
            1
        )

    def test_old_financial_director_back_to_member(self):
        old_financial_director = mommy.make(
            Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR
        )
        mommy.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        old_financial_director.refresh_from_db()

        self.assertEqual(old_financial_director.role, Profile.ROLE_MEMBER)

    def test_get_financial_director(self):
        financial_director = mommy.make(
            Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertEqual(
            Profile.objects.financial_director(), financial_director
        )

    def test_get_financial_director_none(self):
        mommy.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.financial_director())

    # technology director tests

    def test_is_technology_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertTrue(profile.is_technology_director)

    def test_is_not_technology_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_technology_director)

    def test_only_one_technology_director(self):
        mommy.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)
        mommy.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_TECHNOLOGY_DIRECTOR).count(),
            1
        )

    def test_old_technology_director_back_to_member(self):
        old_technology_director = mommy.make(
            Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR
        )
        mommy.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        old_technology_director.refresh_from_db()

        self.assertEqual(old_technology_director.role, Profile.ROLE_MEMBER)

    def test_get_technology_director(self):
        technology_director = mommy.make(
            Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertEqual(
            Profile.objects.technology_director(), technology_director
        )

    def test_get_technology_director_none(self):
        mommy.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.technology_director())

    # marketing director tests

    def test_is_marketing_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertTrue(profile.is_marketing_director)

    def test_is_not_marketing_director(self):
        profile = mommy.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_marketing_director)

    def test_only_one_marketing_director(self):
        mommy.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)
        mommy.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_MARKETING_DIRECTOR).count(),
            1
        )

    def test_old_marketing_director_back_to_member(self):
        old_marketing_director = mommy.make(
            Profile, role=Profile.ROLE_MARKETING_DIRECTOR
        )
        mommy.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        old_marketing_director.refresh_from_db()

        self.assertEqual(old_marketing_director.role, Profile.ROLE_MEMBER)

    def test_get_marketing_director(self):
        marketing_director = mommy.make(
            Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertEqual(
            Profile.objects.marketing_director(), marketing_director
        )

    def test_get_marketing_director_none(self):
        mommy.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.marketing_director())
