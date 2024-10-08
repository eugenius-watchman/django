from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
         # querying genetic relationship
         content_type = ContentType.objects.get_for_models(obj_type, 1)
    
         return TaggedItem.objects \
             .select_related('tag') \
             .filter(
                 content_type=content_type,
                 object_id=1
             )
    
class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.label
    
    
class TaggedItem(models.Model):
    objects = TaggedItemManager()
    # use type(product, video, article)
    #id of target object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type =  models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()