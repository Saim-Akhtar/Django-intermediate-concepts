from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Testing Title", valid=True)

    def test_post_title(self):
        post = Post.objects.get(title="Testing Title")
        self.assertEquals(post.valid,True)
