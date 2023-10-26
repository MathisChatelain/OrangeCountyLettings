from django.test import TestCase


class lettingsTests(TestCase):
    def test_lettings_index(self):
        response = self.client.get("/lettings/")
        self.assertEqual(response.status_code, 200)
