def write(ast):
	f = open("assembly.s","w")


	f.write("\t.globl main\n")

	f.write("main:\n")

	f.write("\tmovl\t$"+ast+", %eax\n")

	f.write("\tret\n")
		

	f.close()

