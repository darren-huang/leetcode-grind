""""2:11pm - 2:50pm"""
import heapq
import math


class Elevators:
    def __init__(self, num_els: int, default_floor: int = 0) -> None:
        self.els = [default_floor] * num_els
        self.els_floors_left = [set() for _ in range(num_els)]
        self.els_next_floors = [[] for _ in range(num_els)]
        self.els_dir = [0] * num_els
        self.waiting_q = set()  # if all els are busy, add floor here

    def _get_direction(self, curr_floor: int, next_floor: int) -> int:
        """return 1 or -1 depending on direction"""
        if curr_floor == next_floor:
            return 0
        return math.floor((next_floor - curr_floor) / abs(next_floor - curr_floor))

    def _add_floor(self, elv_i: int, floor_num: int) -> None:
        # check if floor_num has already been q'ed or not
        dir = self._get_direction(self.els[elv_i], floor_num)
        if floor_num not in self.els_floors_left[elv_i]:
            self.els_floors_left[elv_i].add(floor_num)
            heapq.heappush(self.els_next_floors[elv_i], floor_num * dir)
            self.els_dir[elv_i] = dir

    def button_press(self, floor_num: int) -> None:
        print(f"button at floor {floor_num} is pressed\n")
        assert floor_num >= 0
        for i in range(len(self.els)):
            # check if elevator is free OR going in the same direction
            dir = self._get_direction(self.els[i], floor_num)
            if self.els_dir[i] == 0 or dir == self.els_dir[i]:
                self._add_floor(i, floor_num)
                break
        else:
            self.waiting_q.add(floor_num)

    # takes (N log M) time (N elevators, M floors to keep track of)
    # runs through N elevators
    # for each might need to update heap of floors to travel to
    #    resulting in (log M) runtime to update heap of floors
    def step(self) -> None:
        print("step:")
        for i in range((len(self.els))):
            if not self.els_next_floors[i]:
                continue
            if self.els_next_floors[i][0] == self.els[i]:
                print(f"elevator_{i} opens door at floor {self.els[i]}")
                self.els_floors_left[i].remove(self.els[i])
                heapq.heappop(self.els_next_floors[i])
                if not self.els_floors_left[i]:
                    # if no more floors to go to, set dir to 0
                    self.els_dir[i] = 0
                    if self.waiting_q:
                        for floor in self.waiting_q:
                            self._add_floor(i, floor)
                        self.waiting_q = set()
            else:
                prev = self.els[i]
                self.els[i] += self.els_dir[i]
                print(f"elevator_{i} moves from {prev}->{self.els[i]}")
        print("")


if __name__ == "__main__":
    els = Elevators(2)
    els.button_press(2)
    els.button_press(4)
    els.button_press(7)
    for _ in range(5):
        els.step()
    els.button_press(3)
    els.step()
    els.button_press(0)
    for _ in range(15):
        els.step()
