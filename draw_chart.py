import random
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from pyrevit import script
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Create a bar chart of systems by length"
__title__ = "Systems\n by Lengths"
__author__ = "Tom Bilbe"

def getMeSomeColors():
    r = lambda: random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(),r(),r()))


output = script.get_output()
#Create Chart - pie chart
chart = output.make_bar_chart()
# Title and other options
chart.options = {
    'scaleShowValues': True,
    'scales': {
        'yAxes': [{
            'ticks': {'beginAtZero': True}
        }],
        'xAxes':[{
            'ticks': {'autoSkip': False}
        }]
    }
}

chart.options['title'] = {'display': True,
                       'text':'Systems by Length',
                       'fontSize': 25,
                       'fontColor': '#1c3f77'}
chart.set_style('height:500px')

length = 0.0

#Duct Data
ductCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
ductLengthsBySystem = {}
for dlen in ductCollector:
	dl = dlen.LookupParameter('Length')
	ds = dlen.LookupParameter('System Classification')
	if ds.AsString() in ductLengthsBySystem:
		ductLengthsBySystem[ds.AsString()] = float(dl.AsValueString()) + float(ductLengthsBySystem[ds.AsString()])
	elif ds.AsString() not in ductLengthsBySystem:
		ductLengthsBySystem[ds.AsString()] = dl.AsValueString() 
#Pipe Data
pipeCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeCurves).WhereElementIsNotElementType().ToElements()
pipeLengthsBySystem = {}
for pLen in pipeCollector:
    pl = pLen.LookupParameter('Length')
    ps = pLen.LookupParameter('System Classification')
    if ps.AsString() in pipeLengthsBySystem:
        pipeLengthsBySystem[ps.AsString()] = float(pl.AsValueString()) + float(pipeLengthsBySystem[ps.AsString()])
    elif ps.AsString() not in pipeLengthsBySystem:
        pipeLengthsBySystem[ps.AsString()] = pl.AsValueString()
#CableTray Data
cableCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_CableTray).WhereElementIsNotElementType().ToElements()
cableLengthsBySystem = {}
for cLen in cableCollector:
    cl = cLen.LookupParameter('Length')
    cs = cLen.Name
    if cs in cableLengthsBySystem:
        cableLengthsBySystem[cs] = float(cl.AsValueString()) + float(cableLengthsBySystem[cs])
    elif cs not in cableLengthsBySystem:
        cableLengthsBySystem[cs] = cl.AsValueString()



#data for labels
ductLabel = []
for key in ductLengthsBySystem:
    ductLabel.append('Duct System: ' + str(key))
pipeLabel = []
for key in pipeLengthsBySystem:
    pipeLabel.append('Pipe System: '+ str(key))
cableLabel = []
for key in cableLengthsBySystem:
    cableLabel.append('Cable Type: ' + str(key))
#chart.data.lables is for the X - axis
chart.data.labels = ductLabel + pipeLabel + cableLabel

'''
the set*.data list should match the length of the X - axis list
'''

#create dataset for Ducts (dataset A)
setTheLengths = chart.data.new_dataset('Lengths (m)')
for value in ductLengthsBySystem.values():
    setTheLengths.data.append(float(value) / 1000.0)
#create dataset for Pipe (dataset B)
for value in pipeLengthsBySystem.values():
    setTheLengths.data.append(float(value) / 1000.0)
# #create dataset for Pipe (dataset C)
for value in cableLengthsBySystem.values():
    setTheLengths.data.append(float(value) / 1000.0)

#colour -> we have to get the length of dictionary push that many into the array below
bgDuct = []
bgPipe = []
bgCable = []

for color in range(len(ductLengthsBySystem)):
    bgDuct.append(getMeSomeColors())
for color in range(len(pipeLengthsBySystem)):
    bgPipe.append(getMeSomeColors())
for color in range(len(cableLengthsBySystem)):
   bgCable.append(getMeSomeColors())
setTheLengths.backgroundColor = bgDuct + bgPipe + bgCable #programatically set this and push the string into array here
setTheLengths.hoverBackgroundColor = '#5b9bd8'

chart.draw()
