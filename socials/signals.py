from PIL import Image
from io import BytesIO
import logging
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post,PostImage,Product



THUMBNAIL_SIZE = (200, 200)
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=PostImage)
def generate_thumbnail(sender, instance, **kwargs):
    logger.info("Generating thumbnail for product", instance.post.id,)
    image = Image.open(instance.image)
    image = image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE, Image.LANCZOS)
    temp_thumb = BytesIO()
    image.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)

    instance.thumbnail.save(
    instance.image.name,
    ContentFile(temp_thumb.read()),
    save=False,)
    temp_thumb.close()


@receiver(pre_save, sender=Product)
def generate_thumbnail(sender, instance, **kwargs):
    #logger.info("Generating thumbnail for product", instance.po.id,)
    image = Image.open(instance.image)
    image = image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE, Image.LANCZOS)
    temp_thumb = BytesIO()
    image.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)

    instance.thumbnail.save(
    instance.image.name,
    ContentFile(temp_thumb.read()),
    save=False,)
    temp_thumb.close()