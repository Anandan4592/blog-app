from django.utils import timezone
from django.db.models import Count, Q
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError as DjangoValidationError
from rest_framework.response import Response
from .models import Blog, Author, Category
from .serializers import BlogCreateSerializer, AuthorCreateSerializer, BlogSerializer, BlogDetailSerializer, AuthorSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


Author = get_user_model()

class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            blog = serializer.save()
            if blog.is_published:
                message = "Blog post has been published successfully."
            else:
                message = "Since the content is less than 500 characters,blog post has been saved as a draft."
            return Response({"message": message, },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            # Handle any other exceptions that might occur
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateAuthor(generics.CreateAPIView): # View for creating an author
    queryset = Blog.objects.all()
    serializer_class = AuthorCreateSerializer

class CreateCategory(generics.CreateAPIView): # View for creating a category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ViewBlogs(generics.ListAPIView):     # View for listing all posts with title, author, and publish date
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer


class BlogDetail(generics.ListAPIView):     #View for listing post and author details for each published post
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogDetailSerializer
def post(self, request):
        blog_id = request.data.get('id')
        if not blog_id:
            return Response({"error": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        blog = get_object_or_404(Blog, id=blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopAuthors(generics.ListAPIView):   # View for retrieve top 3 authors with the most posts in the last 6 months
    serializer_class = AuthorSerializer

    def get(self, request):
        six_months_ago = timezone.now() - timezone.timedelta(days=180)  # Get top 3 authors with the most posts in the last 6 months
        top_authors = Author.objects.annotate(
            num_posts=Count('blogs', filter=Q(blogs__publish_date__gte=six_months_ago))
        ).order_by('-num_posts')[:3]

        # Serialize the response
        author_data = [{"username": author.username, "num_posts": author.num_posts} for author in top_authors]
        return Response(author_data, status=status.HTTP_200_OK)


class PopularCategory(generics.ListAPIView): # View for showing the most popular category in the last 6 months
    serializer_class = CategorySerializer

    def get(self, request):
        # Get the most popular category in the last 6 months
        six_months_ago = timezone.now() - timezone.timedelta(days=180)
        
        # Annotate categories with the count of blogs published in the last 6 months
        popular_category = Category.objects.annotate(
            num_blogs=Count('blog', filter=Q(blog__publish_date__gte=six_months_ago))
        ).order_by('-num_blogs').first()  # Get the category with the most blogs
        
        if popular_category:
            category_data = {
                "name": popular_category.name,
                "description": popular_category.description,
                "num_blogs": popular_category.num_blogs
            }
            return Response(category_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No blogs found in the last 6 months."}, status=status.HTTP_404_NOT_FOUND)
