# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render
# the index function is called when the root is visited
def index(request):
	print "#" * 50
	return render(request, "hello/index.html")
# Create your views here.

