from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('search/', PostList.as_view(), name='post_filter'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
