# The difference between the highest and the lowest temperature values 
# predicted for the 10 day forecast.
def diff():
    high = float(input('The highest temperature values predicted for the 10 day forecast: '))
    low = float(input('The lowest temperature values predicted for the 10 day forecast: '))
    diff = high - low
    print('The difference is:', diff)

# The average temperature at noon predicted for the 10 day forecast.
def average():
    tem_sum = 0
    for i in range(10):
        tem = float(input('The temperature at noon for day {:d}: '.format(i+1)))
        tem_sum += tem
    tem_ave = tem_sum/10
    print('The average temperature at noon predicted for the 10 day forecas is:', tem_ave)   

# The highest temperature predicted for the 10 day forecast, converted from Celsius to Fahrenheit.
def convert():
    tem_cel = float(input('The highest temperature in Celsius: '))
    tem_fah = tem_cel * 1.8 + 32
    print('The highest temperature in Fahrenheit:', tem_fah)

diff()
average()
convert()