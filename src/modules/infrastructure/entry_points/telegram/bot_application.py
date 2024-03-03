from telegram.ext import ApplicationBuilder,Application, ContextTypes, PrefixHandler
from telegram import ReplyKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram._utils.types import ReplyMarkup
from telegram.ext._utils.types import BT

from src.modules.infrastructure.telegram.channel_document import ChannelDocument
from src.modules.infrastructure.telegram.channel_message import ChannelMessage

class BotApplication :
  application : Application = None

  def __init__(self, token: str) -> None:
    self.application = ApplicationBuilder().token(token).build()

  
