import unittest
import sys
sys.path.append('../')

from src.modules.configuration.env import Env

class TestEnv(unittest.TestCase):
  def test_when_config_file_is_not_found_then_raise_an_error(self):
    with self.assertRaises(FileNotFoundError):
      Env.read_env_variables("not_found_env_test.json")

  def test_when_config_file_is_correct_then_env_is_correctly_initialized(self):
    env = Env.read_env_variables("tests/modules/configuration/correct_env_test.json")
    self.assertEqual("Bot", env.name)
    self.assertEqual("V1.0", env.version)
    self.assertEqual(2, len(env.tokens))
    self.assertEqual("telegram-token", env.tokens.telegram)
    self.assertEqual("blague-api-token", env.tokens.blagueApi)
    self.assertEqual("http://localhost", env.nextcloud.host)
    self.assertEqual("_login_", env.nextcloud.login)
    self.assertEqual("_password_", env.nextcloud.password)

if __name__ == '__main__':
  unittest.main()