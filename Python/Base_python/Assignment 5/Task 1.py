stu_dict={'Josh':59,'Alice':67}
name=input("Enter your name: ")
if name in stu_dict:
    print("Your marks are:",stu_dict[name])
else:
    print("Student not found")