from src.modules.entities.joke import Joke
from src.modules.infrastructure.data_provider.joke.a_joke_api_service import AJokeService

async def get_joke(self, get_joke_function : AJokeService.get_joke) -> Joke :
  return Joke()