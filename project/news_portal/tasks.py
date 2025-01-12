from celery import shared_task
from .models import Post
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@shared_task()
def send_notification(pk):
    post = Post.objects.get(pk=pk)
    title = post.article_title
    preview = post.preview()
    categories = post.category.all()
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_emails += [s.email for s in subscribers]

    subscribers_emails = set(subscribers_emails)
    html_content = render_to_string(
        'post_created_email.html', {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/post{pk}'
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





