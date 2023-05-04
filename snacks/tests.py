from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Snack


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Snack.objects.create(
            purchaser = testuser1,
            title = 'Green Eggs and Ham',
            description = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_post.save()

    def test_blog_content(self):
        post = Snack.objects.get(id=1)
        actual_author = str(post.purchaser)
        actual_title = str(post.title)
        actual_body = str(post.description)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Green Eggs and Ham')
        self.assertEqual(actual_body, 'I do not like green eggs and ham, Sam I  am.')