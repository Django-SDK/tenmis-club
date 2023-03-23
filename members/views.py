from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

# members function to return a HttpResponse
def members(request):

    # get all membersd list
    members_list = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'members_list': members_list,
    }
    return HttpResponse(template.render(context, request))

# detail function to return a member detail
def details(request, member_id):
    mymember = Member.objects.get(id=member_id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


# main function to return a home page 
def main(request):
    template = loader.get_template('main.html')
    context = {
    }
    return HttpResponse(template.render(context, request))



