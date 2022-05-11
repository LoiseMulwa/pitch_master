import unittest
from app.models import Pitch, User
from app import db
from unittest import TestCase

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_mulwa= User(username='mulwa', password='flasksApp', email='loisemulwa7@gmail.com',biography="New Knowledge on Flask",profile_pic="xxxx")
        self.new_pitch = Pitch(title="Pitch", category='promotion', pitch="Get new pitch", user=self.user_mulwa)


    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()





