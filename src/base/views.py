from django.shortcuts import render
from django.http import HttpResponse


def taskList(request):
	return HttpResponse("<h1>To Do List</h1>")
