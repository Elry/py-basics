from human import Human

class Ubermesch(Human):
  species = "Ubermesch"

  def __init__(self, name, movie=False, superpowers=["mind", "speed"]):
    self.fictional = False
    self.movie = movie
    self.superpowers = superpowers
    super().__init__(name)

  def sing(self):
    return "LMAO"
  
  def boast(self):
    for power in self.superpowers:
      print("{p} this is power".format(p=power))

if __name__ == '__main__':
  sup = Ubermesch(name="triz")

  if isinstance(sup, Human):
    print("also human")
  if type(sup) is Ubermesch:
    print('also enlightned')

  print(Ubermesch.__mro__)
  sup.boast()