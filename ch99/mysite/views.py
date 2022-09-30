from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = Post.objects.all().count()
        post_arr = []
        for i in  range(0, count, 3):
            post_arr.append(Post.objects.all()[i:i+3])
        context["post_arr"] = post_arr
        return context
    
class MakerView(TemplateView):
    template_name = 'bookmark_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     count = Post.objects.all().count()
    #     marker_arr = []
    #     for i in  range(0, count, 3):
    #         marker_arr.append(Post.objects.all()[i:i+3])
    #     context["marker_arr"] = marker_arr
    #     return context


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "사용자만 수정 삭제"
    def dispatch(self, request,*args,**kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request,*args,**kwargs)