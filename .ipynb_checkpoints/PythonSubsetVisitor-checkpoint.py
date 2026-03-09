# Generated from PythonSubset.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonSubsetParser import PythonSubsetParser
else:
    from PythonSubsetParser import PythonSubsetParser

# This class defines a complete generic visitor for a parse tree produced by PythonSubsetParser.

class PythonSubsetVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonSubsetParser#program.
    def visitProgram(self, ctx:PythonSubsetParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#statement.
    def visitStatement(self, ctx:PythonSubsetParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#assignment.
    def visitAssignment(self, ctx:PythonSubsetParser.AssignmentContext):
        return self.visitChildren(ctx)



del PythonSubsetParser