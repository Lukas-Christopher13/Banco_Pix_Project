import unittest

from app import create_app
from app.ext.db import db


class TestClassBase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.app.testing = True
        self.client = self.app.test_client()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.drop_all()
        self.app_context.pop()

    

    