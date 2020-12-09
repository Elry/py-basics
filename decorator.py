from functools import wraps

def beg(target_function):
  @wraps(target_function)
  def wrapper(*args, **kwargs):
    msg, say_please = target_function(*args, **kwargs)
    if say_please:
      return "{} {}".format(msg, 'poor...')
    return msg
  return wrapper

@beg
def say(say_please=False):
  msg = "can u?"
  return msg, say_please

print(say())
print(say(say_please=True))