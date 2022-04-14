# sc = "LEFT_BRACE,LEFT_PAREN,RIGHT_PAREN,RIGHT_BRACE,COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,  BANG, BANG_EQUAL, EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL,    LESS, LESS_EQUAL,    IDENTIFIER, STRING, NUMBER, AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NULL, OR, PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE, EOF"

# key = "AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR, PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,"
# f = open("tokentype.py", 'w')

# f.write("import enum\n")
# f.write('\n \n')
# f.write("@enum.unique\n")
# f.write("class TokenType(enum.Enum):\n")
# novalue = sc.replace(' ', "")
# values = novalue.split(",")
# f.write("\n")
# for x in values:
#     f.write('    {} = "{}"\n'.format(x, x))

# f.write("keywords = {\n")
# novalue = key.replace(' ', "")
# values = novalue.split(",")

# print(values)
# for x in values:
#     f.write('"{}":TokenType.{}, \n'.format(x.lower(), x))

# f.write("\n}")

# f = open("Expr.py", "w")

# src = ["Binary:left,operator,right",
#        "Grouping:expression",
#        "Literal:value",
#        "Unary:operator,right"]

# for x in src:
#     nospace = x.replace(" ", "")
#     grps = nospace.split(":")
#     f.write("class {}:\n".format(grps[0]))
#     f.write("   def __init__(self,{}):\n".format(grps[1]))
#     objs = grps[1].split(",")
#     for n in objs:
#         f.write("       self.{}={}\n".format(n, n))
#     f.write("\n")
#     f.write("   def accept(self,visitor):\n")
#     f.write("       return visitor.visit{}()\n\n".format(grps[0]))
