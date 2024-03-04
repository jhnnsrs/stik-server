from koherent.types import Info
from bridge import types, models, inputs
from django.conf import settings
from wandb import Api
import socket


async def ensure_integration(info: Info, input: inputs.EnsureIntegration) -> types.WandBIntegration:


    # lets try if we can reach the omero-server 
    try:
        api = Api(api_key=input.token)
        list_users_response =  api = api.projects()

        integration, _ = await models.WandBIntegration.objects.aupdate_or_create(
            user=info.context.request.user,
            api_token=input.token,
        )

        return integration




    except Exception as e:
        raise Exception("Could not connect to Notion. Please check your token.") from e

