from abc import ABC, abstractmethod

from src.modules.entities.joke import Joke

class AJokeService(ABC) :
  @abstractmethod
  async def get_joke(self) -> Joke : pass