class PolymerInstruction:
    formula: str
    result: str

    def __init__(self, formula: str, result: str):
        self.formula = formula
        self.result = result

    def __str__(self):
        return self.formula + ' -> ' + self.result
