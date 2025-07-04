import numpy as np
import matplotlib.pyplot as plt

def recaman(N,i=1,t=0,c=0): #making N recaman terms
    while (i<N+1):
        if t-i > 0 and a.count(t-i) == 0:
            a.append(t-i)
            c=t-i   
        else:
            a.append(t+i)
            c=t+i
        t=c
        i+=1

if __name__=="__main__":

    a=[0]
    N=100
    recaman (N)

    plt.rcParams['figure.figsize'] = [6,30]
    i=0
    while(i<N):
        h=abs((a[i+1]-a[i]))
        if a[i+1]>a[i]:
            fi=np.linspace(0,((-1)**i)*np.pi,201)
            plt.plot(h*np.sin(fi),((h*np.cos(fi)+h)/2)+a[i])
        else: 
            fi=np.linspace(0,((-1)**i)*np.pi,201)
            plt.plot(h*np.sin(fi),((h*np.cos(fi)+h)/2)+a[i+1])     
        i+=1
        
    plt.axis("off")
    plt.show()