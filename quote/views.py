from django.shortcuts import render
from .models import marq
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def mar(request):
    inst = marq.objects.all()

    paginator = Paginator(inst, 30)
    page = request.GET.get('page')
    try:
        inst = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        inst = paginator.page(1)
    except EmptyPage:

        # If page is out of range deliver last page of results
        inst = paginator.page(paginator.num_pages)
    # marquee=Post.objects.marquee()
    context = {'inst': inst, 'page': page}
    return render(request, 'quote/quote.html', context)