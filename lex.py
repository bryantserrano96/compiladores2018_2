#Use library re module for regular expressions
import re

#declare a list to store tokens
lex = []

#function to add items into list "lex"
def add( a,b ):
	aux = []
	aux.append( a )
	aux.append( b )
	lex.append( aux )

#function to slice word with a givin position
def slice( string,i ):
	return string[ i: ]

#set of regular expressions
c = '[ (){};- ]'
n = '\d+'
w = '[ a-zA-Z ]+\w'

#list of regular expressions
tokens = [ "int","return",c,n,"~","!" ]

reserved = [ "int","return" ]

#dictionary to tag a token with its name
tag = { '(':"OPEN PA",')':"CLOSE PA",'{':"OPEN BR",'}':"CLOSE BR",';':"SEMIC",'-':"Negation",
'~':"Bitwise complement",'!':"Logical Negation",'int':"INT K",'return':"RETURN K",1:"INT",2:"IDENTIFIER" }

#function lexer
def lexer( data ):
	#case there's a space, \n or a \t
	if re.match( '\s',data ):
		#call function without space, \n or a \t
		lexer( slice( data,1 ) )		
	#case theres a re that matches [a-zA-Z]+\w
	if re.match(w,data):
		#save match in variable
		a = re.match(w,data)
		#condition it's not a reserved word
		if a.group() not in reserved:
			#add it to list "lex"
			add( tag[ 2 ],a.group() )
			#call function lexer without the word matched
			lexer( slice( data,len( a.group() ) ) )
	
	#iterate through list of tokens
	for t in tokens:
		#case theres a match
		if re.match( t,data ):
			#save match in variable
			a = re.match( t,data )
			#case if its a number
			if re.match( n,data ): add( tag[ 1 ] , a.group() )
			#any other case "match"
			else: add( tag[ a.group() ] , a.group() )
			#after adding to lex, call function again without the matched word
			lexer( slice( data,len( a.group() ) ) )
	#return list "lex" with tokens 		
	return lex
