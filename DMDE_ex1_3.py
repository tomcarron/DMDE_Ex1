'''
DMDE Exercise Sheet 1
'''
import numpy as np
import astropy.units as u
from astropy.cosmology import w0waCDM
from astropy.cosmology import Planck18_arXiv_v2 as Planck18
import matplotlib.pyplot as plt

'''
) For a flat ΛCDM model with Ωm = 0.3 and ΩDE = 0.7, plot (up to z = 1.75) the
luminosity distance dl(z) and the angular diameter distance da (z) for the following two
cases of the dark energy equation of state:
w_de=-1.2+0.2 z/1+z
w_de=-0.8-0.2 z/1+z

Is it easy to distinguish between the models? Comment on what you see in your plot,
and focus especially on the cosmological implications of the shape of da (z).
'''
z=np.linspace(0,1.75,1000)  #z up to 1.75
#w_de=-1.2+0.2 z/1+z
cosmo1=w0waCDM(H0=Planck18.H(0), Om0=0.3, Ode0=0.7, w0=-1.2, wa=0.2)
cosmo2=w0waCDM(H0=Planck18.H(0), Om0=0.3, Ode0=0.7, w0=-0.8, wa=-0.2)
plt.figure(1)
plt.plot(z,cosmo1.luminosity_distance(z),label='$d_l(z)$ for $w=-1.2+0.2(z/1+z)$')
plt.plot(z,cosmo2.luminosity_distance(z),label='$d_l(z)$ for $w=-0.8-0.2(z/1+z)$')
plt.plot(z,cosmo1.angular_diameter_distance(z),linestyle='dashed',label='$d_a(z)$ for $w=-1.2+0.2(z/1+z)$')
plt.plot(z,cosmo2.angular_diameter_distance(z),linestyle='dashed',label='$d_a(z)$ for $w=-0.8-0.2(z/1+z)$')
plt.xlabel('z')
plt.ylabel('Distance (Mpc)')
plt.title('Luminosity distance vs z')
plt.legend()
plt.grid()
plt.savefig('Prob3a.png',dpi=400,bbox_inches='tight')

'''
#It is possible to distinguish between the models, particularly with the luminosity distance, but it is not easy. Precision measurements of the distances of objects as well as large sample size of objects of known distance is needed to distinguish between the models. Interestingly, the angular diameter distanceappears to become constant with the redshift, i.e its angular size does not change as the redshift increases. Two objects with the same proper size, one at a larger distance, may appear the same angular size.

#b) When do we use luminosity distance dl (z) and when do we use angular diameter distance
#da (z)? 

#IDK ask charlie......

#For the same cosmological parameters as you used in 3a, plot the comoving volume V (z)
#for each case. Is it now easier to distinguish between the two dark energy equation of
#state cases? 
'''
plt.figure(2)
plt.plot(z,cosmo1.comoving_volume(z),label='$V(z) for w=-1.2+0.2(z/1+z)$')
plt.plot(z,cosmo2.comoving_volume(z),label='$V(z) for w=-0.8-0.2(z/1+z)$')
plt.xlabel('z')
plt.ylabel('Comoving Volume $(Mpc^3)$')
plt.title('Comoving Volume vs z')
plt.legend()
plt.grid()
plt.savefig('Prob3c.png',dpi=400,bbox_inches='tight')

'''
Yes it is now easier to distinguish between the two dark energy equations of state, the two models diverge from eachother more than in the case of the luminosities.
'''
plt.show()

