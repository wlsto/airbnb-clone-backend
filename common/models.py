from django.db import models


# Create your models here.
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 해당 클래스가 Abstract 라는 것을 명시
    class Meta:
        abstract = True
