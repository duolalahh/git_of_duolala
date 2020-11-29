import datetime
from django.shortcuts import render,redirect
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from read_statistics.utils import get_7_days_read_data,get_day_hot_data,get_ysday_hot_data
from django.contrib.contenttypes.models import ContentType
from bowen.models import Blog
from django.urls import reverse

def get_7_days_blog():
    today=timezone.now().date()
    date =today-datetime.timedelta(days=7)
    blogs=Blog.objects.filter(read_details__date__lt=today,read_details__date__gte=date) \
                      .values('id','title') \
                      .annotate(read_num_sum=Sum('read_details__read_num')) \
                      .order_by('-read_num_sum')
    return blogs[:7]

def home(request):
    blog_content_type =ContentType.objects.get_for_model(Blog)
    dates,read_nums=get_7_days_read_data(blog_content_type)

    #获取7天缓存数据
    hot_data_7days=cache.get('hot_data_7days')
    if hot_data_7days is None:
        hot_data_7days=get_7_days_blog()
        cache.set('hot_data_7days',hot_data_7days,3600)
    
    context={}
    context['dates']=dates
    context['read_nums']=read_nums
    context['hot_data_ysday']=get_ysday_hot_data(blog_content_type)
    context['hot_data_day']=get_day_hot_data(blog_content_type)
    context['hot_data_7days']=hot_data_7days
    return render(request,'home.html', context)
