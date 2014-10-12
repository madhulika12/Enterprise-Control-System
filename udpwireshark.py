from multiprocessing import Process

import os,re,sys
import time
import binascii


udppid=False
	#udp3=0
hostabnormal=False
def UDP():
	
		udpid=os.getpid() #define 5009 offline monitored udp attack
		print "udppid"
		print udpid
		udppid=True
		os.system("modprobe ip_queue")
		os.system("iptables -I INPUT -p udp --dport 5009 -j QUEUE")
		print "run snort"
		os.system("snort_inline -c /etc/snort_inline/snort_inline.conf -Q -N -l /var/log/snort_inline/ \-t /var/log/snort_inline/ -v -D")
		
def UDP2():
		
		os.system('iptables -A INPUT -p udp -d 192.168.246.134 --dport 5009 -j DROP')
		print "define udp2 finish"

def UDP3():
			
		udp3=os.getpid()
		print udp3
		os.system('tshark -i eth0 -c 1  -R "udp and ip.dst==192.168.246.134"  > /root/Desktop/capudpip.txt')
		os.system('tshark -i eth0 -e data -T fields -c 1  -R "udp and ip.dst==192.168.246.134"  > /root/Desktop/capudpcontent.txt')
			
		fip=open('/root/Desktop/capudpip.txt','r')
			
		string=[]
	
		l2=fip.readline();

		tmp=l2.split(' ')
		leng=len(tmp)

		for i in range (0,leng):
		
		
				if(cmp(tmp[i],'')!=0):
					string.append(tmp[i])
				
		src=string[1] #src
		print src



		dp=string[10]
		ds=dp[0:(len(dp)-2)]
		if (cmp(ds,"synapsis-edg")==0):
			dstport='5008'
		#print dstport
				
				
		fip.close()
				
		fcontent=open('/root/Desktop/capudpcontent.txt','r')
		fsnort=open('/etc/snort_inline/drop-rules/my.rules','a')
		uc=fcontent.readline()

		udpcontent=uc[0:(len(uc)-1)]

		nc=udpcontent
	#print nc
		nc1=binascii.unhexlify(nc)
		newcontent='"'+nc1+'"'
		print newcontent
		fsnort.write('drop udp %s any -> 192.168.246.134 %s (msg:"drop more udp";content:%s;sid:100;)'%(src,dstport,newcontent))
		fsnort.write('\n')
		fcontent.close()
		fsnort.close()

		os.system('iptables -I INPUT -p udp --dport %s -j QUEUE'%dstport)
		os.system("snort_inline -c /etc/snort_inline/snort_inline.conf -Q -N -l /var/log/snort_inline/ \-t /var/log/snort_inline/ -v -D") 


for i in range (0,3):

	if(udppid==False):
		#print "in parent process (id %s)" % os.getpid()
		#print "xxx"
		#os.system("python /root/Desktop/udp.py")
		UDP()
		time.sleep(15)
		print "1 finish"
	#time.sleep(5)
	
		previous='UDP'
		udppid=True
	elif (cmp(previous,'UDP')==0 and udppid==True and hostabnormal==False):
	
		UDP2()
		hostabnormal=True  
	   	print " udp 2 done"
	elif(cmp(previous,'UDP')==0 and udppid==True and hostabnormal==True):
		os.system("killall -9 snort_inline")
		UDP3()
		time.sleep(10)
		print "UDP3 done"
	
	print "previous %s"%previous
	print "udppid %s"%udppid
	print "hostabnormal %s"%hostabnormal
