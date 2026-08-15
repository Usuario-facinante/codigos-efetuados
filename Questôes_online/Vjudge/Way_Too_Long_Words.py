"""Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes."""
Quantidade_de_palavras = int(input())
for a in range (Quantidade_de_palavras):
	Nome = input()
	if len(Nome) > 10:
		print (f"{(Nome[0])}{((len(Nome))-2)}{Nome[len(Nome)-1]}")
	else:
		print(Nome)