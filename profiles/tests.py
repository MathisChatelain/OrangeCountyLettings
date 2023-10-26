from django.test import TestCase


class profilesTests(TestCase):
    def test_profiles_index(self):
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)
