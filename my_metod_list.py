class My_List:
    def __init__(self, s):
        self.s = s

    def append(self, elmnt):
        s1 = []
        s1 = self.s + [elmnt]
        return s1

    def clear(self):
        s1 = self.s
        s1 = []
        return s1

    def copy(self):
        s1 = []
        for i in self.s:
            s1 += [i]
        return s1

    def count(self, value):
        counter = 0
        for i in self.s:
            if value in [i]:
                counter += 1
        return counter

    def extend(self, iterable):
        s1 = []
        s1 += self.s
        for i in iterable:
            s1 += [i]
        return s1

    def index(self, elmnt):
        for i in range(len(self.s)):
            if self.s[i] == elmnt:
                return i

    def insert(self, pos, elmnt):
        s1 = []
        for i in range(len(self.s)):
            s1 += [self.s[i]]
            if i == pos:
                s1[i] = elmnt
        return s1

    def pop(self, pos):
        s1 = []
        for i in range(len(self.s)):
            if i == pos:
                for j in range(len(self.s)):
                    if j != i:
                        s1 += [self.s[j]]
        return s1

    def remove(self, elmnt):
        s1 = []
        for i in range(len(self.s)):
            if self.s[i] == elmnt:
                for j in range(len(self.s)):
                    if j != i:
                        s1 += [self.s[j]]
                return s1
            
    def reverse(self):
        s1 = []
        for i in range(len(self.s)):
            s1 += [self.s[len(self.s) -1 - i]]
        return s1


def main():
    my_list = My_List(["mkj", 45, "14l", 45, "tg5k", "14l"])
    print(my_list.append(["j", 21, "mnj", 45]))
    print(my_list.clear())
    print(my_list.copy())
    print(my_list.count(45))
    print(my_list.extend(["jk", 125, "cdsx4"]))
    print(my_list.index("tg5k"))
    print(my_list.insert(3, "okol"))
    print(my_list.pop(4))
    print(my_list.remove("14l"))
    print(my_list.reverse())


if __name__ == "__main__":
    main()
