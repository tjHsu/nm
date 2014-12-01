# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math as math

# <codecell>

#first we try with upwind scheme and N=10.

# <codecell>

N   = 10 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a

print "N=",N,",nu=",nu,",a=",a,",M=",M,",h=",h,",tau=",tau

# <codecell>

def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# <codecell>

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

# <codecell>


#for time=0
for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]
#print exact    

# <codecell>

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
nm[0]=nm[N]
nm[N+1]=nm[1]
#print nm
#print nmnew

# <codecell>

#print "nm=",nm
print nu

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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]
        
        
#print nm        
#print nmnew
#print exact

    

# <codecell>

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

#the upwind scheme finish here , and all we do below is to chage N (i.e. 100, and 1000.)

# <codecell>

#upwind scheme N=100
N   = 100 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 


# <codecell>

#upwind scheme N=1000
N   = 1000 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

# <codecell>

#Start Lax-Wendroff scheme

# <codecell>

N   = 10 #grid size N can be 10,100, or 1000
nu  = 0.9
a   = 1
M   = math.ceil(N/nu)
h   = 1.0/N
tau = h*nu/a

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
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

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
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

exact=np.zeros(shape=(N+2))
nm=np.zeros(shape=(N+2))
nmnew=np.zeros(shape=(N+2))

for i in xrange (0,N,1):
    exact[i+1]= np.sin(2*np.pi*i*h)
    
exact[0]=exact[N] 
exact[N+1]=exact[1]

for i in xrange (0,N,1):
    nm[i+1]= np.sin(2*np.pi*i*h)
    
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
        exact[i+1]= np.sin(2*np.pi*(i*h-j*tau))
    exact[0]=exact[N] 
    exact[N+1]=exact[1]

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 

