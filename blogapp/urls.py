from django.urls import path
from .views import ViewBlogs, BlogDetail, TopAuthors, PopularCategory, BlogCreateView, CreateAuthor, CreateCategory

urlpatterns = [
    path('blogs/', ViewBlogs.as_view(), name='blog-list'),
    path('blog/details/', BlogDetail.as_view(), name='blog-details'),
    path('top-authors/', TopAuthors.as_view(), name='top-authors'),
    path('category/popular', PopularCategory.as_view(), name='popular-category'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/createauthor/', CreateAuthor.as_view(), name='author-create'),
    path('blogs/createcategory/', CreateCategory.as_view(), name='category-create'),
]
