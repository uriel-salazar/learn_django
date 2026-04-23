from django.http import JsonResponse
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return JsonResponse({"ok": True})
