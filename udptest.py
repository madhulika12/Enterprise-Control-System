import os
import binascii

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

#srcport=string[7]

dp=string[10]
ds=dp[0:(len(dp)-2)]
if (cmp(ds,"synapsis-edg")==0):
	dstport='5008'
	print dstport
				
				
fip.close()
				
fcontent=open('/root/Desktop/capudpcontent.txt','r')
fsnort=open('/etc/snort_inline/drop-rules/my.rules','a')
uc=fcontent.readline()
#print len(uc)
udpcontent=uc[0:(len(uc)-1)]
#print udpcontent
nc=udpcontent
print nc
nc1=binascii.unhexlify(nc)
newcontent='"'+nc1+'"'
print newcontent
fsnort.write('drop udp %s any -> 192.168.246.134 %s (msg:"drop more udp";content:%s;sid:100;)'%(src,dstport,newcontent))
fsnort.write('\n')
fcontent.close()
fsnort.close()

os.system('iptables -I INPUT -p udp --dport %s -j QUEUE'%dstport)
os.system("snort_inline -c /etc/snort_inline/snort_inline.conf -Q -N -l /var/log/snort_inline/ \-t /var/log/snort_inline/ -v")
