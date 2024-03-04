import strawberry
import strawberry.django
from strawberry import auto
from typing import List, Optional, Annotated, Union, cast
import strawberry_django
from bridge import models, scalars, filters, enums, basemodels
from django.contrib.auth import get_user_model
from koherent.models import AppHistoryModel
from authentikate.strawberry.types import App
from kante.types import Info
import datetime

from itertools import chain
from enum import Enum
from strawberry.experimental import pydantic
from pydantic import BaseModel

@strawberry_django.type(get_user_model())
class User:
    id: auto
    sub: str
    username: str
    email: str
    password: str


    @strawberry_django.field
    def integrations(self) -> list["WandBIntegration"]:
        return models.WandBIntegration.objects.filter(user=self).all()
    




@pydantic.type(basemodels.DatabaseModel)
class Project:
    id: str
    name: str
    url: str


    


@strawberry_django.type(models.WandBIntegration)
class WandBIntegration:
    id: auto
    api_token: str
    user: User