from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]


class Bridge:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
        self.trucks = deque()
        self.gone = deque()
        self.current = 0
#
    def get_current(self):
        self.current = 0
        for a in self.trucks:
            self.current += a[0]

    def on_trucks(self, queue):
        self.get_current()
        #print(f'current : {self.current} / queue[0][0] : {queue[0][0]}')
        print(f'in queue.. {queue}')
        if len(queue) != 0:
            if (self.current + queue[0][0]) <= self.weight:
                print('act')
                self.trucks.append(queue.popleft())
            else:
                pass
        else:
            pass

    def plus_time(self):
        for a in self.trucks:
            a[1] += 1

    def pass_truck(self):
        print(f'trucks : {self.trucks}')
        print(f'gone   : {self.gone}')
        print(f'trucks : {len(self.trucks)}')
        print(self.check_no_trucks())
        if self.check_no_trucks():
            if self.trucks[0][1] == self.length:
                self.gone.append(self.trucks.popleft())
            else:
                pass
        else:
            pass

    def check_no_trucks(self):
        if len(self.trucks) > 0:
            return True
        else:
            return False


def check_no_trucks(queue):
    if len(queue) > 0:
        return True
    else:
        return False


def solution(bridge_length, weight, truck_weights):
    truck_queue = deque()
    for a in truck_weights:
        truck_queue.append([a, 0])

    bridge = Bridge(bridge_length, weight)
    timer = 0

    try:
        while (bridge.check_no_trucks() or check_no_trucks(truck_queue)):
            print(f'\n\ntimer : {timer}')
            print(f'bridge : {bridge.check_no_trucks()} / trucks : {check_no_trucks(truck_queue)}')
            print(f'bridge : {len(bridge.trucks)} / trucks : {len(truck_queue)}')
            bridge.plus_time()
            bridge.pass_truck()
            bridge.on_trucks(truck_queue)
            timer += 1

    finally:
        answer = timer

    print(answer)
    return answer


print(solution(bridge_length, weight, truck_weights))
