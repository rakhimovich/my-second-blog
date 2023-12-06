from django.urls import path


from apps.blogs.views import index, create_blog, detail_blog, delete_blog, update_blog


urlpatterns = [
    path('', index, name="homepage"),
    path('create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>', detail_blog, name="detail_blog"),
    path('delete/<int:pk>', delete_blog, name="delete_blog"),
    path('update/<int:pk>', update_blog, name="update_blog"),
]