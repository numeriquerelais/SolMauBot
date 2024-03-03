import sys
sys.path.append('../')
import unittest
from unittest.mock import Mock

from blagues_api import BlaguesAPI, BlagueType, Blague
from src.modules.infrastructure.data_provider.joke.joke_api_service import JokeApiService


class TestJokeApiService(unittest.IsolatedAsyncioTestCase):
  async def test_when_blagueApi_is_called_then_a_joke_is_returned(self):
    mockedBlaguesAPI = Mock(BlaguesAPI)
    expectedBlague =  Blague(id=1, type=BlagueType.DEV, joke="joke content", answer="answer content")
    mockedBlaguesAPI.random.return_value = expectedBlague

    api = JokeApiService(mockedBlaguesAPI)
    joke = await api.get_joke()
    self.assertEqual(expectedBlague.joke, joke.question)
    self.assertEqual(expectedBlague.answer, joke.answer)

if __name__ == '__main__':
  unittest.main()