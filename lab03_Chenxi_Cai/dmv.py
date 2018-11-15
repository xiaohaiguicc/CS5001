import random as rnd
def main():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    funame = input("Please enter your first, middle, and last name:\n")
    dob = input("Enter date of birth (MM/DD/YY):\n")
    
    # lname = "".join(funame.split()[-1:])
    # fname = funame[0:len(funame)-len(lname)]
    lname_index = funame.rfind(" ")
    lname = funame[lname_index + 1:]
    fname = funame[:lname_index]
    n = 7
    dl = "".join("%s" % rnd.randint(0,9) for num in range(0,n))
    exp = dob[:6] + "21"
    
    print("-------------------------------------")
    print("Washington Driver License")
    print("DL", dl)
    print("LN", lname)
    print("FN", fname)
    print("DOB", dob)
    print("EXP", exp)
    print("-------------------------------------")

main()