text = "X-DSPAM-Confidence:    0.8475"
space = text.find(" ")
#print(space)
spaceon = text[space : ]
numb = spaceon.lstrip()
numfinal = float(numb)
print(numfinal)