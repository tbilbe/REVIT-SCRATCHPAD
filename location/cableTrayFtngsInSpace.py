from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Adds the space name and space number to the BBK_MEP_LOCATION parameter."
__title__ = '''Cable Fittings\n in Space'''
__author__ = "Tom Bilbe"

SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
fittingsCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_CableTrayFitting).WhereElementIsNotElementType().ToElements()

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

t = Transaction(doc, 'Cable Fittings in Space')
t.Start()

for space in SpaceCollector:
    spaceNumber = space.LookupParameter('Number')
    spaceName = space.LookupParameter('Name')
    for cTrayFtngs in fittingsCollector:
        cTrayFtngsInsertPoint = cTrayFtngs.Location.Point
        setBBKLoc = cTrayFtngs.LookupParameter('BBK_MEP_LOCATION')
        if space.IsPointInSpace(dropPointInRoom(cTrayFtngsInsertPoint)):
            setBBKLoc.Set(str(spaceNumber.AsString())+': '+str(spaceName.AsString()))

t.Commit()
