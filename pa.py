class myClass:
    __privateVar=27
    def __privMeth(self):
        print("I'M INSIDE myClass")

    def hello(self):
        print("PRIVATE VARIABLE VALUE:",myClass.__privateVar) 
foo = myClass()
foo.hello()
foo.__privMeth()     
