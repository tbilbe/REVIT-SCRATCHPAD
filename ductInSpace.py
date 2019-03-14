SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
ductCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()

def midpoint (duct):
    p1 = duct.Location.Curve.GetEndPoint(0)
    p2 = duct.Location.Curve.GetEndPoint(1)
    midpoint = XYZ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)
    #print(midpoint)
    return midpoint # Returns (xx.abc, yy.def, zz.ghi)

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

def wholeDuctInRoom (space, duct):
    p1 = duct.Location.Curve.GetEndPoint(0)
    p2 = duct.Location.Curve.GetEndPoint(1)
    inRoomPoint1 = dropPointInRoom(p1)
    inRoomPoint2 = dropPointInRoom(p2)
    if space.IsPointInSpace(inRoomPoint1) and space.IsPointInSpace(inRoomPoint2):
        return True
    else:
        return False

t = Transaction(doc, 'Lets fucking do this again')
t.Start()

for space in SpaceCollector:
	for duct in ductCollector:
		if setBBKLoc.AsString() == None:
        if space.IsPointInSpace(dropPointInRoom(midpoint(duct))) and wholeDuctInRoom(space, duct):
			spaceNumber = space.LookupParameter('Number')
			spaceName = space.LookupParameter('Name')
			setBBKLoc = duct.LookupParameter('BBK_MEP_LOCATION')
			setBBKLoc.Set(spaceName.AsString())
		if space.IsPointInSpace(dropPointInRoom(midpoint(duct))) and not wholeDuctInRoom(space, duct):
			spaceNumber = space.LookupParameter('Number')
			spaceName = space.LookupParameter('Name')
			setBBKLoc = duct.LookupParameter('BBK_MEP_LOCATION')
			setBBKLoc.Set(str(spaceNumber.AsString()) + ': Duct in two spaces')

t.Commit()
