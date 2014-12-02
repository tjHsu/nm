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

#print "N=",N,",nu=",nu,",a=",a,",M=",M,",h=",h,",tau=",tau

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
#print nu

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

#error of this scheme
errorc=np.zeros(shape=(3))
error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorc[0] = max(error)
"""    
print exact
print nmnew
print error
"""

# <codecell>

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_upwind_N10.png",dpi=300,format="png") 
#plt.show() 
plt.clf()

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
    
error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorc[1] = max(error)
    


x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_upwind_N100.png",dpi=300,format="png") 
#plt.show() 

plt.clf()


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
    
error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorc[2] = max(error)
    

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_upwind_N1000.png",dpi=300,format="png") 
#plt.show() 
plt.clf()

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

errorcl=np.zeros(shape=(3))
error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorcl[0] = max(error)
    

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_LaxWendroff_N10.png",dpi=300,format="png") 
#plt.show() 
plt.clf()

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

error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorcl[1] = max(error)
    

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_LaxWendroff_N100.png",dpi=300,format="png") 
#plt.show() 
plt.clf()

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
    

error=np.zeros(shape=(N))
for i in xrange(0,N,1):
    error[i] = math.fabs(exact[i+1]-nmnew[i+1])
errorcl[2] = max(error)

x1 = np.linspace(0,1,N+2)
y1 = nmnew
y2 = exact
plt.plot(x1,y1)
plt.plot(x1,y2,"r")
#plt.savefig("hw4_LaxWendroff_N1000.png",dpi=300,format="png") 
#plt.show() 
plt.clf()

# <codecell>

#print errorc
#print errorcl

x3=[10,100,1000]
y3=errorc
y4=errorcl
plt.plot(x3,y3,"b",label="Upwind Scheme")
plt.plot(x3,y4,"r",label="Lax-Wendroff Scheme")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('the norm of the error')
plt.legend(loc='upper right' )
plt.savefig("error_logscale.png",dpi=300,format="png")
#plt.show()

# <codecell>


