# 1. 완전수 구하기
def findPerfect():
    perfectNum = []
    for number in range(1, 10000):
        sum = 0
        for div in range(1, number):
            if number % div == 0:
                sum += div
        if number == sum:
            perfectNum.append(number)
    return perfectNum
# print(findPerfect())


# 2. 피보나치 수열 구하기
def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# 3. 자연수 합 경우의 수 구하기
def countWay(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return countWay(n - 1) + countWay(n - 2) + countWay(n - 3)
