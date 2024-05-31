from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.base import RedirectView
from blog.forms import PostForm
from blog.models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    """
    a class based view that renders the index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'ali'
        context["posts"] = Post.objects.all()
        return context


class RedirectToMaktab(RedirectView):
    permanent = False
    url = "https://maktabkhooneh.com/"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('blog.view_post',)
    queryset = Post.objects.filter(status=True)
    paginate_by = 5
    context_object_name = 'posts'
    ordering = ['-created_date']


class PostDetailView(LoginRequiredMixin, DetailView):
    permission_required = 'blog.delete_post'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/posts/'
