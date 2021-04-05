"""
프로그래머스의 문제를 해결하는 폴더입니다

Stack/Queue Section

주식문제

문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

"""
prices = [1,2,3,2,3]

def check_up_down(stock):
    sec_list = []
    length = len(stock)
    for i in range(length):
        sec = 0
        for j in range(i, length):
            print(f'j({j}) - i({i}) :: {stock[j]} - {stock[i]} = {stock[j]-stock[i]}')
            print(f'sec is {sec}')
            print(j == (length-1))

            if (stock[j] - stock[i]) >= 0 and j != (length-1):
                sec += 1
                print('add sec')

            elif sec == -1 and ((stock[j] - stock[i]) < 0):
                print(sec == -1 and ((stock[j] - stock[i]) < 0))
                sec_list.append(0)
                print('add 0')
                break

            elif j == (length-1) or (stock[j] - stock[i]) < 0:
                sec_list.append(sec)
                print(f'add sec :: {sec}\n')
                break

            elif j == (length-1):
                sec_list.append(0)
                print('add 0')
                break

            else:
                print('do nothing')
                pass
        print('\n')

    return sec_list


def solution(prices):
    answer = check_up_down(prices)
    print(answer)
    return answer

solution(prices)


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer