#function to write an .s document
def write(ast):
	#creates or overwrites over assembly.s
	f = open("assembly.s","w")
	#line for .globl main
	f.write("\t.globl main\n")
	#line for main:
	f.write("main:\n")
	#line for movl $"cte", %eax
	f.write("\tmovl\t$"+ast+", %eax\n")
	#line for ret
	f.write("\tret\n")
	#closes document
	f.close()
