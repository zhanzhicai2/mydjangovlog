from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
# Create your views here.


def hello(request):
    num = request.GET.get('num', 1)
    n = int(num)
    Citys = City.objects.all()
    # 创建分页
    pager = Paginator(Citys, 20)
    # 获取当前分页的数据
    # if type(num) == int and type(num) == float:

    try:
        pergage_data = pager.page(n)
    except PageNotAnInteger:
        pergage_data = pager.page(1)
    except EmptyPage:
        pergage_data = pager.page(pager.num_pages)
    return render(request, 'city.html', {'pager':pager,'perpage_data':pergage_data})
