"""Containers module."""

from dependency_injector import containers, providers
from blagues_api import BlaguesAPI
from nc_py_api import Nextcloud
import logging
import sys

from src.modules.configuration.env import Env
from src.modules.infrastructure.data_provider.joke.joke_api_service import JokeApiService
from src.modules.infrastructure.entry_points.telegram.bot_application import BotApplication


class Container(containers.DeclarativeContainer):
  settings = Env.read_env_variables("env.json")

  logging = providers.Resource(
    logging.basicConfig,
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  )

  nextcloud_api_service = providers.Factory(
    Nextcloud,
    nextcloud_url=settings.nextcloud.host, 
    nc_auth_user=settings.nextcloud.login, 
    nc_auth_pass=settings.nextcloud.password
  )

  joke_api_service = providers.Factory(
    JokeApiService,
    blague_api = providers.Singleton(
      BlaguesAPI,
      token=settings.tokens.blagueApi
    ),
  )

  botApplication = providers.Factory(
    BotApplication,
    token = settings.tokens.telegram
  )