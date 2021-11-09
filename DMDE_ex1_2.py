'''
DMDE Exercise Sheet 1
'''
import numpy as np
import astropy.units as u
from astropy.cosmology import Planck18_arXiv_v2 as cosmo
import matplotlib.pyplot as plt

'''
Problem 2: Deceleration Parameter (5 points)
The deceleration parameter q = − äa / ȧ^2
 (where a is the scale factor) tells us if the expansion of
the Universe is decelerated (ä < 0 =⇒ q > 0) or accelerated (ä > 0 =⇒ q < 0). For a flat
ΛCDM universe, we know q(z)=
'''
'''
a) What is the value of q(z) at the present time (z=0)?
'''
def q(z):
	y=0.5*cosmo.Om(z) - cosmo.Ode(z)
	return y
	
print('present value of q(z), q(0):', q(0))

#b) Plot q as a function of z

z=np.linspace(1e-2,1100,10000) #Redshifts

plt.figure(1)
plt.semilogx(z,q(z),label='q(z)',color='blue')
plt.title('q vs z')
plt.xlabel('z')
plt.ylabel('q')
plt.grid()
plt.legend()
plt.savefig('prob2b.png',dpi=300,bbox_inches='tight')

'''
Base on the plot, at which redshift does the accelerated expansion of the Universe begin?
Compare your result to what you found in Exercise
1b. Which comes first, dark energy domination or accelerated expansion?
'''
#accelerated expansion of the Universe begins, when q0=0, i.e when q0 goes from positive to negative. According to the plot this occurs at z=0.6.
#accelerated expansion of the Universe(z~0.6) occurs before Dark Energy domination(z~0.3).

plt.show()





