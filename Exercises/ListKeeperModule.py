class ListKeeper:
  lists = {}
  def __init__(self):
    self.lists["example"] = [1,2,3,4,5]

  def show(self):
    names = []
    for x in self.lists:
      names.append(x)
    return names

  def add(self, name, list):
    self.lists[name] = list

  def delete(self, name):
    self.lists.pop(name)

  def sort(self, name):
    x = self.lists.get(name)
    x.sort()
    return x

  def append(self, name, list):
    for newItem in list:
      x = self.lists.get(name)
      x.append(newItem)
"