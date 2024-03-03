import sys
sys.path.append('../')
import unittest

from src.modules.use_cases.jokes.get_joke import get_joke
from src.modules.entities.joke import Joke

class TestJokeUseCase(unittest.IsolatedAsyncioTestCase):
  async def test_when_get_joke_is_called_then_joke_is_return(self):
    expectedJoke = Joke("Question", "Answer")
    joke = await get_joke(lambda : Joke("Question", "Answer") )

    self.assertEqual(expectedJoke.joke, joke.question)
    self.assertEqual(expectedJoke.answer, joke.answer)

if __name__ == '__main__':
  unittest.main()