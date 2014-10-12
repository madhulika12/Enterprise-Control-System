from multiprocessing import Process

import os,re,sys
import time
import binascii

def UDP():
	
		udpid=os.getpid() #define 5009 offline monitored udp attack
		print "udppid"
		print udpid
		udppid=True
		os.system("modprobe ip_queue")
		os.system("iptables -I INPUT -p udp --dport 5009 -j QUEUE")
		print "run snort"
		os.system("snort_inline -c /etc/snort_inline/snort_inline.conf -Q -N -l /var/log/snort_inline/ \-t /var/log/snort_inline/ -v -D")
		

UDP()
time.sleep(15)
print "UDP1 exit"
sys.exit(0)
