#imports lex, parser and generate program
import lex
import parser
import generate

#import os to write in terminal
import os

#calls modules from anytree to reed tree from parser
from anytree import Node, RenderTree, PreOrderIter

#to read document from terminal
from sys import*

#function to open file
def open_file(file):
	data = open(file,"r").read()
	return data

#stores data from second argument in terminal
data = open_file( argv[1] )

#stores tree in "a"
a = parser.parse_program( lex.lexer( data ) )

#saves preorder items from tree in t
t = [node.name[0] for node in PreOrderIter(a)]

#saves number ( number in node "Cte")
num = t[3]

#generate assembly program with number givin
generate.write(num)

#creates executabe assembly program
os.system("gcc -m64 assembly.s -o out")
