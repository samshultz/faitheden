from django.shortcuts import render

from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from random import randint


def Post_List(request):
    object_list = Post.objects.all().order_by('-published')
# the quotes used in the home page (marquee)
    # all_quote = marq.objects.all()
    # counter = 0
    # for i in all_quote:
    #     counter = counter + 1

    # current_quote = ""
    # first = datetime.date(2017, 10, 6)
    # current = datetime.datetime.now()
    # current_date = datetime.date.isoformat(current)
    # first_date = datetime.date.isoformat(first)

    # if first_date != current_date:
    #     num = randint(1, counter)
    #     current_quote = marq.objects.get(pk=num)
    # else:
    #     first_date = current_date

    paginator = Paginator(object_list, 4)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        object_list = paginator.page(1)
    except EmptyPage:

        # If page is out of range deliver last page of results
        object_list = paginator.page(paginator.num_pages)
    # marquee=Post.objects.marquee()
    context = {'object_list': object_list,
               'page': page}  # 'current_quote': current_quote }
    return render(request, 'home/home.html', context)

#


def Post_Detail(request, id):
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.body)
    context = {'instance': instance, 'share_string': share_string}
    return render(request, 'home/detail.html', context)

