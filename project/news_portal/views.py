from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostFilter
from .forms import PostForm
from .models import Post



class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        if self.request.path == '/posts/search/':
            context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/articles/create/':
            post.post_type = 'A'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')