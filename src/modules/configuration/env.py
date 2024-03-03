'''
Module env.py
'''

from collections import namedtuple
import json

class Env:
  def __init__(self, env) -> None:
    self.tokens = env.tokens
    self.name = env.name
    self.version = env.version
    self.nextcloud = env.nextcloud

  def __str__(self):
    tokens=json.dumps(self.tokens)
    return f'Name {self.name} {self.version} tokens : {tokens} nextCloud [host : {self.nextcloud.host} login : {self.nextcloud.login}, password : {self.nextcloud.password}]'
  
  def customSettingsDecoder(settings):
    return namedtuple('X', settings.keys())(*settings.values())

  @staticmethod
  def read_env_variables(path: str) :
    with open(path, 'r') as f:
      settings = json.load(f, object_hook=Env.customSettingsDecoder)
      return Env(settings)
