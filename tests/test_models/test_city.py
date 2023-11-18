#!/usr/bin/python3
"""Test ciy module """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Class that tests for city"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
