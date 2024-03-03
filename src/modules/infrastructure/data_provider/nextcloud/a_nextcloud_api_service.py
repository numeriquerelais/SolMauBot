from abc import ABC, abstractmethod

from src.modules.entities.document import Document


class ANextcloudService(ABC) :
  @abstractmethod
  async def get_document(self, file_name : str) -> Document | None : pass

  @abstractmethod
  async def get_last_report(self, path_name : str, file_name : str)  -> Document | None : pass

  @abstractmethod
  async def get_documents(self, path : str) -> list[Document] | None : pass