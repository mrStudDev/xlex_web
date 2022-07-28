from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostsXlex, Category
from .forms import PostForm, EditForm, AddCategoryForm
from django.urls import reverse_lazy


class PostsListView(ListView):
    model = PostsXlex
    template_name = 'templates_posts/posts_list.html'
    ordering = ['-data']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostsListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostsSingleView(DetailView):
    model = PostsXlex
    template_name = 'templates_posts/post_single.html'


def CategoryView(request, cats):
    category_posts = PostsXlex.objects.filter(category=cats)
    return render(request, 'templates_posts/categories.html', {'cats': cats.title(), 'category_posts': category_posts})


class AddPostView(CreateView):
    model = PostsXlex
    form_class = PostForm
    template_name = 'templates_posts/add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'templates_posts/add_category.html'


class UpdatePostView(UpdateView):
    model = PostsXlex
    form_class = EditForm
    template_name = 'templates_posts/update_post.html'
    success_url = reverse_lazy('home')


class DeletePostView(DeleteView):
    model = PostsXlex
    template_name = 'templates_posts/delete_post.html'
    success_url = reverse_lazy('home')    

  

