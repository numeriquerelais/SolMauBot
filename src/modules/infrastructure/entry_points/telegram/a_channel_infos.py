from abc import ABC
from telegram.ext._utils.types import BT

class AChannelInfos (ABC) :
  def __init__(self, bot: BT, chat_id : int, message_id: int, return_value : int|None = None) -> None:
    self.bot = bot
    self.chat_id = chat_id
    self.message_id = message_id
    self.return_value = return_value
