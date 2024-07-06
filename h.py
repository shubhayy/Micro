
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import Table

# Assuming your data is in a file called 'microlensing_data.ipac'
# Replace the filename with your actual data file

# # Read the data
# data = ascii.read(filename)

# # Plot the light curve
# plt.figure(figsize=(10, 6))
# plt.errorbar(data['HJD'], data['RELATIVE_MAGNITUDE'], yerr=data['MAGNITUDE_UNCERTAINTY'], fmt='o', label='Flux')

# plt.xlabel('Heliocentric Julian Date (HJD)')
# plt.ylabel('Flux')
# plt.title('Microlensing Light Curve')
# plt.legend()
# plt.grid(True)
# plt.show()
 
# iterate over files in
# that directory

import os
import re

dir = 'NASA_Exodata'
star_id_pattern = re.compile(r'STAR_ID\s*=\s*"(.*)"' )

ids = []

paths = ['MOA 2009-BLG-387L', 'MOA 2010-BLG-477L',  'MOA 2010-BLG-073L', 
 'MOA 2009-BLG-266L',   'MOA 2007-BLG-192L', 'MOA-bin-001L',  
 'MOA 2011-BLG-293L',  'MOA 2008-BLG-310L',  'MOA 2011-BLG-262L', 'MOA 2009-BLG-319L', 
 'MOA 2011-BLG-322L', 'MOA 2011-BLG-028L', 'MOA 2008-BLG-379L',
  'MOA 2007-BLG-400L']

filepathss = []

for filename in os.listdir(dir):
    filepath = os.path.join(dir, filename)
    with open(filepath, 'r') as file:
        content = file.read()
        star_id_match = star_id_pattern.search(content)
        if star_id_match:
            star_id = star_id_match.group(1)
            if star_id not in paths:
                pass
        else:
            filepathss.append(filepath)
            

print(filepathss)


['NASA_Exodata/MICROLENSING.log', 'NASA_Exodata/UID_0302569_PLC_002.tbl', 'NASA_Exodata/UID_0302569_PLC_003.tbl', 'NASA_Exodata/UID_0302569_PLC_001.tbl', 
 'NASA_Exodata/UID_0302569_PLC_004.tbl', 'NASA_Exodata/UID_0302569_PLC_005.tbl', 'NASA_Exodata/UID_0302569_PLC_007.tbl', 
 'NASA_Exodata/UID_0302569_PLC_006.tbl', 'NASA_Exodata/UID_0302569_PLC_008.tbl', 'NASA_Exodata/UID_0302518_PLC_014.tbl']