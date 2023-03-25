# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
import math

def fun_Combination(n,k):# где n - множество элементов(карт), k - неупорядоченный набор элементов множества n 
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
N=fun_Combination(52,4)# общее количесвто исходов
print(N)
Ma=fun_Combination(13,4)# количество благопритных исходов в первом случае
print(f"Вероятность того, что все карты – крести = {round(Ma/N*100,3)}%")
Mb=fun_Combination(4,1)*fun_Combination(48,3)+fun_Combination(4,2)*fun_Combination(48,2)+\
    fun_Combination(4,3)*fun_Combination(48,1)+fun_Combination(4,4)*fun_Combination(48,0) #количество благопритных исходов во втором случае
print(f"Вероятность, что среди 4-х карт окажется хотя бы один туз = {round(Mb/N*100,3)}%")