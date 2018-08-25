#Serrano Sanchez Bryant Ricardo
#Compiladores - Lexer
from sys import *

#read content from file
def open_file(file):
	data = open(file,"r").read()
	return data

#lex function
def lex(content):
	token = ""

	flag_s = 0
	string = ""

	flag_i = 0
	integer = ""

	lexer = []
	#save the content of file as list
	content = list(content)

	
	for char in content:
		token += char
		if token == " " and flag_s != 1:
			token = ""				

		elif token == '\t' and flag_s != 1:
			token = ""

		elif token == '\n' and flag_s != 1:
			token = ""
			
		elif token == "{":
			new_item = []
			new_item.append("openBrace")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "}":
			new_item = []
			new_item.append("closeBrace")
			new_item.append(token)
			lexer.append(new_item)

			token = ""

		elif token == "(":
			new_item = []
			new_item.append("openParenthesis")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == ")":
			new_item = []
			new_item.append("closeParenthesis")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""		

		#when using multi-digit integers: untill lexer finds a semicolon, it inserts the integer	
		elif token == ";":
	
			if integer != "" and flag_i == 0:

				new_item = []
				new_item.append("ID INT")
				new_item.append(integer)
				lexer.append(new_item)
				integer = ""	

			new_item = []
			new_item.append("semicolon")
			new_item.append(token)
			lexer.append(new_item)
			
			"""elif expr != "" and isexpr == 0:
				print(expr + "num")
				expr = ""
			"""

			token = ""		
				
		elif token == "int":
			new_item = []
			new_item.append("INT KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "return":
			new_item = []
			new_item.append("RETURN KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""
			
		elif token == "main":
			new_item = []
			new_item.append("MAIN KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "print":
			new_item = []
			new_item.append("PRINT KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "\"":
			
			if flag_s == 0:
				flag_s = 1
			elif flag_s == 1:
				new_item = []
				new_item.append("ID STRING")
				new_item.append(string)
				lexer.append(new_item)
				
				string = ""
				flag_s = 0
				token = ""

		elif flag_s == 1:
			string += char
			token = ""

		elif token == "0" or token == "1" or token == "2" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9":

			integer += token
			token = ""
		

		"""elif token == "+":
			isexpr = 1
			expr += token
			token = ""
		"""	
	return lexer
	

def parse(tokens):


	par = []

	if len(tokens) == 0:
		print("ERROR: SOURCE CODE EMPTY")

	else:
		for sublist in tokens:
			if sublist[0] == 'MAIN KEYWORD':
				print("found main")
			


def run():
    #file's name goes as second parameter in command line
	data = open_file(argv[1])
	print(lex(data))



run() 


