from django.http import JsonResponse
from .models import Setting
import json


def settings_dict_view(request, key=None):
    resp = {}

    if key:
        # resp = get_object_or_404(Setting, key=key).value
        resp = Setting.get(key)
    else:
        for setting in Setting.objects.all():
            resp[setting.key] = setting.value

    return JsonResponse(resp)
