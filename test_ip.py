f1=open('/root/Desktop/captcp.txt','r')
	#wr=open('/root/Desktop/dos_attack_weka_controller/new','w')
	#f2=open('/root/Desktop/dos_attack_weka_controller/new','r')
lines = f1.readlines()
string=[]
number=len(lines)
l_list = lines[number-2:number-1] 
for li2 in l_list:
	splitdata=li2.split(' ')
	leng=len(splitdata)
	#print leng
	for i in range (0,leng-1):
		#print "sss"
		#print splitdata[i]
		if(cmp(splitdata[i],'')!=0):
			string.append(splitdata[i])
	#print string
	src=string[1]
	print src
	
