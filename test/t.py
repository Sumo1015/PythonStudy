class Base:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def f(self):
        print(self.a,self.b,self.c)


#继承
class Derive(Base):
    def __init__(self,a,b,c,d):
        super(Derive,self).__init__(a,b,c)
        self.d=d



    #多态
    def f(self):
        print(self.d)

print(__name__)
if __name__ == "__main__":
    base=Base(1,2,3)
    base.f()
    derived=Derive(1,2,3,4)
    derived.f()














