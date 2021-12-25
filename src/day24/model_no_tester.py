from src.day24.alu import ALU


def test_model_no(alu: ALU, start: int, end: int) -> int:
    value = start
    while True:
        alu.reset()
        inp = []
        valid = True
        for i in str(value):
            val = int(i)
            if val == 0:
                valid = False
            inp.append(val)
        value -= 1
        if not valid:
            continue
        if value < end:
            return -1
        alu.add_input_list(inp)
        if value % 59999 == 1:
            print('testing: ' + str(value))
        try:
            alu.run()
            if alu.z == 0:
                return value
        except Exception as err:
            print(err)
    return 0
