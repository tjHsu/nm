# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math as math


# <codecell>

#Start Upwind scheme

# <codecell>

N   = 10 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=(1-nu)*nm[i+1]+nu*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

#the upwind scheme finish here , and all we do below is to chage N (i.e. 100, and 1000.)

# <codecell>

N   = 100 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=(1-nu)*nm[i+1]+nu*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

N   = 1000 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=(1-nu)*nm[i+1]+nu*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 





# <codecell>

#first we try Lax-Wendroff scheme with N=10




# <codecell>

N   = 10 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=((nu*nu/2)-(nu/2))*nm[i+2]+(1-nu*nu)*nm[i+1]+((nu*nu/2)+(nu/2))*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

#the Lax-Wendroff scheme finish here , and all we do below is to chage N (i.e. 100, and 1000.)

# <codecell>

N   = 100 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=((nu*nu/2)-(nu/2))*nm[i+2]+(1-nu*nu)*nm[i+1]+((nu*nu/2)+(nu/2))*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

N   = 1000 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a
print "M=",M

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    #print i*h
    if i*h<0.5:
        exact[i+1] = 1      
    else:
        exact[i+1] = 0
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
print exact

for i in xrange (0,N,1):
    if i*h<0.5:
        nm[i+1] = 1      
    else:
        nm[i+1] = 0

    
nm[0]=nm[N]
nm[N+1]=nm[1]

for j in xrange (1,int(M)+1,1):

    if j!=1:
        for i in xrange(0,N,1):
            nm[i+1]=nmnew[i+1]
    nm[0]=nm[N]
    nm[N+1]=nm[1]
    
    for i in xrange(0,N,1):
        nmnew[i+1]=((nu*nu/2)-(nu/2))*nm[i+2]+(1-nu*nu)*nm[i+1]+((nu*nu/2)+(nu/2))*nm[i]
    nmnew[0]=nmnew[N]
    nmnew[N+1]=nmnew[1]
    

    for i in xrange(0,N,1):
        
        #print i*h-j*tau
        if i*h-j*tau>=0.5 and i*h-j*tau<1:
            exact[i+1] = 0
        if i*h-j*tau<0.5 and i*h-j*tau>=0:
            exact[i+1] = 1      
        if i*h-j*tau<0 and i*h-j*tau>=-0.5:
            exact[i+1] = 0
        if i*h-j*tau>=-1 and i*h-j*tau<-0.5:
            exact[i+1] = 1

            
#       exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))    
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
    #print exact

    
x1 = np.linspace(0,1,N+2)
y1 = nm
y2 = exact
plt.plot(x1,y1)
plt.ylim(0,1.1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

