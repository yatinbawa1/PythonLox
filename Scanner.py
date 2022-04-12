from ast import Continue
from Token import Token
from TokenType import TokenType


class Scanner:
    start = 0
    current = 0
    line = 0
    tokens = []
    source = ""

    def __init__(self):
        self.source = '**'

    def isAtEnd(self):
        return self.current >= len(self.source)

    def scanTokens(self):
        print(self.source)
        while(not self.isAtEnd()):
            self.start = self.current
            self.scanToken()

        print("{} is of {} type".format(
            self.tokens[0].literal, self.tokens[0].type))

    def advance(self):
        c = self.source[self.current]
        self.current = self.current + 1
        return c

    def match(self, expected):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False
        self.current = self.current + 1
        return True

    def peek(self):
        if (self.isAtEnd()):
            return '/0'
        return self.source[self.current]

    def scanToken(self):
        print("Scanning")
        c = self.advance()
        if c == '(':
            self.addToken(TokenType.LEFT_PAREN, None)
        elif c == ")":
            self.addToken(TokenType.RIGHT_PAREN, None)
        elif c == "{":
            self.addToken(TokenType.LEFT_BRACE, None)
        elif c == "}":
            self.addToken(TokenType.RIGHT_BRACE, None)
        elif c == ",":
            self.addToken(TokenType.COMMA, None)
        elif c == ".":
            self.addToken(TokenType.DOT, None)
        elif c == "+":
            self.addToken(TokenType.PLUS, None)
        elif c == "-":
            self.addToken(TokenType.MINUS, None)
        elif c == ";":
            self.addToken(TokenType.SEMICOLON, None)
        elif c == "*":
            self.addToken(TokenType.STAR, None)
        elif c == "/":
            # self.addToken(TokenType.TokenType.RIGHT_BRACE,None)
            if(self.match('/')):
                while (self.peek() != '\n' and self.isAtEnd()):
                    self.advance()
            else:
                self.addToken(TokenType.SLASH, None)
        elif c == (' ' or '\t' or '\r'):
            # Do nothing
            Continue
        elif c == '\n':
            line = line + 1
        elif c == '"':
            self.string()

    def string(self):
        while(self.peek() != '"' and not self.isAtEnd):
            if self.peek() == '\n':
                line = line + 1
            self.advance()
        value = self.source[self.start + 1: self.current - 1]
        self.addToken(TokenType.STRING, value)

    def addToken(self, type, literal):
        print("{} found at {}".format(type, self.source[self.current - 1]))
        text = self.source[(self.start):(self.current)]
        self.tokens.append(Token(type, text, literal, self.line))


a = Scanner()
a.scanTokens()
