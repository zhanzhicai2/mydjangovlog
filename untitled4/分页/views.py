from django.shortcuts import render

# Create your views here.
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import math


def index2_view(request):
    num = request.GET.get('num', 1)
    n_num = int(num)
    city = City.objects.all()
    pager = Paginator(city, 20)
    try:
        pager_data = pager.page(n_num)
    except PageNotAnInteger:
        pager_data = pager.page(1)
    except EmptyPage:
        pager_data = pager.page(pager.num_pages)
    begin= (n_num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1
    end = begin+9
    if end > pager.num_pages:
        end = pager.num_pages

    if end < 10:
        begin = 1
    else:
        begin = end - 9
    pagerlist = range(begin, end+1)
    return render(request, 'City.html', {'pager': pager, 'pager_data': pager_data, 'pagerlist':pagerlist,'currentpage':n_num})






# def page(num, size=20):
#     num = int(num)
#     # 总记录数
#     num_city = City.objects.count()
#     # 总页数
#     sum_city_page = int(math.ceil((num_city*0.1/size)))
#     # 判断是否越界
#     if num < 1:
#         num = 1
#     if num > sum_city_page:
#         num = sum_city_page
#     # 计算出每页显示的记录
#     city = City.objects.all()[(size*(num-1)):(size*num)]
#     return city, num, sum_city_page
#
#
# def index2_view(request):
#
#     n_num = request.GET.get('num', 1)
#     num = int(n_num)
#     city, n, sum_city_page = page(num)
#
#     # 上一页的页码
#     per_page_num = n-1
#     #     下一页
#     next_page_num = n+1
#     sum_city_page_range = range(n, sum_city_page + 1)
#
#     return render(request, 'City.html',{'City':city,'per_page_num':per_page_num, 'next_page_num':next_page_num,
#                                         'sum_city_page':sum_city_page_range})



