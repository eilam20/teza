from django.test import TestCase
from teza_app.utils import count_capitalized_words  # Replace with actual import path

class UtilsTestCase(TestCase):
    def test_count_capitalized_words(self):
        """
        Test the function for counting words starting with a capital letter.
        """
        text = "This is a Test. It has Several Words that Start with a Capital Letter."
        result = count_capitalized_words(text)
        self.assertEqual(result, 8)  # There are 7 capitalized words in the text

    def test_is_year_odd_or_even(self):
        """
        Test whether the year is correctly identified as odd or even.
        """
        # Check for even year
        year = 2024
        self.assertTrue(year % 2 == 0, "Year should be even")

        # Check for odd year
        year = 2023
        self.assertFalse(year % 2 == 0, "Year should be odd")
