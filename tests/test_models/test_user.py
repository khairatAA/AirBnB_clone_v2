#!/usr/bin/python3
""" The user moduke"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Th class test user """

    def __init__(self, *args, **kwargs):
        """ constructor"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Teat first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
