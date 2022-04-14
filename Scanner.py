from ast import Continue
from Token import Token
from TokenType import TokenType


class Scanner:
    start = 0
    current = 0
    line = 1
    tokens = []
    source = ""

    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "fun": TokenType.FUN,
        "for": TokenType.FOR,
        "if": TokenType.IF,
        "null": TokenType.NULL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE,
    }

    def __init__(self, source):
        self.source = source

    def isAtEnd(self):
        return self.current >= len(self.source)

    def scanTokens(self):
        while(not self.isAtEnd()):
            self.start = self.current
            self.scanToken()

        self.tokens.append(Token(TokenType.EOF, None, None, self.line+1))
        return self.tokens

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

    def isDigit(self, c):
        if (c >= '0' and c <= '9'):
            return True
        else:
            return False

    def isAplha(self, c):
        val = (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'
        return val

    def scanToken(self):
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
            if(self.match('/')):
                print(self.peek() != '\n')
                print(self.isAtEnd())
                while (self.peek() != '\n' and self.isAtEnd()):
                    self.advance()
            else:
                self.addToken(TokenType.SLASH, None)

        elif c == "<":
            if(self.match("=")):
                self.addToken(TokenType.GREATER_EQUAL, None)
            else:
                self.addToken(TokenType.GREATER, None)

        elif c == ">":
            if self.match("="):
                self.addToken(TokenType.LESS_EQUAL, None)
            else:
                self.addToken(TokenType.LESS, None)

        elif c == (' ' or '\t' or '\r'):
            # Do nothing
            Continue
        elif c == '\n':
            self.line += 1

        elif c == '"':
            self.string()

        else:
            if(self.isDigit(c)):
                self.number()
            elif(self.isAplha(c)):
                self.identifier()
            else:
                print("Error {}".format(self.source[0:self.current]))

    def peekNext(self):
        if (self.isAtEnd()):
            return '/0'
        return self.source[self.current+1]

    def number(self):
        while(self.isDigit(self.peek())):
            self.advance()
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            while(self.isDigit(self.peek())):
                self.advance()
        self.addToken(TokenType.NUMBER, float(
            self.source[self.start:self.current]))

    def isAphaNumeric(self, c):
        return self.isDigit(c) or self.isAplha(c)

    def identifier(self):
        while(self.isAphaNumeric(self.peek())):
            self.advance()

        text = self.source[self.start:self.current]
        type = self.keywords.get(text)

        if type == None:
            type = TokenType.IDENTIFIER

        self.addToken(type, None)

    def string(self):
        while(self.peek() != '"' and (not self.isAtEnd())):
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        value = self.source[self.start + 1: self.current]
        self.advance()
        self.addToken(TokenType.STRING, value)

    def addToken(self, type, literal):
        text = self.source[(self.start):(self.current)]
        self.tokens.append(Token(type, text, literal, self.line))
