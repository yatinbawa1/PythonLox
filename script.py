sc = "LEFT_BRACE,LEFT_PAREN,RIGHT_PAREN,RIGHT_BRACE,COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,  BANG, BANG_EQUAL, EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL,    LESS, LESS_EQUAL,    IDENTIFIER, STRING, NUMBER, AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NULL, OR, PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE, EOF"

f = open("TokenType.py", 'w')
f.write("import enum\n")
f.write('\n \n')
f.write("@enum.unique\n")
f.write("class TokenType(enum.Enum):\n")
novalue = sc.replace(' ', "")
values = novalue.split(",")
f.write("\n")
for x in values:
    f.write('    {} = "{}"\n'.format(x, x))
