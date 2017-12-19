from django.test import TestCase
from .models import Memos


class ModelTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.notes = "Write world class code"
        self.date = "2017-12-20"
        self.name = "Arun Lal"
        self.memo = Memos(desc=self.notes, date=self.date, person=self.name)

    def test_model_can_create_a_memo(self):
        """Test the Memos model can create a new memo."""
        old_count = Memos.objects.count()
        self.memo.save()
        new_count = Memos.objects.count()
        self.assertNotEqual(old_count, new_count)
