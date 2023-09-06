def remove_student(id, my_dict):
    if id in my_dict:
        my_dict.pop(id)
    else:
        print("id =", id, " not in my_dict")
    print(my_dict)


def add_student(id, my_dict, my_list):
    my_dict[id] = my_list
    print(my_dict)


def update_student(id, my_dict, my_list):
    if id in my_dict:
        my_dict[id] = my_list
    else:
        print("id =", id, " not in my_dict")
    print(my_dict)


def display_student(id, my_dict):
    if id in my_dict:
        print(my_dict[id])
    else:
        print("id =", id, " not in my_dict")
        print(my_dict)


def finding_student(curs_name, my_dict):
    for i in my_dict.values():
        j = str(i)
        if curs_name in j:
            print("name student is enrolled this course ", i[0])


def old_young_student(my_dict):
    lst = []
    for i in my_dict.values():
        lst.append(i[1])
    lst1 = sorted(lst)
    print("youngest student age =", lst1[0])
    print("oldest student age =", lst1[-1])


def sort_name_student(my_dict):
    lst = []
    for i in my_dict.values():
        lst.append(i[0])
    lst1 = sorted(lst)
    for i in lst1:
        for k in my_dict.values():
            j = str(k)
            if i in j:
                print(str(k))


def convert_record_student(id, my_dict):
    if id in my_dict:
        lst = [id]
        lst.extend(my_dict[id])
        tpl = tuple(lst)
        print(tpl)
    else:
        print("id =", id, " not in my_dict")
        print(my_dict)


def main():
    my_dict = {}
    while True:
        operator = input("What do you want to do ")
        if operator == "add":
            id = input("id: ")
            my_list = [input("name: "), input("age: "),
                       input("course names: ")]
            add_student(id, my_dict, my_list)
        elif operator == "remove":
            id = input("id: ")
            remove_student(id, my_dict)
        elif operator == "update":
            id = input("id: ")
            my_list = [input("name: "), input("age: "),
                       input("course names: ")]
            update_student(id, my_dict, my_list)
        elif operator == "display":
            id = input("id: ")
            display_student(id, my_dict)
        elif operator == "finding":
            curs_name = input("cours names ")
            finding_student(curs_name, my_dict)
        elif operator == "old_young":
            old_young_student(my_dict)
        elif operator == "sort_name":
            sort_name_student(my_dict)
        elif operator == "convert_record":
            id = input("id: ")
            convert_record_student(id, my_dict)
        else:
            break


if __name__ == "__main__":
    main()
