from dataclasses import dataclass

@dataclass
class Joke :
  question : str
  answer : str
    
  def __init__(self, joke : str, answer : str) -> None :
    self.question : str = joke
    self.answer : str = answer

  def __str__(self):
    return f"question : {self.question} answer : {self.answer}"