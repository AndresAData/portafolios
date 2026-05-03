from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from my_apps.portafolios.models import Project

@receiver(pre_save, sender=Project)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        
        base_slug = slugify(instance.title)
        unique_part = str(uuid.uuid4())[:8]
        
        instance.slug = f'{base_slug}-{unique_part}'
