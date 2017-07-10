# coding=utf-8

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from models import LagouJobs, ZhilianJobs
from dss import Serializer


# Create your views here.

def get_lagou(request):
    """
    获取拉勾网职位信息
    :param request:
    :return:
    """
    response_dict = get_jobs(request, LagouJobs)
    return JsonResponse(response_dict, safe=False)


def get_zhilian(request):
    """
    获取智联招聘职位信息
    :param request:
    :return:
    """
    response_dict = get_jobs(request, ZhilianJobs)
    return JsonResponse(response_dict, safe=False)


def get_jobs(request, mtype):
    """
    获取职位信息
    :param request:
    :param mtype:
    :return:
    """
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 10)
    # type=1: python; type=2: android
    ptype = int(request.GET.get('type', 1))
    offset = int(offset)
    limit = int(limit)
    if ptype == 1:
        jobs = mtype.objects.all().filter(keyWord='python')
    elif ptype == 2:
        jobs = mtype.objects.all().filter(keyWord='android')
    else:
        jobs = ZhilianJobs.objects.all()
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
    return response_dict
