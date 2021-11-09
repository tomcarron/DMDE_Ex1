'''
DMDE Exercise Sheet 1
'''
import numpy as np
import astropy.units as u
from astropy.cosmology import Planck18_arXiv_v2 as Planck18
from astropy.cosmology import w0waCDM
import matplotlib
import matplotlib.pyplot as plt
import astropy.constants as const
import scipy.integrate


'''
Problem 4: Recession Velocity (3 points)
Using Ωm = 0.3 and ΩDE = 0.7, plot the recession velocity vrec (z) for wDE = −1.3 and
wDE = −0.7. What happens for z ' 1.5?
'''
z=np.linspace(0,3,100)
cosmo1=w0waCDM(H0=Planck18.H(0), Om0=0.3, Ode0=0.7, w0=-1.3, wa=0.0)
cosmo2=w0waCDM(H0=Planck18.H(0), Om0=0.3, Ode0=0.7, w0=-0.7, wa=0.0)

def integrand(x,z,w):
	y=((Planck18.Ogamma(0)*(1+x)**4)+(Planck18.Om(0)*(1+x)**3)+(Planck18.Ode(0)*(1+x)**(3*(1+w))))**(-0.5)
	return y


def recession_velocity(z,w):
	#v_rec(z) = c * int[0,z] 1/E(z') dz'
	#integrand=((Planck18.Ogamma(z)*(1+x)**4)+(Planck18.Om(z)*(1+x)**3)+(Planck18.Ode(z)*(1+x)**(3*(1+w))))**(-0.5)
	c=const.c.to('m/s').value
	result,err=(scipy.integrate.quad(integrand,0,z,args=(z,w)))
	y=abs(c*result)
	return y
	
	
velocities_1=[]
velocities_2=[]
redshift=[]
for i in range(len(z)):
	zed=z[i]
	redshift.append(zed)
	velocities_1.append(recession_velocity(zed,cosmo1.w0))
	velocities_2.append(recession_velocity(zed,cosmo2.w0))
	

	
	

plt.figure(1)
plt.plot(redshift,velocities_1,label='w=-1.3')
plt.plot(redshift,velocities_2,label='w=-0.7')
plt.xlabel('z')
plt.ylabel('Recession velocity')
plt.title('Recession velocity vs z')
plt.legend()
plt.grid()
plt.savefig('Prob4.png',dpi=400,bbox_inches='tight')

plt.show()
