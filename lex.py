#use library re module for regular expressions
import re 

#function to slice word with a givin position
def slice(string,i):
	return string[i:]

#function to add items into list "l"
def add( a,b,c ):
	aux = []
	aux.append( b )
	aux.append( c )
	a.append( aux )


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

class Lexer:
	#Unique list "l",position error and size for each instance
	def __init__( self,data ):
		self.l = []
		self.pos_error = 0
		self.size = len( data )

	#function lexer
	def lex( self,data ):
		#case there's a space, \n or a \t
		if re.match( '\s',data ):

			#update position and size
			self.pos_error = self.pos_error + 1
			self.size = self.size - 1

			#call function without space, \n or a \t
			self.lex( slice( data,1 ) )		

		#iterate through list of tokens
		for t in tokens:

			#case there's a match
			if re.match( t,data ):

				#save match in variable
				a = re.match( t,data )

				#case matches a number
				if re.match( n,data ): add( self.l,tag[1],a.group() )

				#case matches a word
				elif re.match( w,data ):

					#case matches a word and NOT a reserverd word
					if a.group() not in reserved: add( self.l,tag[2],a.group() )

					#case matches a word and it's a reserved word (keyword)
					else: add( self.l,tag[a.group()],a.group() )

				#anyother case (single characters tokens)	
				else: add( self.l,tag[a.group()],a.group() )

				#update position and size
				self.pos_error = self.pos_error + len( a.group() )
				self.size = self.size - len( a.group() )

				#after adding to list "lex", call function again without the matched word
				self.lex( slice( data,len( a.group() ) ) )

		#returns list of tokens if it checked the whole string
		if self.size == 0:
			return self.l 

		#returns error in case a character unknown is found
		else:
			print ("Lexer Error after position: "+str( self.pos_error ) )
			exit()
