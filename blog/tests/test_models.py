from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post, Comment


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('test_user', None, 'password')
        User.objects.create_user('test_user_1', None, 'password')
        Post.objects.create(
            title='Test post title',
            text='Test post text',
            owner=user
        )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_text_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_owner_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_created_at_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'created at')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_owner_related_model(self):
        post = Post.objects.get(id=1)
        related_model = post._meta.get_field('owner').related_model
        self.assertEquals(related_model, User)

    def test_object_str_representation(self):
        post = Post.objects.get(id=1)
        self.assertEquals(str(post), post.title)

    def test_user_is_post_owner(self):
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertEquals(post.owner, user)

    def test_user_is_not_post_owner(self):
        user = User.objects.get(id=2)
        post = Post.objects.get(id=1)
        self.assertNotEquals(post.owner, user)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('test_user', None, 'password')
        User.objects.create_user('test_user_1', None, 'password')
        post = Post.objects.create(
            title='Test post title',
            text='Test post text',
            owner=user
        )
        Post.objects.create(
            title='Test post title 1',
            text='Test post text 1',
            owner=user
        )
        Comment.objects.create(
            text='Test comment title',
            owner=user,
            post=post
        )

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_owner_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_created_at_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'created at')

    def test_text_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEquals(max_length, 512)

    def test_owner_related_model(self):
        comment = Comment.objects.get(id=1)
        related_model = comment._meta.get_field('owner').related_model
        self.assertEquals(related_model, User)

    def test_user_is_comment_owner(self):
        user = User.objects.get(id=1)
        comment = Comment.objects.get(id=1)
        self.assertEquals(comment.owner, user)

    def test_user_is_not_comment_owner(self):
        user = User.objects.get(id=2)
        comment = Comment.objects.get(id=1)
        self.assertNotEquals(comment.owner, user)

    def test_comment_is_related_to_post(self):
        comment = Comment.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertEquals(comment.post, post)

    def test_comment_is_not_related_to_post(self):
        comment = Comment.objects.get(id=1)
        post = Post.objects.get(id=2)
        self.assertNotEquals(comment.post, post)
