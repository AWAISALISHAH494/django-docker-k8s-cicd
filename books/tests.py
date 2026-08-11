from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William",
            published_year=2025
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Django for Beginners")
        self.assertEqual(self.book.author, "William")
        self.assertEqual(self.book.published_year, 2025)

    def test_book_string_representation(self):
        self.assertEqual(str(self.book), "Django for Beginners")