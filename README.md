Enterprise
==========

MODIFICAITONS 21 = 

-I wrote a script to start up both the mtu.c and whichever of the 3 attacks I'm using. it's in the scripts folder as attack.sh

-I modified the mtu.c code so that it doesn't wait on a tcp response. Just grabs the serial data and converts/sends tcp data. I don't want a tcp RST packet to cause the converter to fail. Cause it did.

-i wrote my own HMI in an Python environment within Ubuntu. It does need the modbus-tk library and python-tk for graphics. Should be under trunk and ZaxGraphics

-I think I'm gonna reincorporate the master PLC so I can try to have multiple slaves. Let's see. But I'm pretty sure the master is only a MODBUS client, not a MODBUS server. Gotta fix that first. This may mean rearchitecting Brad's whole system. Poopoo.

-Looks like the tcptank config also had to be modified. I don't know why, but Bill has his memory model as control_micro_systems but all his addresses are for "control_old". I changed it to "old" as well as the IP address to 10.128.0.1

-yeah, the tcptank is a really simple simulation. Like stupid, unusable, simple. I wonder if that's for the big tanks in the SCADA lab.

-created a tcpwater simulation. Just took his rtuwater and changed the config file for tcp. I think it's gonna work. Device ID 7 BTW.

-i modified the ports being used, because I wanna run multiple simulations at once. The tcpwater simulation now uses 9922,9923,and 503 instead of 9912, 9913, and 502.

-yeah, I had to modify the simulation.py script because it's written to look at the rtuwater config file. Not cool. Now it looks at the tcpwater config file.

-modifying the ports works for 2 slaves at once. Just have to tell the HMI to read from port 503 on the second simulation

-added "sudo yum install tkinter" to the init script. Need it for my python HMI
