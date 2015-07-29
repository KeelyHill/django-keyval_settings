from django.db import models
from django.shortcuts import get_object_or_404
import json


class Setting(models.Model):
    key = models.CharField(max_length=256)
    _value = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    @classmethod
    def create(cls, key, value):
        if key in ['', ' ', None]:
            raise ValueError('A key is required.')
        return cls(key=key, value=value)

    @classmethod
    def get(cls, key):
        setting = get_object_or_404(cls, key=key)
        return setting.value

    @property
    def value(self):
        try:
            return json.loads(self._value)
        except ValueError:
            return self._value

    @value.setter
    def value(self, v):
        if not type(v) is str:
            self._value = json.dumps(v)
        else:
            self._value = v
