import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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