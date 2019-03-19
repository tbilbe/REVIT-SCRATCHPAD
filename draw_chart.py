#TODO programatically add more colors to list as more systems are added

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from pyrevit import script
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Create a pie chart of ratio of systems by length"
__title__ = "Duct System\n by Lengths"
__author__ = "Tom Bilbe"


from pyrevit import script
output = script.get_output()
#Create Chart - pie chart
chart = output.make_pie_chart()
# Title and other options
chart.options.title = {'display': True,
                       'text':'Duct Systems by Length',
                       'fontSize': 18,
                       'fontColor': '#000',
                       'fontStyle': 'bold'}
                       
chart.set_style('height:150px')

chart.data.labels = [] #Labels go at the top of the chart
length = 0.0

#DATA
ductCol = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
dLengthsBySystem = {}
for len in ductCol:
	dl = len.LookupParameter('Length')
	ds = len.LookupParameter('System Classification')
	if ds.AsString() in dLengthsBySystem:
		dLengthsBySystem[ds.AsString()] = float(dl.AsValueString()) + float(dLengthsBySystem[ds.AsString()])
	elif ds.AsString() not in dLengthsBySystem:
		dLengthsBySystem[ds.AsString()] = dl.AsValueString()

#data for labals
for key in dLengthsBySystem:
    chart.data.labels.append(key)

#create data set - piechart
setthe = chart.data.new_dataset('Duct Lengths')
for value in dLengthsBySystem.values():
    setthe.data.append(value)
#colour
setthe.backgroundColor = ["#1F6CB0", "#560764"]


chart.draw()
