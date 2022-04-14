class Binary:
   def __init__(self,left,operator,right):
       self.left=left
       self.operator=operator
       self.right=right

   def accept(self,visitor):
       return visitor.visitBinary()

class Grouping:
   def __init__(self,expression):
       self.expression=expression

   def accept(self,visitor):
       return visitor.visitGrouping()

class Literal:
   def __init__(self,value):
       self.value=value

   def accept(self,visitor):
       return visitor.visitLiteral()

class Unary:
   def __init__(self,operator,right):
       self.operator=operator
       self.right=right

   def accept(self,visitor):
       return visitor.visitUnary()

