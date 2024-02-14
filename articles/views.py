from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, ProposePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# def articles(request):
#    return render(request, 'articles/articles_list.html')

def LikeView(request, pk):
    # post = get_object_or_404(Post, id=request.Post.get('post_id'))
    post = Post.objects.get(id=pk)
    post.likes.add(request.settings.AUTH_USER_MODEL)
    return HttpResponseRedirect(reverse('articles/article-detail', args=[str(pk)]))


class ArticlesHomeView(ListView):               # main page for articles (show all articles)
    model = Post
    template_name = 'articles/articles_list.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):       # articles categories list for nav bar
        categories_menu = Category.objects.all()
        context = super(ArticlesHomeView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        return context


def CategoryListView(request):            # articles categories list for single page
    categories_menu_list = Category.objects.all()
    return render(request, 'articles/category_list.html', {'categories_menu_list': categories_menu_list})


def CategoriesView(request, categories):      # show articles for particular category
    categories_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'articles/categories.html',
                  {'categories': categories.title().replace('-', ' '),
                   'categories_posts': categories_posts})


class ArticlesDetailView(DetailView):          # info about particular article
    model = Post
    template_name = 'articles/articles-detail.html'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(ArticlesDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        all_likes = stuff.all_likes()
        context["categories_menu"] = categories_menu
        context["all_likes"] = all_likes
        return context


class AddPostView(CreateView):           # function for adding article post
    model = Post
    form_class = PostForm
    template_name = 'articles/add.html'
    # fields = '__all__'


class AddCategoryView(CreateView):         # function for adding article category
    model = Category
    template_name = 'articles/category_add.html'
    fields = '__all__'


class EditPostView(UpdateView):             # function for editing article post
    model = Post
    form_class = PostForm
    template_name = 'articles/edit.html'


class DeletePostView(DeleteView):           # function for deleting article post
    model = Post
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('articles:all')


class AddProposePostView(CreateView):
    model = Post
    form_class = ProposePostForm
    template_name = 'articles/propose_post.html'
    success_url = reverse_lazy('home')


