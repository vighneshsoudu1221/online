from django.test import TestCase
from django.urls import reverse


class CalculatorTests(TestCase):
    def test_get_calculator(self):
        response = self.client.get(reverse("calculator"))

        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        response = self.client.post(
            reverse("calculator"),
            {"t1": "10", "t2": "5", "Add": "Add"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["result"], 15)
        self.assertEqual(response.context["action"], "addition")
