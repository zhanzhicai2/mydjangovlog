from django.shortcuts import render

# Create your views here.
from .models import *
import math


def page(num, size=20):
    num = int(num)
    # 总记录数
    num_city = City.objects.count()
    # 总页数
    sum_city_page = int(math.ceil((num_city*0.1/size)))
    # 判断是否越界
    if num < 1:
        num = 1
    if num > sum_city_page:
        num = sum_city_page
    # 计算出每页显示的记录
    city = City.objects.all()[(size*(num-1)):(size*num)]
    return city, num, sum_city_page


def index2_view(request):

    n_num = request.GET.get('num', 1)
    num = int(n_num)
    city, n, sum_city_page = page(num)

    # 上一页的页码
    per_page_num = n-1
    #     下一页
    next_page_num = n+1
    sum_city_page_range = range(n, sum_city_page + 1)

    return render(request, 'City.html',{'City':city,'per_page_num':per_page_num, 'next_page_num':next_page_num,
                                        'sum_city_page':sum_city_page_range})



