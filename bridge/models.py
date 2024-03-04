from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.conf import settings



class WandBIntegration(models.Model):
    """
    A wandb integration

    """

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="omero_user",
        help_text="The user that created the dataset",
    )
    api_token = models.CharField(
        max_length=9000,
        help_text="The api token",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "api_token"],
                name="Unique user and workspace",
            )
        ]

    


