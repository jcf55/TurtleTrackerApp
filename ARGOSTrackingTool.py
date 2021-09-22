#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Jackie Fahrenholz (jcf55@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file- because we've already opened and read it
file_object.close()

#Iterate through all lines in the linelist
#lineString = line_list[100] this is replaced by the below line
for lineString in line_list[17:]:
    if lineString[0] == "#" or lineString[0] == "u": continue
 # can write this as if lineString[0] in ("#", "u") : continue   

    #split the string into a list of data items
    lineData = lineString.split()
    
    #extract item and list them into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    
    #location class
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    # Print the location of Sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}:{obs_long} on {obs_date}")