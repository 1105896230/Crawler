
#coding-utf-8
class Hello:
    def __init__(self,name):
        self.name=name;

    def sayHello(self):
        print ("Hello {0}".format(self.name));



class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print ("Hi{0}".format(self.name));

h=Hello("lin")
h.sayHello()
h1=Hi("lin")
h1.sayHi()