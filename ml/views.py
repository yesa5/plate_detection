from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def list(request):
    return render(request, 'ml/main.html')
