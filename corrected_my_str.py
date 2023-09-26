class My_Str:
    def __init__(self, s):
        self.s = s

    def count(self, volue, start=0, end=None):
        counter = 0
        s1 = self.s[start:end]
        for i in range(len(s1)):
            if s1[i] == volue[0]:
                if s1[i:i + len(volue)] == volue:
                    counter += 1
        return counter  
    
    def endswith(self,volue, start=0, end=None):
        s1 = self.s[start:end]
        if volue in s1:
            if s1[-1] == volue[-1]:
                return True
        return False 
    
    def format(self,*volue):
        s1 = ""
        count = 0
        for i in self.s:
            if i == "{":
                s1 += volue[count]
                count += 1
            elif i == "}":
                s1 += ""
            else:
                s1 += i
        return s1

           
def main():

    my_str = My_Str("Hello, Hello I am {} And my age is {} Welcome tocom My id is {} comWor\tld W\torld")
    print(my_str.count("llo",1,15))
    print(my_str.endswith("llo",1,5))
    print(my_str.format("klon","45","f5"))

if __name__ == "__main__":
    main()

