class get:
    def get1(self):
       self.a=int(input('a = '))     

class log:
    def log1(self):
       self.b=int(input('b = '))     

class dis(get,log):
    def dis1(self):
        sum=self.a+self.b
        print('Sum = ',sum) 

d=dis()
d.get1()
d.log1()
d.dis1()
