# def factorial(number):
#     fact = 1
#     if number == 0 or number==1: 
#         return 1    
#     else:
#         for i in range(2,number):
#             fact*=i   

import math

if __name__ == "__main__":
    num = int(input())
    print(math.factorial(num))