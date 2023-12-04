#Understanding generators and iterators
print("\nWilson - Day 17 of 100DaysOfCode")
print("\nUnderstanding generators and iterators")

#iterator
class Iterator:
  def __iter__(self):
    self.value = 1
    return self

  def __next__(self):
    if self.value <= 5:
      result = self.value
      self.value += 1
      return result
    else:
      raise StopIteration
iter = Iterator()
for item in iter:
  print(item)

#generrrator
print("\ngenerator")
def generator():
    value = 1
    while value <= 5:
        yield value
        value += 1
gen = generator()
for item in gen:
    print(item)
