class MyClass:
    def __init__(self, data):
        self.data = data
        self.type_name = type(data)

    def concat_data(self, a, b):
        if(type(a)!=int and type(b)!=int):
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
