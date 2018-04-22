from django.db import models
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.db.models.deletion import CASCADE
from main.utils import slugify
from main import validators

USER = settings.AUTH_USER_MODEL


class Article(models.Model):
    owner = models.ForeignKey(USER, on_delete=CASCADE)
    title = models.CharField(null=True, blank=True, max_length=200,
                             validators=[validators.validate_title])
    body = models.TextField(null=True, blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    num_slug = models.SmallIntegerField(blank=False, null=False, default=1, validators=[
                                        validators.validate_num_slug])
    
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)


def Article_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.body == None:
        instance.title = "لم يتم كتابة محتوى"
    if instance.title == None:
        instance.title = "لم يتم كتابة عنوان"
    if not instance.slug:
        if instance.num_slug == 1:
            instance.slug = slugify("أجدد التقنيات")
        elif instance.num_slug == 2:
            instance.slug = slugify("عن لغات البرمجة")
        elif instance.num_slug == 3:
            instance.slug = slugify("أطلب المساعدة")
    # هذا الحل هو حل مؤقت لتكوين slugs مشتركة بين الobjects

   

pre_save.connect(Article_pre_save_receiver, sender=Article)
