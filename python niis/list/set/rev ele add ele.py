s={5,8,9,12,8}
ele=8
rep=7
for i in s:
	if i==ele:
		s.remove(ele)
		s.add(rep)
print(s)