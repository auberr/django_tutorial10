from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.
# class TestView(TestCase):
#     def test_two_is_three(self):
#         self.assertEqual(2,3)

#     def test_two_is_two(self):
#         self.assertEqual(2,2)

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "email": "abcdeffff@a.com",
            "password":"1"
        }
        response = self.client.post(url, user_data)
        # print(response.data)
        self.assertEqual(response.status_code, 201)

    # def test_login(self):
    #     url = reverse("token_obtain_pair")
    #     user_data = {
    #         "email": "abcdeffff@a.com",
    #         "password":"1"
    #     }
    #     response = self.client.post(url, user_data)
    #     print(response.data)
    #     self.assertEqual(response.status_code, 201)

class LoginUserTest(APITestCase):
    def setUp(self):

        self.data = {
            "email": "abcdeffff@a.com",
            "password":"1"
        }
        self.user = User.objects.create_user("abcdeffff@a.com", "1")
    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        # print(response.data["access"])
        self.assertEqual(response.status_code, 200)

    
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
        response = self.client.get(
            path = reverse("mock_view"),
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        print(self.data)
        print(response.data)
        self.assertEqual(response.status_code, 200)

        # self.assertEqual(response.data['request.user'], self.data['request.user'])