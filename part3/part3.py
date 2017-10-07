class Data:
    def __init__(self, data):
        self.data = data
        self.type_name = type(data)

    def concat_data(self, a, b):
        if(not (isinstance(a, int) or isinstance(b, int))):  # point 1
            return a+b
        else:
            return None

    def reverse_data(self, a):
        if(not isinstance(a, int)):
            return a[::-1]
        else:
            return None

    def return_last(self, a):
        if(not isinstance(a, int)):
            return a[len(a)-1]
        else:
            return None

    def comparator(self, a, b):
        if(not (isinstance(a, int) or isinstance(b, int))):
            return a == b
        else:
            return None

    def mixture(self, a, b):
        if(not (isinstance(a, int) or isinstance(b, int))):
            return a + ''.join(b)
        else:
            return None



if __name__ == "__main__":
    str_data = Data("python")
    int_data = Data(3)
    list_data = Data(["python", 3, True])
    test_list = [str_data, int_data, list_data]

    for item in test_list:
        print()
        print(item.comparator("Apple", "Oranges"))
        print(item.return_last("Apple"))
        print(item.reverse_data("Apple"))
        print(item.concat_data("Apple", "Oranges"))
        print(item.mixture("Apple",[" Oranges", " Grapes"]))
"""
todo:

Instantiate the object with an argument and apply all the operations on that argument only.
DO NOT Pass any extra argument while envoking the methods. Thereby utilizing the attributes of the
class itself. 
One of the primary reasons for using classes is modularity. 
You can create objects of the same class with same properties anywhere without worrying about the arguments.
Since all the required attributes are assigned by the class itself.

"""
