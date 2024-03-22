wiersze=open('liczby_przyklad.txt','r')
tab=[]
for line in wiersze:
    tab.append(int(line.strip()))
# ZAD 3.2
# licznik=0
# def czy_pierwsza(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     pierw = int(n**0.5) + 1
#     for dzielnik in range(3, pierw, 2):
#         if n % dzielnik == 0:
#             return False
#     return True
#
# for i in tab:
#     if czy_pierwsza(i-1):
#         licznik+=1
# print(licznik)



# ZAD 3.3
from math import sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    range_limit = int(sqrt(n)) + 1

    for i in range(2, range_limit):
        if n % i == 0:
            return False
    return True


def goldbach(n: int) -> list[[int, int]]:
    results = []
    for i in range(2, n // 2 + 1):
        difference = n - i
        if is_prime(i) and is_prime(difference):
            results.append([i, difference])

    return results


with open("dane/liczby.txt", "r") as file:
    nums = [int(n) for n in file.readlines()]

unique_nums = set(nums)
even_nums = filter(lambda x: x % 2 == 0, unique_nums)

goldbach_results = map(
    lambda num: {"number": num, "total_sums": len(goldbach(num))}, even_nums)

sorted_goldbach_results = sorted(
    goldbach_results, key=lambda res: res['total_sums'])

print(f"lower goldbach result: {sorted_goldbach_results[0]}")
print(f"higher goldbach result: {sorted_goldbach_results[-1]}")




# ZAD3.4
# tabb=[]
# for i in tab:
#     tabb.append(hex(i))
#
# print(tabb)
#
# slownik = {}
# for i in range(0, len(tabb)):
#     for j in range(2, len(tabb[i])):
#         if tabb[i][j] in slownik:
#             slownik[tabb[i][j]] += 1
#         else:
#             slownik[tabb[i][j]] = 1
#
# print(slownik)