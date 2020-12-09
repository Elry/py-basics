class Human:
  species = "H. Sapiens" # class attribute shared by all instances

  def __init__(self, name):
    self._age = 0
    self.name = name

  #all instance methods receive 'self' as first argument
  def say(self, msg):
    print("{name}: {message}".format(name=self.name, message=msg))

  def sing(self):
    return "mom's spaghetti"

  @classmethod
  def get_species(cls):
    return cls.species
  
  @staticmethod
  def grunt():
    return "*ayyy*"

  @property # just like a getter
  def age(self):
    return self._age

  @age.setter
  def age(self, age):
    self._age = age

  @age.deleter
  def age(self):
    del self._age


if __name__ == '__main__':
  a = Human(name="aga")
  a.say('ayy')
  Human.species = "ayys lmaos"
  print(a.grunt())