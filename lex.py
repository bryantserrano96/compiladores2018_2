#use library re module for regular expressions
import re 

#declare a list "lex" to store tokens
lex = [] 

#function to add items into list "lex"
def add( a,b ):
	aux = []
	aux.append( a )
	aux.append( b )
	lex.append( aux )

#function to slice word with a givin position
def slice( string,i ): 
	return string[i:]

#set of regular expressions
c = '[(){};-]'
n = '\d+'
w = '[a-zA-Z]+\w'

#list of regular expressions
tokens = [c,n,w,"~","!"]

#list of reserved words
reserved = ["int","return"]

#dictionay to tag tokens
tag = {'(':"OPEN PA",')':"CLOSE PA",'{':"OPEN BR",'}':"CLOSE BR",';':"SEMIC",'-':"Negation",
'~':"Bitwise complement",'!':"Logical Negation",'int':"INT K",'return':"RETURN K",1:"INT",2:"IDENTIFIER"}

#function lexer
def lexer( data ):
	#case there's a space, \n or a \t
	if re.match( '\s',data ):
		#call function without space, \n or a \t
		lexer( slice( data,1 ) )		
	#iterate through list of tokens
	for t in tokens:
		#case there's a match
		if re.match( t,data ):
			#save match in variable
			a = re.match( t,data )
			#case matches a number
			if re.match( n,data ): add( tag[1],a.group() )
			#case matches a word
			elif re.match(w,data):
				#case matches a word and NOT a reserverd word
				if a.group() not in reserved: add( tag[2],a.group() )
				#case matches a word and it's a reserved word (keyword)
				else: add( tag[a.group()],a.group() )
			#anyother case (single characters tokens)	
			else: add( tag[a.group()],a.group() )
			#after adding to list "lex", call function again without the matched word
			lexer( slice( data,len( a.group() ) ) )
	#return list lex with tokens 		
	return lex
