words = open("sample2.txt", "r")
line=[]
lst=[]
for word in words:
	string = word.lower().replace(',','').replace('.','').split(" ");    
for s in string:  
	line.append(s); 

for w in line:
	if w.endswith('ed'):
		lst.append(w)
	elif w.endswith('ion'):
		lst.append(w)
	else:
		pass 

print(lst)


average = sum(len(lst) for word in lst) / len(lst)
print(average)
