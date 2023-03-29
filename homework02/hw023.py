# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
import math
def fun_Combination(n,k):# где n - множество элементов(кнопок), k - неупорядоченный набор элементов множества n 
    return round((math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*(0.5**k)*0.5**(n-k),4)
print(fun_Combination(144,70))