import pexpect
import time
def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    r = ''

    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'],timeout=50)
	#time.sleep(10)
        if i == 0 :
            ssh.sendline(passwd)
	     
        elif i == 1:
            ssh.sendline('yes')
    except pexpect.EOF:
        ssh.close()
	print "EOF"
    except pexpect.TIMEOUT:
	print "timeout"
	ssh.close()
    else:
        r = ssh.read()
        ssh.expect(pexpect.EOF)
        ssh.close()
    return r

#hosts = '''
#3.0.0.1:root:000000:iptables -t nat -A PREROUTING -d 1.0.0.2 -p udp --dport 5008 -j DNAT --to #1.0.0.9:5008'''
ip='3.0.0.1'
user='root'
passwd='000000'
port='1234'
cmd="iptables -t nat -A PREROUTING -d 1.0.0.2 -p udp --dport %s -j DNAT --to 1.0.0.9:%s"%(port,port)
#cmd="mkdir /root/Desktop/test1"
#for host in hosts.split("\n"):
 #   if host:
 #       ip, user, passwd, cmds = host.split(":")
 #       for cmd in cmds.split(","):
 #           print "-- %s run:%s --" % (ip, cmd)
ssh_cmd(ip, user, passwd, cmd)                                
