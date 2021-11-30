from django.test import TestCase
from model_bakery import baker

from .models import Profile


class ProfileTestCase(TestCase):

    # president tests

    def test_is_president(self):
        profile = baker.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertTrue(profile.is_president)

    def test_is_not_president(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_president)

    def test_only_one_president(self):
        baker.make(Profile, role=Profile.ROLE_PRESIDENT)
        baker.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertEqual(
            Profile.objects.filter(role=Profile.ROLE_PRESIDENT).count(), 1
        )

    def test_old_president_back_to_member(self):
        old_president = baker.make(Profile, role=Profile.ROLE_PRESIDENT)
        baker.make(Profile, role=Profile.ROLE_PRESIDENT)

        old_president.refresh_from_db()

        self.assertEqual(old_president.role, Profile.ROLE_MEMBER)

    def test_get_president(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        president = baker.make(Profile, role=Profile.ROLE_PRESIDENT)

        self.assertEqual(Profile.objects.president(), president)

    def test_get_president_none(self):
        baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.president())

    # financial director tests

    def test_is_financial_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertTrue(profile.is_financial_director)

    def test_is_not_financial_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_financial_director)

    def test_only_one_financial_director(self):
        baker.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)
        baker.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_FINANCIAL_DIRECTOR).count(),
            1
        )

    def test_old_financial_director_back_to_member(self):
        old_financial_director = baker.make(
            Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR
        )
        baker.make(Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        old_financial_director.refresh_from_db()

        self.assertEqual(old_financial_director.role, Profile.ROLE_MEMBER)

    def test_get_financial_director(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        financial_director = baker.make(
            Profile, role=Profile.ROLE_FINANCIAL_DIRECTOR)

        self.assertEqual(
            Profile.objects.financial_director(), financial_director
        )

    def test_get_financial_director_none(self):
        baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.financial_director())

    # technology director tests

    def test_is_technology_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertTrue(profile.is_technology_director)

    def test_is_not_technology_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_technology_director)

    def test_only_one_technology_director(self):
        baker.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)
        baker.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_TECHNOLOGY_DIRECTOR).count(),
            1
        )

    def test_old_technology_director_back_to_member(self):
        old_technology_director = baker.make(
            Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR
        )
        baker.make(Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        old_technology_director.refresh_from_db()

        self.assertEqual(old_technology_director.role, Profile.ROLE_MEMBER)

    def test_get_technology_director(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        technology_director = baker.make(
            Profile, role=Profile.ROLE_TECHNOLOGY_DIRECTOR)

        self.assertEqual(
            Profile.objects.technology_director(), technology_director
        )

    def test_get_technology_director_none(self):
        baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.technology_director())

    # marketing director tests

    def test_is_marketing_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertTrue(profile.is_marketing_director)

    def test_is_not_marketing_director(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_marketing_director)

    def test_only_one_marketing_director(self):
        baker.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)
        baker.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertEqual(
            Profile.objects.filter(
                role=Profile.ROLE_MARKETING_DIRECTOR).count(),
            1
        )

    def test_old_marketing_director_back_to_member(self):
        old_marketing_director = baker.make(
            Profile, role=Profile.ROLE_MARKETING_DIRECTOR
        )
        baker.make(Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        old_marketing_director.refresh_from_db()

        self.assertEqual(old_marketing_director.role, Profile.ROLE_MEMBER)

    def test_get_marketing_director(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        marketing_director = baker.make(
            Profile, role=Profile.ROLE_MARKETING_DIRECTOR)

        self.assertEqual(
            Profile.objects.marketing_director(), marketing_director
        )

    def test_get_marketing_director_none(self):
        baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertIsNone(Profile.objects.marketing_director())

    # deliberative council tests

    def test_is_deliberative_council_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_DELIBERATIVE_COUNCIL)

        self.assertTrue(profile.is_deliberative_council_member)

    def test_is_not_deliberative_council_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_deliberative_council_member)

    def test_get_deliberative_council_members_queryset(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        baker.make(Profile, role=Profile.ROLE_DELIBERATIVE_COUNCIL)
        baker.make(Profile, role=Profile.ROLE_DELIBERATIVE_COUNCIL)

        self.assertEqual(
            Profile.objects.deliberative_council_members().count(), 2
        )

    # fiscal council tests

    def test_is_fiscal_council_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_FISCAL_COUNCIL)

        self.assertTrue(profile.is_fiscal_council_member)

    def test_is_not_fiscal_council_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_fiscal_council_member)

    def test_get_fiscal_council_members_queryset(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        baker.make(Profile, role=Profile.ROLE_FISCAL_COUNCIL)
        baker.make(Profile, role=Profile.ROLE_FISCAL_COUNCIL)

        self.assertEqual(Profile.objects.fiscal_council_members().count(), 2)

    # alternate tests

    def test_is_alternate_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_ALTERNATE)

        self.assertTrue(profile.is_alternate_member)

    def test_is_not_alternate_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_alternate_member)

    def test_get_alternate_members_queryset(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        baker.make(Profile, role=Profile.ROLE_ALTERNATE)
        baker.make(Profile, role=Profile.ROLE_ALTERNATE)

        self.assertEqual(Profile.objects.alternate_members().count(), 2)

    # member tests

    def test_is_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertTrue(profile.is_member)

        for role in Profile.BOARD_ROLES:
            profile = baker.make(Profile, role=role)

            self.assertTrue(profile.is_member)

    def test_is_not_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)

        self.assertFalse(profile.is_member)

    def test_get_members_queryset(self):
        baker.make(Profile, role=Profile.ROLE_NOT_A_MEMBER)
        baker.make(Profile, role=Profile.ROLE_PRESIDENT)
        baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertEqual(Profile.objects.members().count(), 2)

    # board member tests

    def test_is_board_member(self):
        for role in Profile.BOARD_ROLES:
            profile = baker.make(Profile, role=role)

            self.assertTrue(profile.is_board_member)

    def test_is_not_board_member(self):
        profile = baker.make(Profile, role=Profile.ROLE_MEMBER)

        self.assertFalse(profile.is_board_member)

    def test_get_board_members_queryset(self):
        baker.make(Profile, role=Profile.ROLE_MEMBER)
        baker.make(Profile, role=Profile.ROLE_PRESIDENT)
        baker.make(Profile, role=Profile.ROLE_FISCAL_COUNCIL)

        self.assertEqual(Profile.objects.board_members().count(), 2)
