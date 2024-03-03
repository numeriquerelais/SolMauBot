from src.modules.infrastructure.telegram.a_sender_elmt import ASenderElmt
from src.modules.infrastructure.telegram.channel_document import ChannelDocument

class SenderDocument(ASenderElmt) :
  @staticmethod
  async def send(document : ChannelDocument) -> int|None :
    await document.bot.send_document(
      chat_id=document.chat_id,
      reply_to_message_id=document.message_id, 
      document=document.content
    )
    return document.return_value