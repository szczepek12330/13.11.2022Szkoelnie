class Customer:
    def __init__(self, name:str, address:str, phone:int):
        self.__name = name
        self.__adress = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


test = Customer("Tomek", "Kielce", 323232323)
test.set_name("Adam")
print(test.get_name())