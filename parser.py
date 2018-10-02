
from anytree import Node, RenderTree


def addT(name,par = None):
		if par == None: aux = Node(name,parent = None)

		else: aux = Node(name,parent = par)

		return aux


def printT(root):
	for pre,fill,node in RenderTree(root):
		print("%s%s" % ( pre,node.name[0] ))


def slice(string,i):
	return string[i:]



def program(lexer):
	
	if len(lexer) > 0 and function(lexer):
		p = function(lexer)
		a = addT(["Program",1])
		p.parent = a
		return a

	else:
		print "Syntax error"


def function(fun):
	if fun[0][0] == "INT K":
		if fun[1][0] == "IDENTIFIER":
			if fun[2][0] == "OPEN PA":
				if fun[3][0] == "CLOSE PA":
					if fun[4][0] == "OPEN BR":

						if statement( slice(fun,5) ):
							a,b = statement( slice(fun,5) )

							if b[0][0] == "CLOSE BR":

								main = addT(["Function",fun])
								a.parent = main
								return main

def statement(st):
	if st[0][0] == "RETURN K":
		if exp( slice(st,1) ):

			a,b = exp(slice(st,1))
			if b[0][0] == "SEMIC":

				re = addT(["Return",st])
				a.parent = re
				return re,slice(b,1)
			

def exp(ex):
	if ex[0][0] == "INT":
		cte = addT([ex[0][1],ex])
		return cte, slice(ex,1)
	
