# REVIT-ScratchPad :star:
## Info
These code snippets can be ran inside the python ide in an active Revit project. :snake:
I will be adding more and more scripts as ideas come to me.

The main focus of this scratchpad is to test out and develop proof of concepts.

# TODOs! 

- [ ] *CREATE BUTTONS ON RIBBON FOR DISTRIBUTION READY CODE*
- [x] Duct length and Ductwork Surface Area Calculator :boom:
- [x] Duct Location - Apply room name, room number to ductwork. :boom:
- [ ] Cable tray location and Length calcs
- [ ] Pipework location and lengths
- [ ] Create MEP System analytics
     - [x] Captured how to generate system assignment - All MEP systems :octocat:
     - [ ] Break systems down into MEP classes - Duct/ Air : Pipe/Liquid fluid : CableTray/ Elec
     - [ ] Capture all plant not assigned to MEP System - Number of items, analysis of which system is worse (Elec / Mech)
- [x] Room and Space name application
     - [x] Understand method how to calculate if object is in Room/ Space.
     - [ ] Create scripts for both lenghts and fittings:
          - [ ] Ventilation
          - [ ] Pipe
          - [x] Cable tray
- [ ] Create possible d3 visualisations of all this data collection?
     - [x] Understand how to transact and with document and create file.writeStream()
     - [x] Create a file either .txt or .csv as direct export from Revit document
     - [ ] Use export to create visualisations to avoid imports into Revit Python Wrapper :dizzy_face:
+ Visulation types:
     - [ ] Systems - Named vs. Unnamed
     - [ ] Systems - MEP Broken down by DUCT vs. PIPE vs. ELEC
     - [ ] Systems - MEP Broken down by Service:
          + DUCT - Services
          + PIPE - Services
          + Elec - Services
     - [ ] Linked model data vs MEP consultant model
          * If MEP model has been linked to room names/ numbers
          * If Grids/Levels have Copy/Monitor applied

---
# UNKNOWNS
* try to get all air terminals - add location information here
* 
