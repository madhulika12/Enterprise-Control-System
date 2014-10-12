import os
def test():
		os.system('tshark -i eth0 -c 20  -R "ip.dst==1.0.0.9"  > /root/Desktop/testunknown.txt')
		os.system('tshark -i eth0 -c 2 -e data -T fields   -R "ip.dst==1.0.0.9"  > /root/Desktop/capunknowncontent.txt')
			
		fip=open('/root/Desktop/testunknown.txt','r')
			
		string=[]
	
		lines=fip.readlines();
		number=len(lines)
		l_list = lines[0:number-1] 
		for l2 in l_list:

			 tmp=l2.split(' ')
			 leng=len(tmp)

			 for i in range (0,leng):
			
				if(cmp(tmp[i],'')!=0):
					string.append(tmp[i])
				
			 src=string[1] #src
			 print src
			 dp=string[7]
			 #ds=dp[0:(len(dp)-2)]
			 print dp
			 if (cmp(dp,"netbios-ssn")==0):
				dstport='139'
			 print dstport
	 	fip.close()

test()
