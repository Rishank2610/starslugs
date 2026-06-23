import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def angular_dist(ra1, dec1, ra2, dec2):
     '''
     Calculates the angular distance (great circle portion) between 2 RA/Dec coordinate pairs inside celestial sphere.
     Args:
        ra1: RA of 1st object [deg.]
        dec1: Dec of 1st object [deg.]
        ra2: RA of 2nd object [deg.]
        dec2: RA of 2nd object [deg.]
     Output:
        theta: angular distance between 2 objects [deg.]
     '''
     
     ra1 = np.radians(ra1)
     dec1 = np.radians(dec1)
     ra2 = np.radians(ra2)
     dec2 = np.radians(dec2)
     
     a = (np.sin(abs(dec1-dec2)/2))**2
     b = np.cos(dec1)*np.cos(dec2)*((np.sin(abs(ra1-ra2)/2))**2)
     theta = 2*np.arcsin(np.sqrt(a+b))
     
     theta = np.degrees(theta)
     
     return theta


def physical_dist(d1, d2, theta):
    '''
    Uses the physical and angular distances between 2 objects to calculate (3-D) distance between them with law of cosines.
    Args:
        d1: physical distance to 1st object [pc]
        d2: physical distance to 2nd object [pc]
        theta: angular distance (great circle) between 2 objects on celestial sphere [deg]
    Returns:
        D: physical distance from object 1 to object 2 [pc]
    '''

    D_squared = d1**2 + d2**2 - 2*d1*d2*np.cos(theta)

    return np.sqrt(D_squared)






# read in csv data
data = pd.read_csv('exoplanet_archive_2026_06_22.csv', skiprows=28)


class StarSystem():
    def __init__(self, csv_data, sys_name):

        self.csv_data = csv_data

        self.sys_name = sys_name # hostname
        self.distance = None # sy_dist
        self.ra =  None # ra
        self.dec = None # dec
        self.star_teff =  None # st_teff
        self.pl_num = None # sy_pnum
        self_star_num = None # sy_snum
    
    def get_row(self):
        """
        csv_data: assuming this is already read into a pd dataframe
        """

        obj_rows = self.csv_data[self.csv_data['hostname']== self.sys_name]

        if len(obj_rows) > 1:
            obj_rows = obj_rows.iloc[0]

        print('distance = '+str(obj_rows['sy_dist']))

        return


test_sys = StarSystem(data, sys_name='11 Com')
test_sys.get_row()