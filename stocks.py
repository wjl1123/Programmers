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

from collections import deque

prices = [1,2,3,2,3]

def check_up_down(deque):
    sec_list = []

    for i in deque:
        sec = -1
        for j in deque:
            print(j - i)
            if ((j - i) >= 0):
                print('act')
                sec += 1
            elif sec == -1 and ((j - i) < 0):
                sec_list.append(0)
                break
            else:
                sec_list.append(sec)
                break

    return sec_list


def solution(prices):
    prices = deque(prices)

    answer = check_up_down(prices)
    print(prices)
    return answer