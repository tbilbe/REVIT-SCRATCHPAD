SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
fittingsCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctFitting).WhereElementIsNotElementType().ToElements()

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

t = Transaction(doc, 'Duct Fitting - BBKLocation')
t.Start()

for space in SpaceCollector:
	for ductFtngs in fittingsCollector:
		ductFtngsInsertPoint = ductFtngs.Location.Point
		setBBKLoc = ductFtngs.LookupParameter('BBK_MEP_LOCATION')
		if setBBKLoc.AsString() == None:
			if space.IsPointInSpace(dropPointInRoom(ductFtngsInsertPoint)):
				spaceNumber = space.LookupParameter('Number')
				spaceName = space.LookupParameter('Name')
				setBBKLoc.Set(str(spaceNumber.AsString()) + ': '+ str(spaceName.AsString()))
				
t.Commit()
__window__.Close()
