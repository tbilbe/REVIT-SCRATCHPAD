####################
import re
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
#collect the rooms from linked file
roomCol = FilteredElementCollector(sdoc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements() # gives a list
########
#filteredCollector: fCollector is a MEPCurve - duct type
fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
# paraSet = fCollector.Parameters
# for p in paraSet:
#     print(p.Definition.Name.ToString() + ': ' +p.AsValueString().ToString())
#duct dict is duct id, duct start, duct end, will inc. duct centerpoint also
ductObj = {}
ductArr = []

midpointArr = [] # Top level array
iterator = 0
for d in fCollector:
    ductObj[d.Id.ToString()] = 'Duct-'+iterator.ToString()+':ID'
    ductObj[d.Location.Curve.GetEndPoint(0).ToString()] = 'Duct-'+iterator.ToString()+':Startpoint'
    ductObj[d.Location.Curve.GetEndPoint(1).ToString()] = 'Duct-'+iterator.ToString()+':Endpoint'
    ductObj[d.Location.Curve.GetEndPoint(1).ToString()] = 'Duct-'+iterator.ToString()+':Endpoint'
    ductArr.append(ductObj)
    iterator = iterator+1

#compile the reg expression
coords = re.compile(r'-?(\d+.\d*)')
#returns a list of the coords in string format - cast this to int when ready

#midpoint of the curve
for midPoints in fCollector:
    reStart = coords.findall(midPoints.Location.Curve.GetEndPoint(0).ToString())
    reEnd = coords.findall(midPoints.Location.Curve.GetEndPoint(1).ToString())
    #midpoint Array of coordinates - need to use XYZ class
    midpointArrNest = [] # [[200, 300, 400],[18,22,10]]
    midpointArrNest.append(((float(reStart[0]) + float(reEnd[0])) / 2))
    midpointArrNest.append(((float(reStart[1]) + float(reEnd[1])) / 2))
    midpointArrNest.append(((float(reStart[2]) + float(reEnd[2])) / 2))
    midpointArr.append(midpointArrNest)
########
roomArr = []
for room in roomCol:
    # print(room)
    for point in midpointArr:
        #create an XYZ
        print(point)
        pointXYZ = XYZ(point[0], point[1], point[2] - 10) #can take away from the coordinate
        print(pointXYZ)
        # if room.Get
        if room.IsPointInRoom(pointXYZ):#give an XYZ here
        #     #TODO Get room data and put into Duct midpoint info
            print('*****')
            print('Yes')
            print('*****')
            roomName = room.LookupParameter('Name')
            roomNumber = room.LookupParameter('Number')
            
            print('duct is in room')
        #     #open transaction
        #     #submit transaction
        #     #close transaction
        else:
            print('no')
            print('Point: '+pointXYZ.toString()+' is not in '+room.LookupParameter('Name').ToString())    


#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
#iterate over the spaces
for space in spaceCol:
    spaceName = space.LookupParameter('Name')
    spaceNumber = space.LookupParameter('Number')
    spaceVolume = space.LookupParameter('Volume')
    print('Space '+spaceName.Definition.Name.ToString() + ': '+spaceName.AsString() + ' - '+spaceNumber.AsString())




###############
#test
#################


####################
import re
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
#collect the rooms from linked file
roomCol = FilteredElementCollector(sdoc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements() # gives a list
########
#filteredCollector: fCollector is a MEPCurve - duct type
fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
# paraSet = fCollector.Parameters
# for p in paraSet:
#     print(p.Definition.Name.ToString() + ': ' +p.AsValueString().ToString())
#duct dict is duct id, duct start, duct end, will inc. duct centerpoint also
ductObj = {}
ductArr = []

midpointArr = [] # Top level array
iterator = 0
for d in fCollector:
    ductObj[d.Id.ToString()] = 'Duct-'+iterator.ToString()+':ID'
    ductObj[d.Location.Curve.GetEndPoint(0).ToString()] = 'Duct-'+iterator.ToString()+':Startpoint'
    ductObj[d.Location.Curve.GetEndPoint(1).ToString()] = 'Duct-'+iterator.ToString()+':Endpoint'
    ductObj[d.Location.Curve.GetEndPoint(1).ToString()] = 'Duct-'+iterator.ToString()+':Endpoint'
    ductArr.append(ductObj)
    iterator = iterator+1

#compile the reg expression
coords = re.compile(r'-?(\d+.\d*)')
#returns a list of the coords in string format - cast this to int when ready

#midpoint of the curve
for midPoints in fCollector:
    reStart = coords.findall(midPoints.Location.Curve.GetEndPoint(0).ToString())
    reEnd = coords.findall(midPoints.Location.Curve.GetEndPoint(1).ToString())
    #midpoint Array of coordinates - need to use XYZ class
    midpointArrNest = [] # [[200, 300, 400],[18,22,10]]
    midpointArrNest.append(abs((float(reStart[0]) + float(reEnd[0])) / 2))
    midpointArrNest.append(abs((float(reStart[1]) + float(reEnd[1])) / 2))
    midpointArrNest.append((float(reStart[2])
    midpointArr.append(midpointArrNest)
########
for point in midpointArr:
    for room in roomCol:
    # print(room)
    
        #create an XYZ
        # print(type(point))
        pointXYZ = XYZ(point[0], point[1], point[2]) #can take away from the coordinate
        print((pointXYZ))
        
        if room.IsPointInRoom(pointXYZ):#give an XYZ here
        #     #TODO Get room data and put into Duct midpoint info
            print('***************************************************')
            print('Yes')
            print('***************************************************')
            roomName = room.LookupParameter('Name')
            roomNumber = room.LookupParameter('Number')
            print('duct is in room')
        #     #open transaction
        #     #submit transaction
        #     #close transaction
        else:
            r1 = room.LookupParameter('Name')
            r1 = r1.Definition
            print('Point: '+pointXYZ.ToString()' is not in '+r1.ToString())
#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
#iterate over the spaces
for space in spaceCol:
    for p in fCollctor:
        pointXYZ = XYZ(p[0], p[1], p[2]) #can take away from the coordinate
        if space.IsPointInSpace(pointXYZ):
            print('*********************************')
            print('*********************************')
            print('Found Me')
            print('*********************************')
            print('*********************************')
        else:
            print('no')


##########

import re

fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()

coords = re.compile(r'-?(\d+.\d*)')

midpointArr = [] # Top level array

#midpoint of the curve
for midPoints in fCollector:
    midpointArrNest = [] # [[200, 300, 400],[18,22,10]]
    reStart = coords.findall(midPoints.Location.Curve.GetEndPoint(0).ToString())
    reEnd = coords.findall(midPoints.Location.Curve.GetEndPoint(1).ToString())
    midpointArrNest.append(abs((float(reStart[0]) - float(reEnd[0])) / 2))
    midpointArrNest.append(abs((float(reStart[1]) - float(reEnd[1])) / 2))
    midpointArrNest.append((float(reStart[2])))
    midpointArr.append(midpointArrNest)


##################
#filteredCollector: fCollector is a MEPCurve - duct type
fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
#test
#CHECK IF DUCT ENDPOINT(0) AND ENDPOINT(1) IS IN THE SAME ROOM
from Autodesk.Revit.DB import Transaction
##########
duct_roomArr = []
t = Transaction(doc, 'Updating Duct Space Parameters')
t.Start()
for s in spaceCol:
    for ducts in fCollector:
        tempArr = []
        writeParameter = ducts.LookupParameter('Comments')
        if s.IsPointInSpace(ducts.Location.Curve.GetEndPoint(0)) and s.IsPointInSpace(ducts.Location.Curve.GetEndPoint(1)):
            print('Found Me')
            print('duct in single space')
            tempArr.append(s.Number)
            writeParameter.Set(s.Number)
            tempArr.append(ducts)
            duct_roomArr.append(tempArr)
        elif s.IsPointInSpace(ducts.Location.Curve.GetEndPoint(0)) or s.IsPointInSpace(ducts.Location.Curve.GetEndPoint(1)):
            print('*********************************')
            print('*********************************')
            print('Found Me')
            ('duct in two spaces')
            writeParameter.Set('Not in single space')
            print('*********************************')
            print('*********************************')
        else:
            print('no space')
            # writeParameter.Set('Space not found')
t.Commit()

################
#get the path of the link
app = doc.Application
docs = app.Documents
n = docs.Size

# print n, 'open documents:'
for d in docs:
    s = d.PathName
#   print s
    if '_A_' or 'Ar' in s: #HAVE TO CHECK THE ARCH FILE NAME HERE
        sdoc = d
print(sdoc.PathName)
#collect the rooms from linked file
roomCol = FilteredElementCollector(sdoc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements() # gives a list
########
#filteredCollector: fCollector is a MEPCurve - duct type
fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
#test
duct_roomArr = []
t = Transaction(doc, 'Updating Duct Space Parameters')
t.Start()
for r in roomCol:
    for d in fCollector:
        tempArr = []
        writePara = d.LookupParameter('Comments')
        if r.IsPointInRoom(d.Location.Curve.GetEndPoint(0)) and r.IsPointInRoom(d.Location.Curve.GetEndPoint(1)):
            
            writePara.Set(r.Number)
        elif r.IsPointInRoom(d.Location.Curve.GetEndPoint(0)) or r.IsPointInRoom(d.Location.Curve.GetEndPoint(1)):
            writePara.Set(r.Number.ToString() + ' in two rooms.')
        else:
            writePara.Set('No space found') 
t.Commit()

#TODO create a helper function to create mid points for the ducts.
#1 loop over ducts
#2 run midpoint function over each duct - midpoint function returns a point
#3 check point in space
#4 if point in space write space name to duct



def midpoint (duct):
    p1 = duct.Location.Curve.GetEndPoint(0)
    p2 = duct.Location.Curve.GetEndPoint(1)
    midpoint = XYZ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)
    print(midpoint)
    return midpoint


################
#get the path of the link
app = doc.Application
docs = app.Documents
n = docs.Size

# print n, 'open documents:'
for d in docs:
    s = d.PathName
#   print s
    if '_A_' or 'Ar' in s: #HAVE TO CHECK THE ARCH FILE NAME HERE
        sdoc = d
print(sdoc.PathName)

roomCol = FilteredElementCollector(sdoc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements() # gives a list

fCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
#collect the spaces
spaceCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
t = Transaction(doc, 'Updating Duct Space Parameters')
t.Start()
for r in roomCol:
    for d in fCollector:
        
        writePara = d.LookupParameter('Comments')
        if r.IsPointInRoom(midpoint(d)):
            writePara.Set(r.Number)
        elif r.IsPointInRoom(d.Location.Curve.GetEndPoint(0)) or r.IsPointInRoom(d.Location.Curve.GetEndPoint(1)):
            writePara.Set(r.Number.ToString() + ' in two rooms.')
        else:
            writePara.Set('No space found') 
t.Commit()