import os
import time
while True:
	os.system('tshark -i eth0 -c 2 -R "tcp and ip.dst==192.168.246.134 and tcp.flags.syn == 0x02 and tcp.window_size==16384 "> /root/Desktop/captcp2.txt')
		   
	
	#os.system("cat captcp2.txt | grep TCP> captcpclean.txt")
	
	#ftcp=open('/root/Desktop/captcpclean.txt','r')
	ftcp=open('/root/Desktop/captcp2.txt','r')
	getstr=[]
	
	for li3 in ftcp:
		spd=li3.split(' ')
		
		le=len(spd)
		for i in range (0,le-1):
		
		
			if(cmp(spd[i],'')!=0):
				getstr.append(spd[i])
			
		src=getstr[1]
		dpt=getstr[7]
		#print dpt
		if(cmp(dpt,'netbios-ssn')==0):
			dpt='139'
		srcrange=src+'/16'
		os.system('iptables -A INPUT -p tcp -s %s -d 192.168.246.134 --dport %s -j DROP'%(srcrange,dpt))
	
	ftcp.close()
	
	
		
	
		
