#Method 1:
# def main():
#     counter = 0
#     sum = 0

#     while True:
#         number = input("Input a value:")
#         counter += 1
#         if(number == "Done"):
#             print("All done")
#             break
#         sum += float(number)
#         average = sum/counter

#         print("Average so far:",average)

#Method 2:
def main():
    counter = 0
    average = 0.0
    value = input("Input a value:")

    while(value != "done"):
        temp = average * counter + float(value)
        counter += 1
        average = temp/counter
        print("Average so far:",average)

        value = input("Input a value:")

main()


