'''
DMDE Exercise Sheet 1
'''
import numpy as np
import astropy.units as u
from astropy.cosmology import Planck18_arXiv_v2 as cosmo
import matplotlib.pyplot as plt

'''
Problem 1 a) Using the best-fit values of the present day cosmological parameters given by the Planck
Collaboration (2018), plot Ωr , Ωm , and ΩΛ as a function of redshift z. Assume a flat
ΛCDM model, and state which Planck results you used. 
'''
#Current values of cosmological parameters
H0=cosmo.H(0)
Om0=cosmo.Om(0)
Olambda0=cosmo.Ode(0)
Or0=cosmo.Ogamma(0)
print('H0:',H0),print('Om0:',Om0),print('Olambda0:',Olambda0),print('Or0:',Or0)



z=np.linspace(1e-2,1100,10000) #Redshifts

#Plotting density parameters as function of z
plt.figure(1)
plt.semilogx(z,cosmo.Ogamma(z),label='$\Omega_{\gamma}(z)$',color='green')
plt.semilogx(z,cosmo.Om(z),label='$\Omega_{m}(z)$',color='blue')
plt.semilogx(z,cosmo.Ode(z),label='$\Omega_{\Lambda}(z)$',color='red')
plt.title('$\Omega$ vs z for Flat $\Lambda$CDM Universe')
plt.xlabel('z')
plt.ylabel('$\Omega$')
plt.grid()
plt.legend()
plt.savefig('prob1a.png',dpi=300,bbox_inches='tight')


#b) z=0.3
#Age of the universe at z=0.3
print('Age of the Universe at z=0.3:', cosmo.age(0.3))

#c) Consider two cases for the equation of state of Dark energy: w=-1.3, w(z)=-1+0.3(z/1+z)
#What are the dark energy domination epochs for these two cases, how does this compare to the w=-1 case.

from astropy.cosmology import w0wzCDM

cosmo_w = w0wzCDM(H0=cosmo.H(0), Om0=cosmo.Om(0), Ode0=cosmo.Ode(0), w0=-1.3, wz=0.0)

plt.figure(2)
plt.semilogx(z,cosmo_w.Ogamma(z),label='$\Omega_{\gamma}(z)$',color='green')
plt.semilogx(z,cosmo_w.Om(z),label='$\Omega_{m}(z)$',color='blue')
plt.semilogx(z,cosmo_w.Ode(z),label='$\Omega_{\Lambda}(z)$',color='red')
plt.title('$\Omega$ vs z for w=-1.3')
plt.xlabel('z')
plt.ylabel('$\Omega$')
plt.grid()
plt.legend()
plt.savefig('prob1c1.png',dpi=300,bbox_inches='tight')


#For w=-1.3, dark energy begins to dominate at z=0.1
print('Age of the Universe at z=0.1:', cosmo_w.age(0.1))

from astropy.cosmology import w0waCDM
cosmo_w2 = w0waCDM(H0=cosmo.H(0), Om0=cosmo.Om(0), Ode0=cosmo.Ode(0), w0=-1.0, wa=0.3)

plt.figure(3)
plt.semilogx(z,cosmo_w2.Ogamma(z),label='$\Omega_{\gamma}(z)$',color='green')
plt.semilogx(z,cosmo_w2.Om(z),label='$\Omega_{m}(z)$',color='blue')
plt.semilogx(z,cosmo_w2.Ode(z),label='$\Omega_{\Lambda}(z)$',color='red')
plt.title('$\Omega$ vs z for w=-1.3+0.3(z/1+z)')
plt.xlabel('z')
plt.ylabel('$\Omega$')
plt.grid()
plt.legend()
plt.savefig('prob1c2.png',dpi=300,bbox_inches='tight')


#For w=-1.0+0.3(z/1+z), dark energy begins to dominate at z=0.2
print('Age of the Universe at z=0.2:', cosmo_w2.age(0.2))
plt.show()

#How does this compare with the w=-1 case? In both cases, DarkENergy comes to dominate a lower redshift i.e later in the universe.






	
	
	
	
	
	
	
	
	

