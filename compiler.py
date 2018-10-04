#imports lex, parser and generate programs
import lex
import parser
import generate

#import os to write in terminal
import os

#to read document from terminal
from sys import*

#function to open file
def open_file( file ):
	data = open( file,"r" ).read()
	return data

#stores data from second argument in terminal
data = open_file( argv[1] )

#creates instance of Lexer
x = lex.Lexer( data )

#runs lexer, parser and generate progrmas over data
generate.write( parser.parse_program( x.lex( data ) ) )

#creates assembly executabe
os.system("gcc -m64 assembly.s -o out")
