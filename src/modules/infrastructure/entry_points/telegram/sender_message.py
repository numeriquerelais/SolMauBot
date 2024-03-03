from src.modules.infrastructure.telegram.a_sender_elmt import ASenderElmt
from src.modules.infrastructure.telegram.channel_message import ChannelMessage

class SenderMessage(ASenderElmt) :
  @staticmethod
  async def send(message : ChannelMessage) -> int|None :
    await message.bot.send_message(
      chat_id=message.chat_id,
      reply_to_message_id= message.message_id, 
      text=message.text,
      reply_markup=message.markup
    )
    return message.return_value