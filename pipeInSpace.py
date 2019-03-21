from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Adds the space name and space number to the BBK_MEP_LOCATION parameter."
__title__ = '''Pipe\n in Space'''
__author__ = "Tom Bilbe"

SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
pipeCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeCurves).WhereElementIsNotElementType().ToElements()

def midpoint (mepObj):
    p1 = mepObj.Location.Curve.GetEndPoint(0)
    p2 = mepObj.Location.Curve.GetEndPoint(1)
    midpoint = XYZ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2)
    #print(midpoint)
    return midpoint # Returns (xx.abc, yy.def, zz.ghi)

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

def wholeDuctInRoom (space, mepObj):
    p1 = mepObj.Location.Curve.GetEndPoint(0)
    p2 = mepObj.Location.Curve.GetEndPoint(1)
    inRoomPoint1 = dropPointInRoom(p1)
    inRoomPoint2 = dropPointInRoom(p2)
    if space.IsPointInSpace(inRoomPoint1) and space.IsPointInSpace(inRoomPoint2):
        return True
    else:
        return False

t = Transaction(doc, 'Pipe in Space naming')
t.Start()

for space in SpaceCollector:
    spaceNumber = space.LookupParameter('Number')
    spaceName = space.LookupParameter('Name')
    for pipe in pipeCollector:
        setBBKLocation = pipe.LookupParameter('BBK_MEP_LOCATION')
        if setBBKLocation.AsString() == '':
            if pipe.LevelOffset > 6:
            a = space.IsPointInSpace(dropPointInRoom(midpoint(pipe)))
            b = wholeDuctInRoom(space, pipe)
            if a and b:
                setBBKLocation.Set(spaceNumber.AsString())
            if a and not b:
                setBBKLocation.Set(str(spaceNumber.AsString()) + ': Pipe in two spaces')
t.Commit()
