# credit=int(input("enter your grade "))
# if credit in range (40,60):
#     print("your grade is c")
# elif 60<=credit and 70>=credit:
#     print("grade is b")
#
# else: print("your grade is a")
#
marks=int(input("enter your marks: "))
uni_exam=input("you failed or pass")
if uni_exam == "pass":
    print("you enter university")
    if marks>980:
        print("you are eligible for soe")
    else :
        print("eligible for sos")
