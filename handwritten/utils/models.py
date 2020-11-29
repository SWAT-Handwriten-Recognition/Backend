"""Models Utilities"""

from django.db import models

class HandwrittenModel(models.Model):
    """
    This class is a base model to App because contains the attributes common
    -created (DateTime)
    -modified (Datatime)
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time was created'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text='Date time was modified'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'