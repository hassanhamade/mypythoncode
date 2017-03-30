class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
        self.__mult=a*b
        print("Class Point object created")
    def __del__(self):
        class_name=self.__class__.__name__
        print("Class {} object destroyed".format(class_name))
    def print(self):
            print("X={}".format(self.x))
            print("Y={}".format(self.y))
            print("Mult={}".format(self.__mult))
    def getMult(self):
        return self.__mult
    def setMult(self, val):
        self.__mult=val
