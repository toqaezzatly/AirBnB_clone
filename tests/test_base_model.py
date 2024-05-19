#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_unique(self):
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        model_dict = self.model.to_dict()
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertTrue(all(key in model_dict for key in expected_keys))

    def test_to_dict_values(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()

