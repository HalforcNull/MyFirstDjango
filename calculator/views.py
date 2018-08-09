from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><head>Input Data</head><body><form action='/calculator/result'><input name='num1' />+<input name='num2' /><br /><input type='submit' value='Submit' /></form></body><html>")
	
def calcresult(request):
	num1 = request.GET.get('num1')
	num2 = request.GET.get('num2')
	return HttpResponse(num1+num2)