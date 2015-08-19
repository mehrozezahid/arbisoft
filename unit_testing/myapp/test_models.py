from django.core.cache import cache
from django.test import TestCase
from myapp.models import Person


class PersonModelTest(TestCase):
    # def setUp(self):
    #     Person.objects.create(first_name="Mehroze", last_name="Zahid")
    #     Person.objects.create(first_name="Hello", last_name="World")
    #
    # def test_person_name(self):
    #     person_1 = Person.objects.get(first_name="Mehroze")
    #     person_2 = Person.objects.get(first_name="Hello")
    #
    #     self.assertEqual(person_1.last_name, "Zahid")
    #     self.assertEqual(person_2.last_name, "World")

    def test_cache(self):
        fname = 'Mehroze'
        lname = 'Zahid'
        email = 'hello@world.com'

        Person.objects.create(email=email, first_name=fname, last_name=lname)

        with self.assertNumQueries(1):
            Person.get_person(email)
            Person.get_person(email)
