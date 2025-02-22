from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .views import PostListCreateView

User = get_user_model()


class PostListCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.view = PostListCreateView.as_view()
        self.url = reverse('list_posts')

        # Create a test user
        self.user = User.objects.create_user(
            username="test", email="test@example.com", password="test@12345"
        )

    def authenticate(self):
        response = self.client.post(
            reverse("login"),
            {"email": "test@example.com", "password": "test@12345"},
            format="json"
        )
        print(response.data)  # Debugging output

        # If login is successful, set the token for authorization
        token = response.data["token"]['access']
        if token:
            self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.authenticate()  # Ensure authentication before posting
        sample_post = {"title": "New Post", "content": "This is a test post."}
        
        response = self.client.post(
            self.url, sample_post, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
