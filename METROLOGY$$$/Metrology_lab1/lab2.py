import clang.cindex
import os

class MyRecursiveASTVisitor(clang.cindex.TranslationUnit):

    operators_count = 0
    branches_count = 0
    max_depth = 0
    sourcepathlist = []
    depthes = {}
    operators = set()

    def __init__(self, translation_unit):
        super(MyRecursiveASTVisitor, self).__init__()
        self.translation_unit = translation_unit

    def TraverseDecl(self, node):
        if self.is_decl_in_source(node):
            super(MyRecursiveASTVisitor, self).TraverseDecl(node)
        return True

    def VisitVarDecl(self, node):
        if node.has_init:
            self.operators.add((node.extent.start.offset, node.extent.end.offset))
            MyRecursiveASTVisitor.operators_count = len(self.operators)
        return True

    def VisitCallExpr(self, node):
        self.operators.add((node.extent.start.offset, node.extent.end.offset))
        MyRecursiveASTVisitor.operators_count = len(self.operators)
        return True

    def VisitUnaryOperator(self, node):
        self.operators.add((node.extent.start.offset, node.extent.end.offset))
        MyRecursiveASTVisitor.operators_count = len(self.operators)
        return True

    def VisitBinaryOperator(self, node):
        self.operators.add((node.extent.start.offset, node.extent.end.offset))
        MyRecursiveASTVisitor.operators_count = len(self.operators)
        return True

    def VisitIfStmt(node):
        print("if (", end='')
        node.cond_expr.accept()
        print(") {")
        if node.then_stmt is not None:
            node.then_stmt.accept()
        print("}", end='')
        if node.else_stmt is not None:
            print(" else {")
            node.else_stmt.accept()
            print("}", end='')
        print("")

    def VisitSwitchStmt(node):
        print("switch (", end='')
        node.cond.accept()
        print(") {")
        for case in node.cases:
            if case.label is not None:
                print("case ", end='')
                case.label.accept()
                print(":")
            else:
                print("default:")
            for stmt in case.stmts:
                stmt.accept()
        print("}")

    def VisitForStmt(self, ForStmt):
        self.output += "for {} in range({}, {}):\n".format(
            self.getVarName(ForStmt.getLoopVariable()),
            self.PrintExpr(ForStmt.getInit()),
            self.PrintExpr(ForStmt.getCond())
        )
        self.IncrementIndentLevel()
        self.TraverseStmt(ForStmt.getBody())
        self.DecrementIndentLevel()

    def VisitWhileStmt(self, WhileStmt):
        self.output += "while {}:\n".format(self.PrintExpr(WhileStmt.getCond()))
        self.IncrementIndentLevel()
        self.TraverseStmt(WhileStmt.getBody())
        self.DecrementIndentLevel()

    def VisitDoStmt(self, DoStmt):
        self.output += "while True:\n"
        self.IncrementIndentLevel()
        self.TraverseStmt(DoStmt.getBody())
        self.DecrementIndentLevel()
        self.output += "if not {}:\n".format(self.PrintExpr(DoStmt.getCond()))
        self.IncrementIndentLevel()
        self.output += "break\n"
        self.DecrementIndentLevel()


file = 'example.cpp'

with open(file, 'r') as f:
    code = f.read()

metrics = MyRecursiveASTVisitor(code)
