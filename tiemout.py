import sys
import signal
 
class TimeoutException(Exception): 
    pass 
 
def get_name():
    def timeout_handler(signum, frame):
        raise TimeoutException()
 
    old_handler = signal.signal(signal.SIGALRM, timeout_handler) 
    signal.alarm(3) # triger alarm in 3 seconds
 
    try: 
        print "Please enter a name: ",
        name = sys.stdin.readline()
    except TimeoutException:
        return "default value"
    finally:
        signal.signal(signal.SIGALRM, old_handler) 
 
    signal.alarm(0)
    return name
 
if __name__ == '__main__':
    name = get_name()
    print "Got: %s" % name,
