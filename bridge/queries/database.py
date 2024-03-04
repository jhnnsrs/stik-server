from bridge.conn import get_conn
from bridge import types, filters
from strawberry_django import pagination
import strawberry

async def projects(filters: filters.ProjectFilter | None = None, pagination: pagination.OffsetPaginationInput | None = None) -> list[types.Project]:
    x = await get_conn().projects()
    print(x)
    return [types.Project(value=y) for y in x]


async def project(id: strawberry.ID) -> types.Project:
    x = await get_conn().project(name=id)
    return types.Project(value=x)