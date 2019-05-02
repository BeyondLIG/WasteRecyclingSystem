from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from apps.scrap.models import Scrap
from pure_pagination import PageNotAnInteger, Paginator


class ScrapListView(View):
    def get(self, request):
        scraps = Scrap.objects.filter(delete=0)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 分页
        p = Paginator(scraps, 5, request=request)
        scraps = p.page(page)
        return render(request, 'scrap-list.html', {'scraps': scraps})
