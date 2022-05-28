# Extended list...

class SuperList(list):      # Using list as a parent class
    def __len__(self):
        return 1000


list_one = SuperList()
print(len(list_one))

list_one.append(3)
print(len(list_one))

print(list_one[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))

print(isinstance(list_one, SuperList))



