import random
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from rpw.ui.forms import (SelectFromList, FlexForm, Label, ComboBox, TextBox, CheckBox, Separator, Button, Alert)
from pyrevit import revit, UI, DB, script
from pyrevit.forms import utils
from pyrevit.forms import toaster
doc = __revit__.ActiveUIDocument.Document

__doc__ = "Multi Select window will popup for operatinos on different categories."
__title__ = '''Multiple\n Selector Tool'''
__author__ = "Tom Bilbe"

def getMeSomeColors():
    r = lambda: random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(),r(),r()))

output = script.get_output()
#Create Chart - bar chart
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
pipeLabel = []
cableLabel = []
bgDuct = []
bgPipe = []
bgCable = []
#chart.data.lables is for the X - axis
chart.data.labels = ductLabel + pipeLabel + cableLabel

# value = SelectFromList('Choose an Element Type', {
#     'Dampers':ElementId(-2008016), 
#     'Air Terminals':ElementId(-2008013),
#     'Mechanical Equipment':ElementId(-2001140)})

components = [CheckBox('Vent', 'Ventilation'),
                CheckBox('Pipe', 'Pipework'),
                CheckBox('Cable', 'Cable Tray'),
                Separator(),
                Button('Smash')]

setTheLengths = chart.data.new_dataset('Lengths (m)')

form = FlexForm('Choose MEP System Type for Chart', components)
form.show() #form.values = {'pipe':true}
# valuesToStrings = form.values
if form.values:
    if form.values['Pipe'] == True:
        for key in pipeLengthsBySystem:
            pipeLabel.append('Pipe System: '+ str(key))
        for value in pipeLengthsBySystem.values():
            setTheLengths.data.append(float(value) / 1000.0)
        for color in range(len(pipeLengthsBySystem)):
            bgPipe.append(getMeSomeColors())
    if form.values['Vent'] == True:
        for key in ductLengthsBySystem:
            ductLabel.append('Duct System: ' + str(key))
        for value in ductLengthsBySystem.values():
            setTheLengths.data.append(float(value) / 1000.0)
        for color in range(len(ductLengthsBySystem)):
            bgDuct.append(getMeSomeColors())
    if form.values['Cable'] ==True:
        for key in cableLengthsBySystem:
            cableLabel.append('Cable Type: ' + str(key))
        for value in cableLengthsBySystem.values():
            setTheLengths.data.append(float(value) / 1000.0)
        for color in range(len(cableLengthsBySystem)):
            bgCable.append(getMeSomeColors())

setTheLengths.backgroundColor = bgDuct + bgPipe + bgCable #programatically set this and push the string into array here
setTheLengths.hoverBackgroundColor = '#5b9bd8'

#chart.data.lables is for the X - axis
chart.data.labels = ductLabel + pipeLabel + cableLabel

chart.draw()
# alert = Alert('selections', title="Selection Test 🤖", header=str(valuesToStrings))
# collector = FilteredElementCollector(doc).OfCategoryId((value)).WhereElementIsNotElementType().ToElements()
