#A fever diagnosis system

#Qusestion "Do you have aching bones or aching joints?" and the following questions
def achingques():
    if(input("Do you have aching bones or aching joints?\n") == "yes"):
        print("Possibilities include viral infection.")
    elif(input("Do you have a rash?\n") == "yes"):
        print("Insufficient information to list possibilities.")
    elif(input("Do you have a score throat?\n") == "yes"):
        print("Possibilities include a throat infection.")
    elif(input("Do you have back pain just above the waist with chills and fever?\n") == "yes"):
        print("Possibilities include kidney infection.")
    elif(input("Do you have pain urinating or are urinating more often?\n") == "yes"):
        print("Possibilities include a urinary tract infection.")
    elif(input("Have you spent the day in the sunr in hot conditions?\n") == "yes"):
        print("Possibilities sunstroke or heat exhaustion.")
    else:
        print("Insufficient information to list possibilities.")

#Question "Are you vomiting or had diarrhea?" and the following questions
def diarrheaques():
    if(input("Are you vomiting or had diarrhea?\n") == "yes"):
        print("Possibilities include digestive tract infection.")
    else:
        achingques()


def main():
    if(input("Are you coughing?\n") == "yes"):
        if(input("Are you short of breath or wheezing or coughing up phlegm?\n") == 'yes'):
            print("Possibilities include pneumonia or infection of airways.")
        elif(input("Do you have a headache?\n") == "yes"):
            print("Possibilities include viral infection.")
        else:
            achingques()
    elif(input("Do you have a headche?\n") == "yes"):
        if(input("Are experiencing any of the following: " 
                 "pain when bending your head forward, " 
                 "nausea or vomiting, bright light hurting your eyes, " 
                 "drowinessor confusion?\n") == "yes"):
            print("Possibilities include menigitis.")
        else:
            diarrheaques()
    else:
        achingques()
    
main()