import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy


# read in csv data
data = pd.read_csv('../data/exoplanet_archive_2026_06_22.csv', skiprows=28)


class Distance():
    def __init__(self, system1, system2):

        self.ra1 = system1.ra
        self.ra2 = system2.ra
        self.dec1 = system1.dec
        self.dec2 = system2.dec
        self.d1 = system1.distance
        self.d2 = system2.distance
        self.theta = self.angular_dist()
        self.distance= self.physical_dist()
    
    def angular_dist(self):
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
        
        ra1_rad = np.radians(self.ra1)
        dec1_rad = np.radians(self.dec1)
        ra2_rad = np.radians(self.ra2)
        dec2_rad = np.radians(self.dec2)
        
        a = (np.sin(abs(dec1_rad-dec2_rad)/2))**2
        b = np.cos(dec1_rad)*np.cos(dec2_rad)*((np.sin(abs(ra1_rad-ra2_rad)/2))**2)
        
        theta_rad = 2*np.arcsin(np.sqrt(a+b))
                
        return np.degrees(theta_rad)
    
    def physical_dist(self):
        '''
        Uses the physical and angular distances between 2 objects to calculate (3-D) distance between them with law of cosines.
        Args:
            d1: physical distance to 1st object [pc]
            d2: physical distance to 2nd object [pc]
            theta: angular distance (great circle) between 2 objects on celestial sphere [deg]
        Returns:
            D: physical distance from object 1 to object 2 [pc]
        '''

        D_squared = self.d1**2 + self.d2**2 - 2*self.d1*self.d2*np.cos(self.theta)

        return np.sqrt(D_squared)


class StarSystem():
    def __init__(self, csv_data, sys_name):

        self.csv_data = csv_data # Reading the csv data into a pandas dataframe
        self.sys_name = sys_name # hostname
        self.distance = None # sy_dist
        self.ra =  None # ra
        self.dec = None # dec
        self.star_teff =  None # st_teff
        self.pl_num = None # sy_pnum
        self.star_num = None # sy_snum
        self.get_info()
    
    def clean_data(self) -> pd.DataFrame:
        """
        Clean the data for the system
        """
        mask  = self.csv_data['st_teff'].isna() and self.csv_data['sy_dist'].isna()
        self.csv_data = self.csv_data[~mask]
        return self.csv_data
    
    def get_row(self):
        """
        csv_data: assuming this is already read into a pd dataframe
        """
        self.clean_data()
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


def print_info_systems(systems_list):
    """print_info_systems

    Print the information for two systems

    Args:
        a (array): I'm just testing things
    
    Returns:
        float: Another test
    """
    row_name = []
    for i in range(len(systems_list)):
        row_name.append(systems_list[i].sys_name)
    col_name = ['RA', 'Dec', 'Distance', 'Teff', 'Number of Planets', 'Number of Stars']

    table_data = []
    for i in range(len(systems_list)):
        table_data.append([systems_list[i].ra, systems_list[i].dec, systems_list[i].distance, systems_list[i].star_teff, systems_list[i].pl_num, systems_list[i].star_num])
    
    plt.table(cellText=table_data, rowLabels=row_name, colLabels=col_name, loc='center', cellLoc='center')
    plt.axis('off')
    #my_table.scale(1, 1.5)
    plt.show()
    return


def main():
    """
    Main function
    """
    test_sys_1 = StarSystem(data, sys_name='51 Eri')
    #test_sys_1.get_row()
    #test_sys_1.get_info()
    #test_sys_1.print_info()

    test_sys_2 = StarSystem(data, sys_name='11 Com')
    #test_sys_2.get_row()
    #test_sys_2.get_info()
    #test_sys_2.print_info()

    systems_list = [test_sys_1, test_sys_2]
    print_info_systems(systems_list)

    # get physical 3-d distance between system 1 and system 2
    distance_12_obj = Distance(test_sys_1, test_sys_2) # Distance object
    distance_12 = distance_12_obj.distance # distance [pc]
    print(distance_12)


if __name__ == '__main__':
    main()
