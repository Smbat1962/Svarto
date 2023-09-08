
class store_student_class():
    def __init__(self, id, my_list):
        self.id = id
        self.my_list = my_list

    def add(self):
        my_dict = {}
        my_dict[self.id] = self.my_list
        print(my_dict)
        while True:
            operator = input("what do you do ")
            if operator == "add":
                id = input("id: ")
                my_list = [input("name: "), input("age: "),input("course names: ")]
                my_dict[id] = my_list
                print(my_dict)
            elif operator == "remove":
                id = input("id= ")
                if id in my_dict:
                    del my_dict[id]
                else:
                    print("id = ", id,"not in my_dict")
            elif operator == "update":
                id = input("id: ")
                my_list = [input("name: "), input("age: "),input("course names: ")]
                if id in my_dict:
                    my_dict[id] = my_list
                else:
                    print("id =", id, " not in my_dict")
                print(my_dict)

            else:
                break
        return my_dict
    
p1 = store_student_class(input("id: "), [input("name: "), input("age: "),input("course names: ")])
p1.add()
