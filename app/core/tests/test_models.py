from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        """ test creating a user with an email is succesfull """
        email = "test@silv.io"
        password = "Abbascgda123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test the email for a new user is normalized """
        email = "test@SILV.io"
        user = get_user_model().objects.create_user(email, "Abbascgda123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, 'Abbascgda123')

    def test_superuser_create(self):
        """ test creating a new super user"""
        user = get_user_model().objects.create_superuser(
                'testsuper@silv.io',
                'test123'
                )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
