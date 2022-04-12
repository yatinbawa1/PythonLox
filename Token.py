class Token:

    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def type(self):
        return self.type

    def lexeme(self):
        return self.lexeme

    def literal(self):
        return self.literal

    def line(self):
        return self.line
