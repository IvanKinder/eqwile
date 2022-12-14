import json

import requests
from django.contrib.auth.models import User
from django.test import TestCase

from categoryapp.models import Category
from tizerapp.models import Tizer


class ApiStatusTest(TestCase):

    def test_update_status_by_admin(self):
        new_category = Category(category_name='test')
        new_category.save()
        new_user = User(username='test')
        new_user.save()
        new_tizer = Tizer(title='test', description='test', category=new_category, author=new_user)
        new_tizer.save()

        headers = {
            'username': 'admin',
            'password': 'admin'
        }
        body = '''{
            "tizer_id": "1",
            "status_id": "1"
        }'''

        response = requests.put('http://127.0.0.1:8000/api/status/', headers=headers, data=body)

        self.assertEqual(json.loads(response.content).get('status'), 200)

    def test_update_status_by_onknown_user(self):
        headers = {
            'username': 'admsin',
            'password': 'admin'
        }
        body = '''{
            "tizer_id": "1",
            "status_id": "1"
        }'''

        response = requests.put('http://127.0.0.1:8000/api/status/', headers=headers, data=body)

        self.assertEqual(json.loads(response.content).get('status'), 403)

    def test_update_status_bad_request(self):
        headers = {
            'username': 'admin',
            'password': 'admin'
        }
        body = '''{
            "tizer_id": "1w",
            "status_id": "1"
        }'''

        response = requests.put('http://127.0.0.1:8000/api/status/', headers=headers, data=body)

        self.assertEqual(json.loads(response.content).get('status'), 200)
