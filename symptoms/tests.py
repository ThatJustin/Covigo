from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from django.utils.decorators import method_decorator

from symptoms.models import Symptom, PatientSymptom
from symptoms.utils import symptom_count_by_id
from symptoms.views import toggle_symptom


class ToggleSymptomTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = RequestFactory().get('/')
        cls.request.user = User()
        cls.symptom = Symptom.objects.create(name="test_symptom")

    def test_set_active(self):
        cases = [
            {'is_active': True, 'expected': False, 'msg': "When is_active is True"},
            {'is_active': False, 'expected': True, 'msg': "When is_active is False"}
        ]
        for case in cases:
            with self.subTest(case.get('msg')):
                self.symptom.is_active = case.get('is_active')
                self.symptom.save()
                toggle_symptom(self.request, self.symptom.id)
                self.symptom.refresh_from_db()
                self.assertEqual(case.get('expected'), self.symptom.is_active)


class CountSymptomsByIDTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        symptom_1 = Symptom.objects.create(id=1)
        symptom_2 = Symptom.objects.create(id=2)
        symptom_3 = Symptom.objects.create(id=3)
        user_1 = User.objects.create(id=1, username="Bob")
        user_2 = User.objects.create(id=2, username="Steve")
        user_3 = User.objects.create(id=3, username="Jessica")
        PatientSymptom.objects.create(symptom_id=symptom_1.id, user_id=user_1.id)
        PatientSymptom.objects.create(symptom_id=symptom_2.id, user_id=user_1.id)
        PatientSymptom.objects.create(symptom_id=symptom_3.id, user_id=user_1.id)
        PatientSymptom.objects.create(symptom_id=symptom_1.id, user_id=user_2.id)
        PatientSymptom.objects.create(symptom_id=symptom_2.id, user_id=user_2.id)
        PatientSymptom.objects.create(symptom_id=symptom_3.id, user_id=user_2.id)
        PatientSymptom.objects.create(symptom_id=symptom_1.id, user_id=user_3.id)
        PatientSymptom.objects.create(symptom_id=symptom_3.id, user_id=user_3.id)

    def test_count_id(self):
        cases = [
            {'input_list': [1], 'expected': 3, 'msg': "When input_list is [1]"},
            {'input_list': [2], 'expected': 2, 'msg': "When input_list is [2]"},
            {'input_list': [1, 2], 'expected': 2, 'msg': "When input_list is [1, 2]"},
            {'input_list': [1, 2, 3], 'expected': 2, 'msg': "When input_list is [1, 2, 3]"}
        ]
        for case in cases:
            with self.subTest(case.get('msg')):
                self.assertEqual(case.get('expected'), symptom_count_by_id(case.get('input_list')))
