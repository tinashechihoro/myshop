from django.db import models

class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                           db_index=True,
                           unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'  
                             
