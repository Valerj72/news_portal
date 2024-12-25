from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if not kwargs['action'] == 'post add':
        return

    emails = User.objects.filter(subscriptions__category__in=instance.category.all()
    ).values_list('email', flat=True)
    subject = f'Новая статья в категории {instance.category.all()}'

    text_content = (
        f'Статья: {instance.article_title}\n'
        f'Автор: {instance.author}\n\n'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Статья: {instance.article_title}<br>'
        f'Автор: {instance.author}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()