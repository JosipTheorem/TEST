import numpy as np
import matplotlib.pyplot as plt

Imaginarni=np.linspace(-1,1,1000)*1j
Realni=np.linspace(-2,0.5,1000)

#making a complex numbers grid by hand
Brojevi=[]
for x in range (0,1000):
    for y in range (0,1000):
        Brojevi.append(Realni[x]+Imaginarni[y])


#building a sparse Mandelbrot set
Mandelbrot=[]
num_iterations = 600
N = len(Brojevi)

for Broj in range (0,N):
    z=0
    for Iteracija in range (0, num_iterations):
        
        z=z*z+Brojevi[Broj]
        
        if (abs(z)>2):
            break
            
    if(abs(z)<2):
        Mandelbrot.append(Brojevi[Broj])     


plt.rcParams['figure.figsize'] = [14,10]

fig1=plt.figure(1)
plt.scatter(np.real(Mandelbrot), np.imag(Mandelbrot),s=2,c='black')  
plt.axis([-2,1,-1,1])

plt.axis("off")
plt.show()
