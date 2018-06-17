from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def default(request):
    return HttpResponse('<h1>Wellcome!</h1><br><body>' +
                        'Write your operation in the url</body>')


def sum(request, op1, op2):
    result = int(op1) + int(op2)
    return HttpResponse(('<head><b>Result: </b><br></head><body>' +
                         op1 + ' + ' + op2 + ' = ' + str(result) +
                         '</body>'))


def subs(request, op1, op2):
    result = int(op1) - int(op2)
    return HttpResponse(('<head><b>Result: </b><br></head><body>' +
                         op1 + ' - ' + op2 + ' = ' + str(result) +
                         '</body>'))


def mult(request, op1, op2):
    result = int(op1) * int(op2)
    return HttpResponse(('<head><b>Result: </b><br></head><body>' +
                         op1 + ' * ' + op2 + ' = ' + str(result) +
                         '</body>'))


def div(request, op1, op2):
    result = int(op1) / int(op2)
    return HttpResponse(('<head><b>Result: </b><br></head><body>' +
                         op1 + ' / ' + op2 + ' = ' + str(result) +
                         '</body>'))


def notFound(request):
    return HttpResponseNotFound('<h1>404 - Resource not Found</h1>')
