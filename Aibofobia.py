# -*- coding: utf-8 -*-
# By: LawlietJH
# Aibofobia.py
# Python 3
# v1.0.0



def GetPalindromo(Cad):
	
	Inv = Cad[::-1]
	Tam = len(Cad)
	Sal1 = ''
	Sal2 = ''
	
	if   Cad == '': return ''
	elif Cad == Inv: return True
	else:
		
		for x in range(Tam):
			
			if Cad[x:].find(Inv[:Tam-x]) == 0: Sal1 = Cad + Inv[Tam-x:]; break
		
		for x in range(Tam):
			
			if Inv[x:].find(Cad[:Tam-x]) == 0: Sal2 = Inv + Cad[Tam-x:]; break
		
		if len(Sal1) > len(Sal2): return Sal2
		else: return Sal1



print("\n\n\t\t Convierte Cualquier Cadena En Un Palindromo.")
	
while(True):
	
	Palabra = input("\n\n\t Escribe Una Palabra: ").lower().replace(' ', '')

	Palindromo = GetPalindromo(Palabra)

	if Palindromo == True: print("\n Ya Es Un Palindromo ---> " + Palabra)
	else: print("\n\n\t Palindromo: " + Palindromo)


