file_obj=open('Crime.csv')
line1=[]
line2=[]
dict_id_name={}

def check_Str(s):
	d={}
	for c in s:
		d[c]=1+d.get(c,0)
	return d


for line in file_obj:
	line.strip() # removing whitespaces
	for i in line.split(','): #extracting data
		line1.append(i)

i=16
while i<len(line1):
	line2.append(line1[i])
	i+=9
dic_crimeid=check_str(line2) 


lineD=line(dic.keys())
for i in range(len(line1)):
	if line1[i] in lineD:
		dict_id_name[line1[i]]=line1[i+1].strip()


print("{0:25s} {1:25s} {2:1s}".format('Crime type','Crime ID','Crime Count'))
for key,value in dic_crimeid.items():
	if key in dict_id_name.keys():
print("{0:25} {1:25} {2:1}".format(dict_id_name[key],key,dic_crimeid[key]))
