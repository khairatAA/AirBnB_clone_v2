#!/usr/bin/python3
"""States module """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class to test state """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test mane3"""
        new = self.value()
        self.assertEqual(type(new.name), str)
