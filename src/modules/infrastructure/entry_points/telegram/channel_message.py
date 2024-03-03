from telegram._utils.types import ReplyMarkup
from telegram.ext._utils.types import BT

from src.modules.infrastructure.telegram.a_channel_infos import AChannelInfos

class ChannelMessage(AChannelInfos) :
  def __init__(self, bot: BT, chat_id : int, message_id: int, text: str, markup : ReplyMarkup|None  = None, return_value : int|None = None) -> None:
    super().__init__(bot, chat_id, message_id, return_value)
    self.text = text
    self.markup = markup