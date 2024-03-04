from koherent.types import Info
from bridge import types, models, inputs
from django.conf import settings
from wandb import Api
import socket
from bridge.conn import get_conn

def create_project(info: Info, input: inputs.CreateProjectInput) -> types.Project:


    # lets try if we can reach the omero-server 
    api = get_conn()
    api.create_project(name=input.name, entity=input.entity)
    project = api.project(name=input.name)



    
    return types.Project(id=project.name, name=project.name, url=project.url)

