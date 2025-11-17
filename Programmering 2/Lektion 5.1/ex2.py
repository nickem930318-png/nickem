class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hej, jag heter {self.name} och är {self.age} år gammal."

anrop = Customer("Alice", 30)
print(anrop.greet())
 
        