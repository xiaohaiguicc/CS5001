
# def pseudorandom(p, d, x_0, n):
#     num_list = [x_0]
#     for i in range(n):
#         num_list.append(num_list[i] ** d % p)
#     del num_list[0]

#     return num_list

# def usps(num):
#     num = str(num)
#     sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
#     if int(num[4]) == sum % 5 :
#         return True
#     else:
#         return False

# def cipher(text, K):
#     sentence ="abcdefghijklmnopqrstuvwxyz"
#     new_sen = ""
#     for item in text:
#         new_index = sentence.index(item) - K
#         new_sen += sentence[new_index % 26]
#     return new_sen

# def refexive(matrix):
#     for i in range(len(matrix)):
#         if matrix[i][i] != 1:
#             print("This relation is not reflexive.")
#             return
#     else:
#         print("This relation is reflexive.")

# def symmetric(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] != matrix[j][i]:
#                 print("This relation is not symmetric.")
#                 return
#     else:
#         print("This relation is symmetric.")

# def main():
# #     num_list = pseudorandom(11, 3, 2, 5)
# #     print(num_list)

# #     flag = usps(53194)
# #     print(flag)
#     # sen = "ycvejqwvhqtdtwvwu"
#     # for i in range(26):
#     #     print(cipher(sen, i))

#     matrix_1 = [[1,0,0],[0,1,0],[0,0,1]]
#     matrix_2 = [[1,1,0],[1,1,0],[1,0,1]]
#     matrix_3 = [[0,1,0],[1,0,0],[0,0,1]]
#     symmetric(matrix_1)
#     symmetric(matrix_2)
#     symmetric(matrix_3)

def main():
    myLinkedList = [1, 2, 3, 4, 5]
    myLinkedList.remove(4)
    print(myLinkedList)
    myLinkedList.insert(3, 55)
    myLinkedList.reverse()
    print(myLinkedList.__len__())
    mystack = []
    print(mystack.pop())
main()
