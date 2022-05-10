# generators
def double_num(iterable):
  for i in iterable:
    yield i + i

for i in double_num(range(1, 9999)):
  print(i)
  if i >= 30:
    break

values = (-x for x in [1,2,3,4,5])
for x in values:
  print(x)

# generator directly to list type
gen_to_list = list(values)
print(gen_to_list)

