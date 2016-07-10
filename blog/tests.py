from django.test import TestCase
from django.contrib.auth.models import User
from models import Post, Reply


class PostVisibilityTests(TestCase):
    def setUp(self):
        self.fake_user = User(username='FakeUser', password='FakePassword')
        self.fake_user.save()
        self.fake_post = Post(title='Fake Post', author=self.fake_user, content='This is a fake post used for testing')

    def test_post_publish_method_sets_is_published_to_True(self):
        self.fake_post.publish()
        self.assertTrue(self.fake_post.is_published)

    def test_post_unpublish_method_sets_is_publised_to_False(self):
        self.fake_post.unpublish()
        self.assertFalse(self.fake_post.is_published)

    def test_post_delete_method_sets_is_deleted_to_True(self):
        self.fake_post.delete()
        self.assertTrue(self.fake_post.is_deleted)


class ReplyVisibilityTests(TestCase):
    def setUp(self):
        self.fake_user = User(username='FakeUser', password='FakePassword')
        self.fake_user.save()
        self.fake_post = Post(title='Fake Post', author=self.fake_user, content='This is a fake post used for testing')
        self.fake_post.save()
        self.fake_reply = Reply(post=self.fake_post, name='FakeName', email='fake@email.com',
                                content='This is fake reply to be used for testing')

    def test_reply_approve_method_sets_is_approved_to_True(self):
        self.fake_reply.approve()
        self.assertTrue(self.fake_reply.approved_reply)

    def test_reply_delete_method_set_is_deleted_to_True(self):
        self.fake_reply.delete()
        self.assertTrue(self.fake_reply.is_deleted)