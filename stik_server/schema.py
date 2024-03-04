from typing import Any, AsyncGenerator, Type

import strawberry
import strawberry_django
from authentikate.strawberry.permissions import HasScopes, IsAuthenticated, NeedsScopes
from kante.directives import relation, replace, upper
from kante.types import Info
from koherent.strawberry.extension import KoherentExtension
from strawberry import ID
from strawberry.field_extensions import InputMutationExtension
from strawberry.permission import BasePermission
from strawberry_django.optimizer import DjangoOptimizerExtension

from bridge import models, mutations, queries, types
from bridge.channel import image_listen
from bridge.conn import NotionExtension


@strawberry.type
class Query:
    integrations: list[types.WandBIntegration] = strawberry_django.field(extensions=[])
    projects: list[types.Project] = strawberry.field(resolver=queries.projects)
    project = strawberry.field(resolver=queries.project)
    
    me: types.User = strawberry.field(resolver=queries.me)
    


@strawberry.type
class Mutation:
    ensure_integration: types.WandBIntegration = strawberry_django.mutation(
        resolver=mutations.ensure_integration,
    )
    create_project: types.Project = strawberry_django.mutation(
        resolver=mutations.create_project,
    )
    


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    directives=[upper, replace, relation],
    extensions=[
        DjangoOptimizerExtension,
        KoherentExtension,
        NotionExtension
    ],
)
