import sys
sys.path.append('../starslugs')
from starslugs.star_run import Distance, StarSystem
from starslugs.star_run import print_info_systems
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy

data = pd.read_csv('data/exoplanet_archive_2026_06_22.csv', skiprows=28)

def test_full_distance_calc(data):
    # read in csv data
    test_sys_1 = StarSystem(data, sys_name='51 Eri')
    #test_sys_1.get_row()
    #test_sys_1.get_info()
    #test_sys_1.print_info()

    test_sys_2 = StarSystem(data, sys_name='51 Eri')
    #test_sys_2.get_row()
    #test_sys_2.get_info()
    #test_sys_2.print_info()

    systems_list = [test_sys_1, test_sys_2]
    print_info_systems(systems_list)

    # get physical 3-d distance between system 1 and system 2
    distance_12_obj = Distance(test_sys_1, test_sys_2) # Distance object


    distance_12 = distance_12_obj.distance # distance [pc]
    assert np.isclose(distance_12, 0)

def test_get_info(data):
    star_name = '51 Eri'
    exp_dist = data[data['hostname'] == star_name]['sy_dist']
    test_sys = StarSystem(data, sys_name=star_name)
    test_sys.get_info()
    assert test_sys.distance == exp_dist.iloc[0]

if __name__ == '__main__':
    test_full_distance_calc(data)
    test_get_info(data)