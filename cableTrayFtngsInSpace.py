SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
fittingsCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_CableTrayFitting).WhereElementIsNotElementType().ToElements()

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

t = Transaction(doc, 'Lets fucking do this again')
t.Start()

for space in SpaceCollector:
    for cTrayFtngs in fittingsCollector:
        cTrayFtngsInsertPoint = cTrayFtngs.Location.Point
        if setBBKLoc.AsString() == None:
            if space.IsPointInSpace(dropPointInRoom(cTrayFtngsInsertPoint)):
                spaceNumber = space.LookupParameter('Number')
                spaceName = space.LookupParameter('Name')
                setBBKLoc = cTray.LookupParameter('BBK_MEP_LOCATION')
                setBBKLoc.Set(spaceNumber.AsString())

t.Commit()
