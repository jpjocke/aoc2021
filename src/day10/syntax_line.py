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

    def __str__(self):
        sb = 'ok: '
        if not self.ok:
            sb = 'Corrupt: ' + self.errorChar + ' - '
        return sb + self.line
