import json

from django.test import TestCase
from django.contrib.auth.models import User

from knox.models import AuthToken

from blog.models import Post


class ListPostAPITest(TestCase):
    POSTS_COUNT = 5

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('test_user', None, 'password')
        for post in range(cls.POSTS_COUNT):
            Post.objects.create(
                title=f'Test post title {post}',
                text=f'Test post text {post}',
                owner=user
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_returns_json(self):
        resp = self.client.get('/api/posts/')
        self.assertEqual(resp.get('Content-Type'), 'application/json')

    def test_view_returns_all_posts(self):
        resp = self.client.get('/api/posts/')
        content = json.loads(resp.content)
        self.assertEqual(len(content), self.POSTS_COUNT)

    def test_view_unauthorized_create_post(self):
        data = {
            "title": "Some title",
            "text": "Some text"
        }
        resp = self.client.post('/api/posts/', data=data)
        self.assertEqual(resp.status_code, 401)

    def test_view_authorized_create_post(self):
        user = User.objects.get(pk=1)
        token = AuthToken.objects.create(user)
        headers = {
            'HTTP_AUTHORIZATION': f'Token {token}'
        }
        data = {
            "title": "Some title",
            "text": "Some text"
        }
        resp = self.client.post('/api/posts/', data=data, content_type='application/json', **headers)
        self.assertEqual(resp.status_code, 201)

    def test_view_create_post_title_is_required(self):
        user = User.objects.get(pk=1)
        token = AuthToken.objects.create(user)
        headers = {
            'HTTP_AUTHORIZATION': f'Token {token}'
        }
        data = {
            "text": "Some text"
        }
        resp = self.client.post('/api/posts/', data=data, content_type='application/json', **headers)
        content = json.loads(resp.content)
        self.assertEqual(resp.status_code, 400)
        self.assertListEqual(content.get('title'), ['This field is required.'])

    def test_view_create_post_text_is_required(self):
        user = User.objects.get(pk=1)
        token = AuthToken.objects.create(user)
        headers = {
            'HTTP_AUTHORIZATION': f'Token {token}'
        }
        data = {
            "title": "Some text"
        }
        resp = self.client.post('/api/posts/', data=data, content_type='application/json', **headers)
        content = json.loads(resp.content)
        self.assertEqual(resp.status_code, 400)
        self.assertListEqual(content.get('text'), ['This field is required.'])
