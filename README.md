# REVIT-ScratchPad
## Info
These code snippets can be ran inside the python ide in an active Revit project.
I will be adding more and more scripts as ideas come to me.

The main focus of this scratchpad is to test out and develop proof of concepts.

# TODODs!

- [x] Duct length and Ductwork Surface Area Calculator
- [x] Duct Location - Apply room name, room number to ductwork.
- [ ] Cable tray location and Length calcs
- [ ] Pipework location and lengths
- [ ] Create MEP System analytics
     - [x] Captured how to generate system assignment - All MEP systems
     - [ ] Break systems down into MEP classes - Duct/ Air : Pipe/Liquid fluid : CableTray/ Elec
     - [ ] Capture all plant not assigned to MEP System - Number of items, analysis of which system is worse (Elec / Mech)
- [x] Room and Space name application
- [ ] Create possible d3 visualisations of all this data collection?
     - [x] Understand how to transact and with document and create file.writeStream()
     - [x] Create a file either .txt or .csv as direct export from Revit document
     - [ ] Use export to create visualisations to avoid imports into Revit Python Wrapper
