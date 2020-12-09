class Bat:
  species = 'Baty'
  
  def __init__(self, can_fly=True):
    self.fly = can_fly
  
  def say(self, msg):
    msg = ".."
    return msg

  def sonar(self):
    return "))..(("
  
if __name__ == '__main__':
  b = Bat()
  b.say('w')
  b.sonar