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

    def islower(self):
        s1 = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
        is_lower = True
        for i in self.s:
            if i in s1:
                is_lower = False
                break
        return is_lower

    def isnumeric(self):
        s1 = "0123456789"
        is_numeric = True
        for i in self.s:
            if i not in s1:
                is_numeric = False
                break
        return is_numeric

    def isprintable(self):
        s1 = "\n\r\t\b\f"
        is_printable = True
        for i in self.s:
            if i in s1:
                is_printable = False
                break
        return is_printable

    def istitle(self):
        s1 = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
        s2 = "abcdefghijklmnoprstuvwxyz"
        is_title = True
        s0 = self.s.split(" ")
        for i in s0:
            if i[0] in s2:
                is_title = False
                break
            elif i[0] in s1:
                for j in i[1:-1]:
                    if j not in s2:
                        is_title = False
                        break
            elif i[-1] in s1:
                is_title = False
                break
            else:
                is_title = False
                break
        return is_title

    def split(self, separator=None, maxsplit=None):
        if separator == None:
            separator = " "
        elif maxsplit == None:
            maxsplit = len(self.s)
        is_split = 0
        lst = []
        s1 = ""
        for i in range(len(self.s)):
            s1 += self.s[i]
            if self.s[i] == separator:
                is_split += 1
                lst.append(s1)
                s1 = ""
                if is_split == maxsplit:
                    break
            elif i == len(self.s) - 1:
                lst.append(s1)

        return lst

    def partition(self, value):
        s1 = ""
        for i in range(len(self.s)):
            if self.s[i] == value[0]:
                for j in range(i, len(self.s)):
                    s1 += self.s[j]
                    if s1 == value:
                        break
                tpl = (self.s[:i], value, self.s[i + len(value):])
        if value not in self.s:
            tpl = (self.s, "", "")
        return tpl

    def replace(self, oldvalue, newvalue, count=None):
        count1 = 0
        if count == None:
            count = -1
        lst1 = self.s.split()
        for i in range(len(lst1)):
            if oldvalue in lst1[i]:
                if count1 == count:
                    break
                count1 += 1
                lst1[i] = newvalue
        st = ""
        for i in lst1:
            st += " " + i
        return st


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
    print(my_str.islower())
    print(my_str.isnumeric())
    print(my_str.isprintable())
    print(my_str.istitle())
    print(my_str.split(" ",))
    print(my_str.partition("Kmnj"))
    print(my_str.replace("Onbg", "mou", 2))


if __name__ == "__main__":
    main()
