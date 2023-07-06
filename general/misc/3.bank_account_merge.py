"""base bank trading system, 
1.has a get amount of money function GET
has a deposit function DEPOSIT
has a transfer function TRANSFER
has a create account function CREATE

2. schedule transfers
SCHEDULE ts uuid1 uuid2 amt when_to_transfer
should happen first

3. merge accounts
MERGE_ACCOUNTS ts uuid1 uuid2
1:56pm - took 40 minutes so far

4. support a price at timestamp function
"""
from typing import List, Callable
from collections import defaultdict
import heapq


class BankAccounts:
    def __init__(self) -> None:
        self.accts = defaultdict(int)

        # minheap of (time_to_transfer, time_scheduled, uuid1, uuid2, amt)
        self.transfers_heap = []

    def _error(self, ts) -> None:
        print(f"{ts}: ERROR")

    def _done(self, ts) -> None:
        print(f"{ts}: DONE")

    def _check_schedule(self, ts: int) -> None:
        if not self.transfers_heap:
            return

        transfer_time, _, uuid1, uuid2, amt = self.transfers_heap[0]
        if transfer_time <= ts:
            heapq.heappop(self.transfers_heap)
            self.transfer(transfer_time, uuid1, uuid2, amt)

    def get(self, ts: int, uuid: str) -> None:
        self._check_schedule(ts)
        if uuid not in self.accts:
            self._error(ts)
        else:
            print(f"{ts}: {self.accts[uuid]}")

    def deposit(self, ts: int, uuid: str, amt: int) -> None:
        self._check_schedule(ts)
        if uuid in self.accts:
            self.accts[uuid] += amt
            self._done(ts)
        else:
            self._error(ts)

    def transfer(self, ts: int, uuid1: str, uuid2: str, amt: int) -> None:
        self._check_schedule(ts)
        if (
            uuid1 == uuid2
            or uuid1 not in self.accts
            or uuid2 not in self.accts
            or self.accts[uuid1] < amt
        ):
            self._error(ts)
        else:
            self.accts[uuid1] -= amt
            self.accts[uuid2] += amt
            self._done(ts)

    def create(self, ts: int, uuid: str) -> None:
        self._check_schedule(ts)
        if uuid not in self.accts:
            self.accts[uuid] = 0
            print(f"{ts}: {uuid} account created")
        else:
            self._error(ts)

    def schedule(
        self, ts: int, uuid1: str, uuid2: str, amt: int, transfer_time: int
    ) -> None:
        self._check_schedule(ts)
        if uuid1 not in self.accts or uuid2 not in self.accts:
            self._error(ts)
        else:
            heapq.heappush(
                self.transfers_heap,
                (transfer_time, ts, uuid1, uuid2, amt),
            )
            self._done(ts)

    def merge(self, ts: int, uuid1: str, uuid2: str) -> None:
        self._check_schedule(ts)


def type_cast(func: Callable, types: List[type]):
    def caster(*args):
        return func(*[t(arg) for t, arg in zip(types, args)])

    return caster


def process_text(text: str):
    ba = BankAccounts()
    func_maps = {
        "GET": type_cast(ba.get, [int, str]),
        "DEPOSIT": type_cast(ba.deposit, [int, str, int]),
        "TRANSFER": type_cast(ba.transfer, [int, str, str, int]),
        "CREATE": type_cast(ba.create, [int, str]),
        "SCHEDULE": type_cast(ba.schedule, [int, str, str, int, int]),
        "MERGE": type_cast(ba.merge, [int, str, str]),
    }
    for line in test1.split("\n"):
        if line.strip():
            line_components = line.strip().split()
            cmd, args = line_components[0], line_components[1:]
            func_maps[cmd](*args)


test1 = """
CREATE 0 user_1
GET 1 user_1
GET 2 user_2
SCHEDULE 2 user_1 user_2 5 8
CREATE 3 user_2
SCHEDULE 2 user_1 user_2 5 7
SCHEDULE 2 user_1 user_2 1 8
TRANSFER 4 user_1 user_2 50
DEPOSIT 5 user_1 55
GET 6 user_1
GET 7 user_2
TRANSFER 8 user_1 user_2 50
TRANSFER 9 user_1 user_2 49
GET 10 user_1
GET 11 user_2
"""

if __name__ == "__main__":
    print(test1, "\n\n")
    process_text(test1)
