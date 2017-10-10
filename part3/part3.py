class Data:
    def __init__(self, data):
        self.data = data
        self.type_name = type(data)

    def concat_data(self, a):
        if(not (self.type_name == int or self.type_name == list or isinstance(a, int))):  # point 1
            return self.data + a
        else:
            return None

    def reverse_data(self):
        if(self.type_name != int):
            return self.data[::-1]
        else:
            return None

    def return_last(self):
        if(self.type_name != int):
            return self.data[len(self.data) - 1]
        else:
            return None

    def comparator(self, a):
        if(not (self.type_name == int or isinstance(a, int))):
            return self.data == a
        else:
            return None

    def mixture(self, a):
        if(not (self.type_name == int or self.type_name == list or isinstance(a, int))):
                return self.data + ''.join(a)
        else:
            return None



if __name__ == "__main__":
    str_data = Data("python")
    int_data = Data(3)
    list_data = Data(["python", 3, True])
    test_list = [str_data, int_data, list_data]

    for item in test_list:
        print()
        print(item.comparator("Apple"))
        print(item.return_last())
        print(item.reverse_data())
        print(item.concat_data(" Oranges"))
        print(item.mixture([" Oranges", " Grapes"]))
"""
todo:

Instantiate the object with an argument and apply all the operations on that argument only.
DO NOT Pass any extra argument while envoking the methods. Thereby utilizing the attributes of the
class itself.
One of the primary reasons for using classes is modularity.
You can create objects of the same class with same properties anywhere without worrying about the arguments.
Since all the required attributes are assigned by the class itself.

"""
"""
concat_data() and mixture() returns None if self.data is not str
"""
