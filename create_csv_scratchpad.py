import clr
import System
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document


t = Transaction(doc, 'Write an external file.')
t.Start()

#Create Require variables
#Collect using filtered element collector
mepCollector = FilteredElementCollector(doc).OfClass(MEPSystem)
listLength = len(list(mepCollector))
totalUnnamed = 0

# percent = round((float(totalUnnamed) / listLength) * 100)
# completeRevitSystems = 100 - percent

#Set the file path
filepath = 'C:\\Users\\tom.bilbe\\Desktop\\Projects\\scripts\\New folder\\OUTPUT_FROM_SCRIPTS\\SystemChecks.txt'
 
#Delete the file if it exists.
if (System.IO.File.Exists(filepath) == True):
    System.IO.File.Delete(filepath)
 
#Create the file
file = System.IO.StreamWriter(filepath)
 
#Write some things to the file
#************
# file.WriteLine('the amount of systems in the Revit Doc: ', listLength)
# file.WriteLine('the amount of systems complete in the Revit Doc: ', completeRevitSystems, '%')
# Iterate over the systems to check for unassigned
#************
#Create object to write into file
dict = []
for s in mepCollector:
    dict.append(s)
    if s.Name == '<unnamed>':
        totalUnnamed = totalUnnamed + 1

#Do the file writing in here
file.WriteLine('length of arr'+len(dict))
file.WriteLine('hello')
file.WriteLine('world')
file.WriteLine(totalUnnamed)
 
#Close the StreamWriter and pyrevit window
file.Close()
t.Commit()
__window__.Close()














###############

mepcol = FilteredElementCollector(doc).OfClass(MEPSystem)
totalUnnamed = 0
for s in mepcol:
	if s.Name == '<unnamed>':
		#print(s.Name)
		totalUnnamed = totalUnnamed + 1
print('total Unnamed systems: ' + str(totalUnnamed))
collectorLength = len(list(mepcol))
percent = round((float(totalUnnamed) / collectorLength) * 100)
print('percentage unreferenced systems: '+ str(totalUnnamed)+ '/' +str(collectorLength)+': '+str(percent)+'%')
