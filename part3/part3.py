class Data:
    def __init__(self, data):
        self.data = data
        self.type_name = type(data)

    def concat_data(self, a, b):
        if(type(a)!=int and type(b)!=int):  # point 1
            return a+b
        else:
            return None
            
    def reverse_data(self, a):
        if(type(a) != int):
            return a[::-1]
        else:
            return None

    def return_last(self, a):
        if(type(a) != int):
            return a[len(a)-1]
        else:
            return None

    def comparator(self, a, b):
        if(type(a)!=int and type(b)!=int):
            return a == b
        else:
            return None

    def mixture(self, a, b):
        if(type(a)!=int and type(b)!=int):
            return a + ''.join(b)
        else:
            return None
        
  

if __name__ == "__main__":
    str_data = Data("python")
    int_data = Data(3)
    list_data = Data["python", 3, True]
    
    str_is_equal = str_data.comparator("Apple", "Oranges")
    str_last_elem = str_data.return_last("Apple")
    str_reverse_data = str_data.reverse_data("Apple")
    str_list_data = str_data.concat_data("Apple", "Oranges")
    

"""

1. better way to check for object type: isinstance(a, str)
a = 1
isinstance(a, int) => returns True else returns False

b = "apple"
isinstance(b, str) => returns True else retruns False

c = [1, 2, 3, "Apple"]
isinstance(c, list) => returns True else returns False

2. methods  are correct
3. I have created 3 objects you can test the class through them. I have checked methods with string object. 
"""



  
