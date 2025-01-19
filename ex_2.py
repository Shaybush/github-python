class Garbage:
  def __init__(self, location, capacity, quantity):
    self.location = location
    self.capacity = float(capacity)
    self.quantity = float(quantity)
    if self.quantity > self.capacity // 2:
      self.quantity = 0

  def _str_(self):
    return f"self.locayion = {self.location}"

def empty_garbage(garbage_list):
  garbage_cans_location = []
  for i in garbage_list:
    if i.quantity == 0:
      garbage_cans_location.append(i.location)
  return garbage_cans_location

garbage_can_1 = Garbage("13_street", 100, 35)
garbage_can_2 = Garbage("14_street", 100, 55)
garbage_can_3 = Garbage("15_street", 100, 49)
garbage_can_4 = Garbage("16_street", 100, 30)
garbage_can_5 = Garbage("17_street", 100, 25)

garbage_cans = [garbage_can_1, garbage_can_2, garbage_can_3, garbage_can_4, garbage_can_5]
locations = empty_garbage(garbage_cans)
print(locations)



