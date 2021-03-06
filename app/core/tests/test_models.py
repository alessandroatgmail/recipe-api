from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test1@silv.io", password="testpass"):
    return get_user_model().objects.create_user(email, password)


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
            return user

    def test_superuser_create(self):
        """ test creating a new super user"""
        user = get_user_model().objects.create_superuser(
                'testsuper@silv.io',
                'test123'
                )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'

        )

        self.assertEqual(str(tag), tag.name)


    def test_ingredient_str(self):

        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):

        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe),recipe.title)
