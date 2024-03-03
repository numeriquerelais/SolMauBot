from src.modules.entities.document import Document

async def get_document(self, name) -> Document :
  return Document()

async def get_last_report(self) -> Document :
  return Document()

async def get_documents(self, name) -> list[Document]:
  return [Document(), Document()]