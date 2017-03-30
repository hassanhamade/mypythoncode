class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        print("Class Point object created")
    def __del__(self):
        class_name=self.__class__.__name__
        print("Class {} object destroyed".format(class_name))
    def print(self):
            print("X={}".format(self.x))
            print("Y={}".format(self.y))

p1=Point(10,10)
p2=Point(20,20)
p1.print()
p2.print()
del(p1)
