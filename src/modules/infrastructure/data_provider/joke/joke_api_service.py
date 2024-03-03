from blagues_api import BlaguesAPI, BlagueType, Blague

from src.modules.entities.joke import Joke
from src.modules.infrastructure.data_provider.joke.a_joke_api_service import AJokeService

class JokeApiService(AJokeService) :
  def __init__(self, blague_api : BlaguesAPI) -> None:
    self.__api : BlaguesAPI = blague_api

  async def get_joke(self) -> Joke :
    blague : Blague = await self.__api.random(disallow=[BlagueType.LIMIT, BlagueType.BEAUF, BlagueType.DARK])
    return Joke(blague.joke, blague.answer)

    