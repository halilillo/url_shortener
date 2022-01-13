from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.shortcuts import get_object_or_404, redirect, reverse

from .models import Url


class UrlCreate(CreateView):
    model = Url
    fields = ['url']
    template_name = "urls/url_create.html"

    def get_success_url(self):
        return reverse('urls:url_detail', args=[self.object.id])
    

class UrlDetail(DetailView):
    model = Url
    template_name = "urls/url_detail.html"


def redirect_view(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.url)