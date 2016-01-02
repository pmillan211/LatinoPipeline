# Adding Patty's python script directory to Windows' environmental variables 
import sys
sys.path.append('C:/Users/MillPa04/Documents/Python Scripts/')

# Importing Patty's python module
import toolbox

# Front end file path
sFrontEndDirPath = 'C:/Users/MillPa04/Documents/Python Scripts/'
sFrontEndFileName = 'MyWebSite.html'

# Temporary User Data Base
#profile1 = '{name:name1,experience:{},education:{}}'
profile1 = '{"NAME":"name1","EXPERIENCE":"experience1","EDUCATION":"education1"}'
profile2 = '{"NAME":"name2","EXPERIENCE":"experience2","EDUCATION":"education2"}'
profile3 = '{"NAME":"name3","EXPERIENCE":"experience3","EDUCATION":"education3"}'

# Populate Data Base
ProfileDB = []
ProfileDB.append(profile1)
ProfileDB.append(profile2)
ProfileDB.append(profile3)

# Test DB
toolbox.updateFrontEnd(sFrontEndDirPath + sFrontEndFileName, ProfileDB[2])

