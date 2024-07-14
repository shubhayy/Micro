import os
from pysis import PySIS

def process_pysis_files(directory):
    # Initialize pySIS
    pysis = PySIS()

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an infrared light curve (ending with '_I.pysis')
        if filename.endswith('_I.pysis'):
            # Construct the full file path
            filepath = os.path.join(directory, filename)
            
            try:
                # Read the light curve data
                light_curve_data = pysis.read(filepath)
                
                # Assume light_curve_data contains magnitudes
                # Process the light curve data (example methods)
                light_curve_data.remove_outliers()
                light_curve_data.normalize()
                
                # Extract features for machine learning
                features = light_curve_data.extract_features()

                # Print the processed data and features (or save them)
                print(f'Processed data for {filename}:')
                print(light_curve_data)
                print(f'Extracted features for {filename}:')
                print(features)
                
            except Exception as e:
                print(f'Error processing {filename}: {e}')

    print("Processing complete.")

# Define the directory containing the .pysis files
pysis_directory = 'Exodata/LightCurves/KMT/2016/blg-0212'

# Process .pysis files and extract light curves
process_pysis_files(pysis_directory)


