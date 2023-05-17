import os
import subprocess

# Get the current working directory
current_directory = os.getcwd()

# Change directory command
change_directory_cmd = f'cd /d {current_directory}'

# Run the change directory command
subprocess.run(change_directory_cmd, shell=True)

# Command to create KML file using Exiftool
exiftool_cmd = 'exiftool -E -p kml.fmt Images > test.kml'

# Run the Exiftool command to create the KML file
subprocess.run(exiftool_cmd, shell=True)

# Command to extract GPS coordinates using Exiftool
extract_coordinates_cmd  = 'exiftool -T -c "%.6f" -p ${filepath};${GPSLatitude};${GPSLongitude};${GPSAltitude} Images > coordinates.csv'
# Run the command to extract GPS coordinates and save them to a text file
subprocess.run(extract_coordinates_cmd, shell=True)