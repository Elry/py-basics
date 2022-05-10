from bat import Bat
from ubermesch import Ubermesch

class Batman(Bat, Ubermesch):
  def __init__(self, *args, **kwargs):
    Ubermesch.__init__(self, 'anonymous', movie=True, superpowers=['Wealthy'], *args, **kwargs)
    Bat.__init__(self, *args, can_fly=False, **kwargs)
    self.name = "neo"
  
  def sing(self):
    return "tototototoototot"

if __name__ == '__main__':
  sup = Batman
  print(Batman.__mro__)
  print(sup.get_species())
  print(sup.sing())
