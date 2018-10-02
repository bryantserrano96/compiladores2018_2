import lex
import parser
import generate

import os

from anytree import Node, RenderTree, PreOrderIter

from sys import*


def open_file(file):
	data = open(file,"r").read()
	return data

data = open_file( argv[1] )

#print ( lex.lexer(data) )

a = parser.program( lex.lexer( data ) )

tree = [node.name[0] for node in PreOrderIter(a)]

num = tree[3]

generate.write(num)


os.system("gcc -m64 assembly.s -o out")
