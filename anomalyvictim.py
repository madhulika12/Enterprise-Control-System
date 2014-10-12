

f1=open('test_normal.csv','r')
wr=open('test.arff','w+b')
wr1=open('test.csv','w+b')
line = f1.readlines()

sub='," ",'
for l in line:
    if(l.find(sub)<0):
        #string=l+'\r\n'
        wr1.write(l)
wr1.close()        
f2=open('test.csv','r')
lines = f2.readlines()
number=len(lines)
l_list=lines[number-5:number]

mem=592052.3*0.8
BR=431.97*1.2
BS=4.928336*1.2
PR=3.566611*1.2
PS=0.08397*1.2
IOR=250.3041	*1.2
IOW=527.3424	*1.2
Id=99.70744*1.2
Pro=0.2932*1.2
US= 0.023423*1.2
newmem=0
newBR=0
newBS=0
newPR=0
newPS=0
newIOR=0
newIOW=0
newID=0
newPro=0
newUS=0
abnormal=0
print mem
print BR
print BS
print PR
print PS
print IOR
print IOW
print Id
print Pro
print US
for li in l_list:
    data=li.split(',')
    #print data


    length=len(data[1])

  

    a=data[1][1:length-1]

    #print a



    length2=len(data[2])

  

    b=data[2][1:length2-1]

    #print b



    length3=len(data[3])  

    c=data[3][1:length3-1]

    #print c



    length4=len(data[4])  

    d=data[4][1:length4-1]

    #print d

    

    length5=len(data[5])  

    e=data[5][1:length5-1]

    #print e

    

    length6=len(data[6])

    f=data[6][1:length6-1]

    #print f

    
    #print data[7]
    length7=len(data[7])

    g=data[7][1:length7-1]

    #print g





    length8=len(data[8])

    h=data[8][1:length8-1]

    #print h



    length9=len(data[9])

    i=data[9][1:length9-1]

    #print i

    length10=len(data[10])

    j=data[10][1:length10-2]

    d1=float (a)
    
    d2=float(b)
    d3= float(c)
    d4=float (d)
    d5=float (e)
    d6=float (f)
    d7=float (g)
    d8=float (h)
    d9=float (i)
    d10=float (j)
    #print d10
    if(0):#command
        d1=float (data[1])    
        d2=float(data[2])
        d3= float(data[3])
        d4=float (data[4])
        d5=float (data[5])
        d6=float (data[6])
        d7=float (data[7])
        d8=float (data[8])
        d9=float (data[9])
        d10=float (data[10])
    #wdata=str(newmem)+','+str(newBR)+','+str(newBS)+','+str(newPR)+','+str(newPS)+','+str(newIOR)+','+str(newIOW)+','+str(newID)+','+str(newPro)+','+str(newUS)+','+data[10]+'\r\n'
    #print wdata
    #wr.write(wdata)
    newmem=newmem+d1
    newBR=newBR+d2
    newBS=newBS+d3
    newPR=newPR+d4
    newPS=newPS+d5
    newIOR=newIOR+d6
    newIOW=newIOW+d7
    newID=newID+d8
    newPro=newPro+d9
    newUS=newUS+d10

newmem=newmem/5
newBR=newBR/5
newBS=newBS/5
newPR=newPR/5
newPS=newPS/5
newIOR=newIOR/5
newIOW=newIOW/5
newID=newID/5
newPro=newPro/5
newUS=newUS/5
print newmem
print newBR
print newBS
print newPR
print newPS
print newIOR
print newIOW
print newID
print newPro
print newUS
if(newmem<mem):
    abnormal=abnormal+1
if(newBR> BR):
    abnormal=abnormal+1
if(newBS > BS):
    abnormal=abnormal+1
if(newPR > PR):
    abnormal=abnormal+1
if(newPS > PS):
    abnormal=abnormal+1
if(IOR > newIOR):
    abnormal=abnormal+1
if(IOW > newIOW):
    abnormal=abnormal+1
if(newID > Id):
    abnormal=abnormal+1
if(newPro > Pro):
    abnormal=abnormal+1
if(newUS > US):
    abnormal=abnormal+1
print abnormal
if(abnormal>3):
        hostabnormal=True
else:
        hostabnormal=False
print hostabnormal
f1.close()    

print "finish"
