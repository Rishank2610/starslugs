import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy


# read in csv data
data = pd.read_csv('exoplanet_archive_2026_06_22.csv', skiprows=28)

class StarSystem():
    def __init__(self, csv_data, sys_name):

        self.csv_data = csv_data # Reading the csv data into a pandas dataframe
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

        obj_rows = self.csv_data[self.csv_data['hostname'] == self.sys_name] # Getting the row for the system

        if len(obj_rows) > 1:
            obj_rows = obj_rows.iloc[0]

        #print('distance = '+str(obj_rows['sy_dist']))
        return obj_rows
    
    def get_info(self):
        """
        Get the information for the system
        """
        obj = self.get_row()
        self.distance = obj['sy_dist']
        self.ra = obj['ra']
        self.dec = obj['dec']
        self.star_teff = obj['st_teff']
        self.pl_num = obj['sy_pnum']
        self.star_num = obj['sy_snum']

        return
    
    def print_info(self):
        """
        Print the information for the system
        """
        
        row_name = [self.sys_name]
        col_name = ['RA', 'Dec', 'Distance', 'Teff', 'Number of Planets', 'Number of Stars']
        table_data = [[self.ra, self.dec, self.distance, self.star_teff, self.pl_num, self.star_num]]
        my_table = plt.table(cellText=table_data, rowLabels=row_name, colLabels=col_name, loc='center', cellLoc='center')
        plt.axis('off')
        # Increase cell size (width factor, height factor)
        my_table.scale(1, 1.5)

        plt.show()

        return

test_sys = StarSystem(data, sys_name='11 Com')
test_sys.get_row()
test_sys.get_info()
test_sys.print_info()