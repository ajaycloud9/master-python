

class Student:

    def __init__(self) -> None:
        print("Starting student class")
    
    # def print_name(self,name):
    #     print(name)
    
    # def print_name(self, xyz):
    #     print(xyz)

    def print_name(self, *args):
        print(args)

    def print_name(self, *args, **kwargs):
        print(args,kwargs)

        for i in args:
            print (i)
        for k,v in kwargs.items():
            print(k,v)

new_stud = Student()

# new_stud.print_name(1, "name", 2)
new_stud.print_name(1,2,3,name="test")