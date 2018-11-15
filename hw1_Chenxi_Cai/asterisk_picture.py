# print('\t\t\t\t\t*\t\t\t\t\t\n\t\t\t\t*\t\t*\t\t\t\t\n\t\t\t*\t\t\t\t*\t\t\t\n\t\t*\t\t\t\t\t\t*\t\t\n\t*\t*\t*\t*\t*\t*\t*\t*\t*\t\n')
#a is the number of leaf lines, b is the number of trunk lines
a = 8
b = 10
#s is the leaf lines, s1 is the trunk lines 
s_a = ''
s_b = ''
#Build leaf top line
for i in range(a):
    s_a += '\t'
s_a += '*\n'
#Build leaf middle line
for i in range(a-1):
    for j in range(a-1-i):
        s_a += '\t'
    s_a += '*'
    for k in range(2*(i+1)):
        s_a +='\t'
    s_a += '*\n'
#Build leaf bottom line
for i in range(2*a +1):
    s_a += '\t*'
print(s_a)

#Build middle trunk lines
for i in range(b-1):
    for j in range(a-1):
        s_b += '\t'
    s_b += '*\t\t*\n'
#Build bottom trunk lines
for i in range(a-1):
    s_b += '\t'
s_b += '*\t*\t*'
print(s_b)
