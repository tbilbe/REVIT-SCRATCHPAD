#Script returns Green light if the room and MEP space data is aligned.
#TODO create alert output for user
#Write info to file


#get the path of the link
app = doc.Application
docs = app.Documents
n = docs.Size

# print n, 'open documents:'
for d in docs:
    s = d.PathName
#   print s
    if '_A_' in s: #HAVE TO CHECK THE ARCH FILE NAME HERE
        sdoc = d
print(sdoc.PathName)
#collect the rooms from linked file *PASS IN sdoc TO THE filElCol()PARAM
roomCol = FilteredElementCollector(sdoc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements() # gives a list
########
#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
