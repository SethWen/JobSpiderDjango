# coding=utf-8

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from models import LagouJobs
from dss import Serializer


# Create your views here.

def index(request):
    # jobs = LagouJobs.objects.all().filter(pk=20)
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 10)

    offset = int(offset)
    limit = int(limit)

    jobs = LagouJobs.objects.all()
    count = jobs.count()
    if count >= limit * (offset + 1):
        offset_jobs = jobs[offset * limit:offset * limit + limit]
    else:
        offset_jobs = jobs[offset * limit:offset * limit + (count % limit)]

    print('mlgb', type(jobs))

    s = Serializer.serializer(offset_jobs)
    response_dict = {
        'code': 20200,
        'msg': 'success',
        'data': s
    }
    print(type(s))
    return JsonResponse(response_dict, safe=False)
