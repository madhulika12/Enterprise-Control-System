from multiprocessing import Process
import os
import time
childpid=0
def sleeper():
   childpid=os.getpid()
   print 'starting child process with id: %d '%childpid
   print 'parent process:', os.getppid()
   #print 'sleeping for %s ' % seconds
   os.system("snort_inline -c /etc/snort_inline/snort_inline.conf -Q -N -l /var/log/snort_inline/ \-t /var/log/snort_inline/ -v")
   print "Done sleeping"


#if __name__ == '__main__':
print "in parent process (id %s)" % os.getpid()
p = Process(target=sleeper)
p.start()
   #print "in parent process after child process start"
   #print "parent process about to join child process"
   #p.join()
time.sleep(5)
os.system("kill -9 %d"%childpid)
print "killed"
print childpid
print "in parent process after child process join" 
print "parent process exiting with id ", os.getpid()
print "The parent's parent process:", os.getppid()  
