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

    def endswith(self, volue, start=0, end=None):

        s1 = self.s[start:end]
        if volue in s1:
            if s1[-1] == volue[-1]:
                return True

        return False

    def format(self, *volue):

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

    def isalnum(self):
        s1 = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz"
        is_alnum = True
        for simvol in self.s:
            if simvol not in s1:
                is_alnum = False
                break
        return is_alnum

    def isalpha(self):
        s1 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz"
        is_alpha = True
        for simvol in self.s:
            if simvol not in s1:
                is_alpha = False
                break
        return is_alpha

    def isdigit(self):
        s1 = "0123456789"
        is_digit = True
        for simvol in self.s:
            if simvol not in s1:
                is_digit = False
                break
        return is_digit

    def isidentifier(self):
        s1 = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz_"
        s2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz_"
        is_identifier = True
        for simvol in self.s:
            if self.s[0] not in s2:
                is_identifier = False
                break
            elif simvol not in s1:
                is_identifier = False
                break
        return is_identifier



def main():

    my_str = My_Str(
        "Hello, Hello I am {} And my age is {} Welcome tocom My id is {} comWor\tld W\torld")
    # my_str = My_Str("D584lkj69")
    print(my_str.count("llo", 1, 15))
    print(my_str.endswith("llo", 1, 5))
    print(my_str.format("klon", "45", "f5"))
    print(my_str.isalnum())
    print(my_str.isalpha())
    print(my_str.isdigit())
    print(my_str.isidentifier())



if __name__ == "__main__":
    main()
