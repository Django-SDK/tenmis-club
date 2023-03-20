from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# members function to return a HttpResponse
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({}, request))


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = person("John", 36)