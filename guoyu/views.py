# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tempinfo
from dss.Serializer import serializer
from django.views.generic import ListView
from dss.Mixin import MultipleJsonResponseMixin
import json
import datetime
import os
# Create your views here.
# 获取模板列表
class GetTempList(MultipleJsonResponseMixin,ListView):
    model = Tempinfo
    queryset = Tempinfo.objects.all()
    paginate_by = 20


	

def get_temp_detail(request):
    model = Tempinfo
    abliz = request.POST['tid']
    if abliz=='10':
        queryset = Tempinfo.objects.filter(id__gt=5)
        paginate_by=20
        resp = serializer(queryset)
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
    	resp = {'errorcode': 999, 'detail': 'Get success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


                            

                                
                                
                                
                           
