import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Document

# Create your tests here.

class DocumentModelTests(TestCase):

    def test_was_published_recently_with_future_document(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_document = Document(uploaded_at=time)
        self.assertIs(future_document.was_published_recently(), False)

    def test_was_published_recently_with_old_document(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_document = Document(uploaded_at=time)
        self.assertIs(old_document.was_published_recently(), False)

    def test_was_published_recently_with_recent_document(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_document = Document(uploaded_at=time)
        self.assertIs(recent_document.was_published_recently(), True)
