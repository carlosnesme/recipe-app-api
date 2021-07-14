from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@carlos.com',
            password = 'password123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@carlos.com',
            password = 'password123',
            name = 'Test user full name'

        )

    def test_user_listed(Self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = Self.client.get(url)

        Self.assertContains(res, Self.user.name)
        Self.assertContains(res, Self.user.email)
    
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create use page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        




