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

#Create two empty dictionary objects
date_dict={}
coord_dict={}

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
    #if Lc is not 1, 2, or 3
    #if obs_lc not in ("1", "2", "3"):
        #continue
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    # Print the location of Sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}:{obs_long} on {obs_date}")
#Adding items to the dictionary if lc is 1, 2, or 3
if obs_lc in ("1", "2", "3") :
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}:{obs_long} on {obs_date}")
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat,obs_long)