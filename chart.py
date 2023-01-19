#---- utworzenie termu "sredni" zmiennej
#---- lingwistycznej "wzrost"
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from simulation import symulation

def temp_control(temper, oczek):
    temp=np.zeros((4,80))
    for i in range(0,80):
        x=i
        temp[0,i]=x-20

        if x>=(oczek-3+20) and x<=(oczek-1+20):
            niska=((oczek-1+20)-x)/((oczek-1+20)-(oczek-3+20))
        elif x < (oczek-3+20):
            niska=1
        else:
            niska=0

        if x>=(oczek-3+20) and x<=(oczek-1+20):
            srednia=(x-(oczek-3+20))/((oczek-1+20)-(oczek-3+20))
        elif x>(oczek-1+20) and x<(oczek+1+20): # 22 - 24
            srednia=1
        elif x>=(oczek+1+20) and x<=(oczek+4+20):
            srednia=((oczek+4+20)-x)/((oczek+4+20)-(oczek+1+20))
        else:
            srednia=0       

        if x>=(oczek+1+20) and x<=(oczek+4+20):
            wysoka=(x-(oczek+1+20))/((oczek+4+20)-(oczek+1+20))
        elif x<(oczek+1+20):
            wysoka=0
        else:
            wysoka=1
        temp[1,i] = srednia
        temp[2,i] = niska
        temp[3,i] = wysoka

    # wnioskowanie
    temperatura = temper
    u_niska = temp[2,temperatura+20]
    u_srednia = temp[1,temperatura+20]
    u_wysoka = temp[3,temperatura+20]
    
    ogrzewanie = 0
    klimatyzacja = 0


    print(f"u_niska: {u_niska}")
    print(f"u_srednia: {u_srednia}")
    print(f"u_wysoka: {u_wysoka}")

    if u_niska > 0.4:
        ogrzewanie = 3
    elif u_niska <= 0.4 and u_srednia < 0.4 and u_wysoka == 0:
        ogrzewanie = 2
    elif u_niska == 0 and (u_srednia > 0.4 and u_srednia < 1):
        ogrzewanie = 1
    elif u_srednia == 1 and u_niska == 0 and u_wysoka == 0:
        ogrzewanie = 0
        klimatyzacja = 0
    elif (u_srednia < 1 and u_srednia > 0.5) and u_wysoka < 0.5:
        klimatyzacja = 1
    elif u_srednia < 0.5 and (u_wysoka > 0.5 and u_wysoka < 1):
        klimatyzacja = 2
    elif u_wysoka == 1 and u_srednia == 0 and u_niska == 0:
        klimatyzacja = 3

    """
    symulacja działania programu
    """
    temperatura = symulation(temperatura, ogrzewanie, klimatyzacja)


    #---- graficzna prezentacja termu "srednia"
    plt.plot(temp[0,:],temp[1,:],'r')
    plt.plot(temp[0,:],temp[2,:],'b')
    plt.plot(temp[0,:],temp[3,:],'g')
    plt.axis([-20,59,0,1.2])
    plt.xlabel('temp [°C]')
    plt.ylabel('u(temp)')

    #plt.show()

    print(oczek)
    
    return [ogrzewanie, klimatyzacja]

    