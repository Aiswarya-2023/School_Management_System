from django.test import TestCase
from rest_framework.test import APITestCase
from school.models import User

class RoleBasedAccessTest(APITestCase):
    def setUp(self):
        # Create test users for each role
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.office_staff_user = User.objects.create_user(username='staff', password='staffpass', role='office_staff')
        self.librarian_user = User.objects.create_user(username='librarian', password='librarianpass', role='librarian')

def test_admin_access(self):
    self.client.login(username='admin', password='adminpass')
    response = self.client.get('admin-view/') 
    self.assertEqual(response.status_code, 200)

def test_office_staff_access(self):
    self.client.login(username='staff', password='staffpass')
    response = self.client.get('office-staff-view/') 
    self.assertEqual(response.status_code, 200)

def test_librarian_access(self):
    self.client.login(username='librarian', password='librarianpass')
    response = self.client.get('librarian-view/')  
    self.assertEqual(response.status_code, 200)

def test_admin_access_to_office_staff_view(self):
    self.client.login(username='admin', password='adminpass')
    response = self.client.get('office-staff-view/')  
    self.assertEqual(response.status_code, 403)
