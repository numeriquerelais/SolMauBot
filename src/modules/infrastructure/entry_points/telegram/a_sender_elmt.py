from abc import ABC, abstractmethod
from src.modules.infrastructure.telegram.a_channel_infos import AChannelInfos

class ASenderElmt(ABC):
  @staticmethod
  @abstractmethod
  async def send(channelInfos : AChannelInfos)  -> int|None : pass
