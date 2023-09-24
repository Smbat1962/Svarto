class My_Str:
    def __init__(self, s):
        self.s = s

    def capitalize(self):
        if 65 < ord(self.s[0]) < 90:
            return self.s

        return chr(ord(self.s[0]) - 32) + self.s[1:]

    def casefold(self):
        s1 = ""
        for simvol in self.s:
            if 65 < ord(simvol) < 90:
                s1 += chr(ord(simvol) + 32)
            else:
                s1 += simvol
        return s1
    
    def center(self, leng, simvol = None):
        s1 = ""
        for i in range(leng):
            if 0 <= i <= (leng - len(self.s))//2:
                if simvol == None:
                    s1 += " "
                else:
                    s1 += simvol
        s1 += self.s
        for i in range(leng):        
            if (leng + len(self.s))//2 < i < leng :
                if simvol == None:
                    s1 += " "
                else:
                    s1 += simvol
        
        return s1
    
    def count(self, value, start=0, end=None):
        counter = 0
        s1 = self.s[start:end]
        s2 = s1.split(" ")
        #print(s2)
        for i in s2:
            if i == value:
                counter += 1
        return counter   
    def endswith(self,value, start=0, end=None):
        s1 = self.s[start:end]
        if value in s1:
            return True
        else:
            return False 

    def expandtabs(self,tabsize=None):
        s1 = ""
        for i in self.s:
            if i == "\t":
                if tabsize == None:
                    s1 += i
                else:
                    s1 += " "*tabsize
            else:
                s1 += i
        return s1
    def find(self,volue, start=0, end=None):
        s1 = self.s[start:end]
        for i in range(len(self.s)):
            if self.s[i] == volue[0]:
                if volue in s1:
                    return i
                else:
                    return -1

my_str = My_Str("hello , Hello And Welcome to to My Wor\tld W\torld")
print(my_str.capitalize())
print(my_str.casefold())
print(my_str.center(65,"+"))
print(my_str.count("to",10,31))
print(my_str.endswith("Hello",8,13))
print(my_str.expandtabs(5))
print(my_str.find("Wor",5,47))
