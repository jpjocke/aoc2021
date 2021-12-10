class SyntaxLine:
    line: str
    completed: str
    ok: bool
    errorChar: str

    def __init__(self, line: str):
        self.line = line
        self.ok = True
        self.errorChar = ''
        self.completed = ''

    def get_error_point(self) -> int:
        if self.ok:
            return 0
        if self.errorChar == ')':
            return 3
        if self.errorChar == ']':
            return 57
        if self.errorChar == '}':
            return 1197
        if self.errorChar == '>':
            return 25137

    def get_complete_point(self) -> int:
        if not self.ok:
            return 0
        total = 0
        for c in self.completed:
            total *= 5
            if c == ')':
                total += 1
            if c == ']':
                total += 2
            if c == '}':
                total += 3
            if c == '>':
                total += 4
        return total

    def __str__(self):
        sb = 'ok: '
        if not self.ok:
            sb = 'Corrupt: ' + self.errorChar + ' - '
        return sb + self.line + '--[ ' + self.completed + ' ]--'
