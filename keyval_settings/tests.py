from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Setting
import json


class SettingsTestCase(TestCase):

    def setUp(self):
        Setting.objects.create(key='Foo', _value='Bar')
        Setting.objects.create(key='bool_t', _value='true')
        Setting.objects.create(key='bool_f', _value='false')
        Setting.objects.create(key='nully', _value='null')

    def test_general_set_and_get(self):
        """General test, checking the most basic get function."""
        self.assertEqual(Setting.get('Foo'), 'Bar')

    def test_proper_booleans(self):
        """Ensures booleans get json-ified properly"""
        bool_false = Setting.get('bool_f')
        self.assertFalse(bool_false)

        bool_true = Setting.get('bool_t')
        self.assertEqual(bool_true, True)

    def test_all_settings_view(self):
        """Tests the view which returns a dictionary from the models objects"""
        response = self.client.get(reverse('Settings View'))
        self.assertEqual(response.status_code, 200)

        toDict = json.loads(response.content.decode("utf-8"))
        self.assertEqual(type(toDict), dict)

    def test_individual_setting_view(self):
        """Gets individual keys/value pairs with the url.
           This tests a few of the value types to make sure they
           are returned in their proper format.
        """
        # Foo
        response = self.client.get(reverse('Setting Detail', args=['Foo']))
        self.assertEqual(response.status_code, 200)

        loads = json.loads(response.content.decode("utf-8"))
        self.assertEqual(loads, 'Bar')

        # bool_t
        response = self.client.get(reverse('Setting Detail', args=['bool_t']))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.content.decode("utf-8"), 'true')
        loads = json.loads(response.content.decode("utf-8"))
        self.assertEqual(loads, True)

        # nully
        response = self.client.get(reverse('Setting Detail', args=['nully']))
        self.assertEqual(response.status_code, 200)

        loads = json.loads(response.content.decode("utf-8"))
        self.assertEqual(loads, None)
