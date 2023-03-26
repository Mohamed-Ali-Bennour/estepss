from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import  Profile , Locations,Permission_level
import json
# Create your views here.
from django.core.serializers.json import DjangoJSONEncoder

def login(request):
   
   # my_list = list(user.values())
    username = request.GET.get('username')
    password = request.GET.get('pwd')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        response_data = {'status': 200 , 'message': user.id}
    else:
        response_data = {'status': 404 , 'message': "wrong"}
        


    



    


    print('test')
    return JsonResponse(response_data,safe=False)


def get_profile(request):
        id = request.GET.get('id')
        user=User.objects.get(id=id)

        profile=Profile.objects.get(user=user)

        p={'username':user.username, 'photo' : profile.profile_picture.url,
           'role':profile.role
           }

        return JsonResponse( p ,safe=False);


def change_location(request):
     
     id= request.GET['id']
     la = request.GET['la']
     lo = request.GET['lo']


     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)
     locations.latitude=la
     locations.longitude=lo
     locations.save()

     return JsonResponse({"wored":1},safe=False)

def get_location(request):
     id=request.GET['id']
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)

     return JsonResponse({"latitude":locations.latitude,"longitude":locations.longitude},safe=False)




def get_account_details(request):

   
     
    _from=request.GET['from']
    _to=request.GET['to']
    user_from=User.objects.get(id=_from)
    user_to=User.objects.get(id=_to)
    profile_from=Profile.objects.get(user=user_from)
    profile_to=Profile.objects.get(user=user_to)

    p=Permission_level.objects.get(profile_from=profile_from,profile_to=profile_to) 

   
    profile=Profile.objects.get(user=user_from)
    import re


    
    match = re.search(r'\((\d+)\)', profile.job_locatin)
    print(match.group(1)  == str(p.Permission_level)  )
    print(match.group(1)  == str(p.Permission_level)  )
    if match.group(1)  == str(p.Permission_level) :
         data={"pic":profile.profile_picture.url,
               "online":profile.is_online,
               "phone":profile.phone_number,
               "job_location":profile.job_locatin}
  
    else:
      data={"pic":profile.profile_picture.url,
               "online":profile.is_online,
               "phone":profile.phone_number,
               }
         
         


    return JsonResponse(data, encoder=DjangoJSONEncoder, safe=False)

     