class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def disp(self):
        print("hello world")
        print("name",self.name)
        print("color",self.color)
obj=Car("volvo","red")
obj.disp()