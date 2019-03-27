from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Adds the space name and space number to the BBK_MEP_LOCATION parameter."
__title__ = '''Pipe Fittings\n in Space'''
__author__ = "Tom Bilbe"

SpaceCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MEPSpaces).WhereElementIsNotElementType().ToElements()
fittingsCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeFitting).WhereElementIsNotElementType().ToElements()

def dropPointInRoom (point):
    # Only change z axis height
    belowCeilingReducer = 6 # ft
    lowerZPoint = point[2] - belowCeilingReducer
    inRoomMidpoint = XYZ(point[0], point[1], lowerZPoint)
    return inRoomMidpoint

t = Transaction(doc, 'Duct Fitting - BBKLocation')
t.Start()

for space in SpaceCollector:
	spaceNumber = space.LookupParameter('Number')
	spaceName = space.LookupParameter('Name')
	for pipeFtngs in fittingsCollector:
		pipeFtngsInsertPoint = pipeFtngs.Location.Point
		setBBKLoc = pipeFtngs.LookupParameter('BBK_MEP_LOCATION')
		if space.IsPointInSpace(dropPointInRoom(pipeFtngsInsertPoint)):
			setBBKLoc.Set(str(spaceNumber.AsString()) + ': '+ str(spaceName.AsString()))
				
t.Commit()
