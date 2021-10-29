text = []
filename = input()
with open (filename) as text_r:
	for line in text_r:
		text.append(line)
print(text)
for i in range(len(text)):	
	if ("{\n" in text[i]):
		print("Finding { and replacing...")
		text[i] = text[i].replace('{','',1)
		text[i-1] = text[i-1].replace('\n','')
		text[i-1] = text[i-1] + "{"
		print("OK")
fileptr = open(filename + "_edited.txt","w")
for i in range(len(text)):	
	fileptr.write(text[i])
fileptr.close()