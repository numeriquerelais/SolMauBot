from attr import dataclass


@dataclass
class Document :
  name : str
  path : str | None
  link : str | None

  def __init__(self, name : str, path : str | None, link : str | None) -> None :
    self.name = name
    self.path = path
    self.link = link