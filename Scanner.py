import Token
import TokenType
import enum


class Scanner:
    start = 0
    current = 0
    line = 0
    tokens = []
    source = ""

    def __init__(self):
        self.source = "(((("

    def isAtEnd(self):
        return self.current >= len(self.source)

    def scanTokens(self):
        while(not self.isAtEnd()):
            self.start = self.current
            self.scanToken()

        print(self.tokens)

    def advance(self):
        c = self.source[self.current]
        self.current = self.current + 1
        return c

    def scanToken(self):
        print("Scanning")
        c = self.advance()
        if c == "(":
            self.addToken(TokenType.TokenType.LEFT_PAREN, None)

    def addToken(self, type, literal):
        print(self.start)
        text = self.source[(self.start):(self.current)]
        self.tokens.append(Token.Token(type, text, literal, self.line))


a = Scanner()
a.scanTokens()
