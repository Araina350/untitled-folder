class IOString:
    def _init_(self):
        self.str1 = " "
    def get_String(self):
        self.str1 = input("ENTER PLEASE")    
    def print_String(self):
        print("RESULT IS",self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()