from django.shortcuts import render
from django.views.generic import *
from bookmark.models import Bookmark # [주의]
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from blog.models import Post

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
    
class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner = self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

def marker_index(request):
    Markerlist = Post.objects.all()
    print(Markerlist)
    context = {'Markerlist': Markerlist}
    return render(request,'bookmark/bookmark_list.html',context)


def marker_detail(request, category):
    Markerlist = Post.objects.filter(name=category)
    context = {'category':category,'centerLat': Markerlist[0].latitude,
'centerLon':Markerlist[0].longtitude,'Markerlist':Markerlist}
    return render(request,'bookmark/bookmark_list.html',context)
    







