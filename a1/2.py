ciphertext = "T qcura wthl rrscmc q yyew qsxgthhh drkjh F vtoyat bw qgvlhqnr pmdjrb, rhz ymxd B fhqxftpt R qcura poqsiw xmx scmzvhdt uvut df vdsjhwfuhlcds hvtzmdbp godulyt dn smx scmnbzx cefjbifnji. Gh mtp qrud vmbi lvlh 35000 khuxv sr vs smhbs jmxd, vqnm lxnfi knt rsiv fsxgthlhf, thz usrbnnyv, M rdn's pjnw, i xfnyqb ktcth 35000 khuxv sf dmvpyi, wihluxp, fboko, tmxkc, ezc bsymw qcnrysct. Jy e txqdwqbiw oefifhf eyovbhd, S kie e fjhulvyb vrufrxh. --Wmxgthebtf"


decodedtext = ""
# assumes first letter is capital and alphabetic
for x in range (26): 
	if ( ( ( x + 65 + ord ( ciphertext[len(ciphertext) - 1] ) ) % 26 ) == ( ord ( ciphertext[0] ) - 65)):
		original = x 
firstLetter = chr ( original + 65 )
decodedtext = decodedtext + firstLetter

prevLetter = firstLetter

for i in range ( 1, len(ciphertext) - 1 ): 
	if ( ciphertext[i].isalpha() ):
		if( ciphertext[i].islower() ):
			offset = 97
		else:
			offset = 65

		for x in range (26): 
			if ( ( ( x + offset + ord ( prevLetter ) ) % 26 ) == ( ord ( ciphertext[i] ) - offset )):
				original = x 

		letter = chr ( original + offset)

		decodedtext = decodedtext + letter
		prevLetter = letter

	else: 
		decodedtext = decodedtext + ciphertext[i]

print(decodedtext)
print()
