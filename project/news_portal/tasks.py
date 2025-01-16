import datetime

from celery import shared_task
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import  timezone

@shared_task()
def send_notification(pk):
    post = Post.objects.get(pk=pk)
    title = post.article_title
    preview = post.preview()
    categories = post.category.all()
    subscribers_emails = User.objects.filter(subscriptions__category__in=categories).values_list('email', flat=True)

    subscribers_emails = set(subscribers_emails)
    html_content = render_to_string(
        'post_created_email.html', {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task()
def periodic_tasks():
    last_week = timezone.now() - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = Category.objects.filter(posts__in=posts)
    subscribers_emails = User.objects.filter(subscriptions__category__in=categories).values_list('email', flat=True)

    subscribers_emails = set(subscribers_emails)
    html_content = render_to_string(
        'weekly_email.html', {
            'posts': posts,
            'link': f'{settings.SITE_URL}/posts/'
        }
    )

    msg = EmailMultiAlternatives(
        subject="Посты за неделю",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


