from dataclasses import dataclass
from src.modules.entities.document import Document

@dataclass
class Folder() :
  name : str
  path : str | None
  link : str | None
  content : list[Folder | Document] = [] # type: ignore

  def __init__(self, name : str, path : str | None, link : str | None, content : list[Folder | Document]) -> None : # type: ignore
    self.name = name
    self.path = path
    self.link = link
    self.content = content
