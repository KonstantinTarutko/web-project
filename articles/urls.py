from django.urls import path
from .views import ArticlesHomeView, ArticlesDetailView, \
    AddPostView, EditPostView, \
    DeletePostView, AddCategoryView, CategoriesView, \
    CategoryListView, AddProposePostView, LikeView

app_name = 'articles'

urlpatterns = [
    # path('main/', views.articles, name='articles'),
    path('all/', ArticlesHomeView.as_view(), name='all'),
    path('all/<int:pk>', ArticlesDetailView.as_view(), name='article-detail'),
    path('add/', AddPostView.as_view(), name='add'),
    path('category', AddCategoryView.as_view(), name='category'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit'),
    path('<int:pk>delete/', DeletePostView.as_view(), name='delete'),
    path('categories/<str:categories>/', CategoriesView, name='categories'),
    path('categories-list/', CategoryListView, name='categories-list'),
    path('propose-post/', AddProposePostView.as_view(), name='propose-post'),
    path('likes/<int:pk>/', LikeView, name='like-article'),
]
