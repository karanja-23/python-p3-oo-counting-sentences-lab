#!/usr/bin/env python3
import re
class MyString:
  def __init__(self,value=""):
    self.value = value

  @property 
  def value (self):
    return self._value
  
  @value.setter
  def value (self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence (self):
    last_character = (len(self._value)- 1)
    if self._value[last_character] == ".":
      return True
    else:
      return False
  
  def is_question (self):
    last_character = (len(self._value)- 1)
    if self._value[last_character] == "?":
      return True
    else:
      return False

  def is_exclamation (self):
    last_character = (len(self._value)- 1)
    if self._value[last_character] == "!":
      return True
    else:
      return False    
    
  def count_sentences(self):
     sentences = re.split('[.!?]', self.value)
     return len([s for s in sentences if s.strip()])