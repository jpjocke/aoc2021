import copy
import threading

from src.day24.alu import ALU
from src.day24.model_no_tester import test_model_no


class ThreadedModelNo(threading.Thread):
    highest = -1

    def __init__(self, alu: ALU, start: int, end: int):
        threading.Thread.__init__(self)
        self.alu = copy.deepcopy(alu)
        self.start_val = start
        self.end = end

    def run(self):
        print('starting ' + str(self.end) + '-' + str(self.start_val))
        highest = test_model_no(self.alu, self.start_val, self.end)
        if highest == -1:
            print('none found between ' + str(self.end) + '-' + str(self.start_val))
        else:
            print(str(highest) + ' found between ' + str(self.end) + '-' + str(self.start_val))

# only uses one thread anyways...
def run_threads(alu: ALU) -> int:
    a = ThreadedModelNo(alu, 99999999999999, 90000000000000)
    b = ThreadedModelNo(alu, 89999999999999, 80000000000000)
    c = ThreadedModelNo(alu, 79999999999999, 70000000000000)
    d = ThreadedModelNo(alu, 69999999999999, 60000000000000)
    e = ThreadedModelNo(alu, 59999999999999, 50000000000000)
    f = ThreadedModelNo(alu, 49999999999999, 40000000000000)
    g = ThreadedModelNo(alu, 39999999999999, 30000000000000)
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()

    threads = [a, b, c, d, e, f, g]

    for t in threads:
        t.join()
    highest = -1
    for t in threads:
        print('thread found: ' + str(t.highest))
        if t.highest > highest:
            highest = t.highest

    print("Exiting Main Thread")
    return highest
