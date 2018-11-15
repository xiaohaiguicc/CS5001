from id import Idnumber


def main():
    num = input("Please enter an account number:\n")
    id_number = Idnumber(num)
    id_number.judge()


main()
