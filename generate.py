#calls modules from anytree to reed tree from parser
from anytree import Node, RenderTree, PreOrderIter

#function to write an .s document
def write( ast ):

	#saves preorder items from tree in t
	t = [node.name[0] for node in PreOrderIter( ast )]

	#saves number
	num = t[3]

	#creates and overwrites over assembly.s
	f = open( "assembly.s","w" )
	#line for .globl main
	f.write( "\t.globl main\n" )
	#line for main:
	f.write( "main:\n" )
	#line for movl $"cte", %eax
	f.write( "\tmovl\t$"+num+", %eax\n" )
	#line for ret
	f.write( "\tret\n" )
	#closes document
	f.close()
