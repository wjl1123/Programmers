"""
문제 설명
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다.
그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
    J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고
중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다.
위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를
알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가
몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며
대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.


입출력 예
priorities	   location	  return
[2, 1, 3, 2]	    2	  1
[1, 1, 9, 1, 1, 1]	0	  5
입출력 예 설명
예제 #1

문제에 나온 예와 같습니다.

예제 #2

6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.


"""

priorities = [2, 1, 3, 2, 2]
location = 4

priorities3 = [3, 1, 2, 1]
location3 = 1

priorities2 = [1, 1, 9, 1, 2, 1, 2, 1, 2, 1]
location2 = 0

#max 뒤로는 내림
#max 앞으로는 오름
from collections import deque

def solution(priorities, location):
    printed = [0]*len(priorities)
    idx = 0
    num = 1

    while num != len(priorities)+1:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            # 뒤에 넣는다 (우선순위 밀림)
        else:
            printed[idx%len(printed)] = num
            print(f' idx : {idx}  len(printed) : {len(printed)}')
            print(f' idx%len : {idx%len(printed)}  num : {num}')
            print(priorities)
            print(printed)
            print('')
            num += 1
            priorities.append(0)

        del priorities[0]
        idx += 1

    return printed[location]
# 우선순위대로 넣기
# 우선순위 같은게 겹치면 전에 넣은 index + 1 부터 시작
# 뺀 원소 다음 index 원소 넣기

print(solution(priorities2, location2))



def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer