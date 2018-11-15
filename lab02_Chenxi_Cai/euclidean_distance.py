import math
# Input four numerical values representing two 2-dimensional points (so, x1, y1, x2, and y2) 
# then calculates the Euclidean distance between the two points
def main():
    x1 = float(input('Enter the horizontal ordinate as x1 in (x1, y1) of the first point: '))
    y1 = float(input('Enter the vertical ordinate as y1 in (x1, y1) of the first point: '))
    x2 = float(input('Enter the horizontal ordinate as x2 in (x2,y2) of the second point: '))
    y2 = float(input('Enter the vertical ordinate as y2 in (x2,y2) of the second point: '))

    euc_dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print('The Euclidean distance between two points is:', euc_dis)


main()