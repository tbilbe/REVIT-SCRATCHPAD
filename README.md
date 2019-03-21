# REVIT-ScratchPad :star:
## Info
These code snippets can be ran inside the python ide in an active Revit project. :snake:
I will be adding more and more scripts as ideas come to me.

# What the Buttons look like so far!
![icons_for_git](https://user-images.githubusercontent.com/26323783/54754238-f2cd3800-4bda-11e9-9f9b-ad76fc04e8b3.PNG)

The main focus of this scratchpad is to test out and develop proof of concepts.
# Visualisations
![test_gif1](https://user-images.githubusercontent.com/26323783/54753764-be0cb100-4bd9-11e9-97ad-5848818bb451.gif)
---
# TODOs! 

- [x] *CREATE BUTTONS ON RIBBON FOR DISTRIBUTION READY CODE*
- [x] Duct length and Ductwork Surface Area Calculator :boom:
- [x] Duct Location - Apply room name, room number to ductwork. :boom:
- [x] Cable tray location and Lengths
- [x] Pipework location and lengths
- [x] Create MEP System analytics
     - [x] Captured how to generate system assignment - All MEP systems :octocat:
     - [x] Break systems down into MEP classes - Duct/ Air : Pipe/Liquid fluid : CableTray/ Elec
     - [x] Capture all plant not assigned to MEP System - Number of items, analysis of which system is worse (Elec / Mech)
- [x] Room and Space name application
     - [x] Understand method how to calculate if object is in Room/ Space.
     - [x] Create scripts for both lenghts and fittings:
          - [x] Ventilation
          - [x] Pipe
          - [x] Cable tray
- [ ] Create possible d3 visualisations of all this data collection?
     - [x] Understand how to transact and with document and create file.writeStream()
     - [x] Create a file either .txt or .csv as direct export from Revit document
     - [ ] Create CSV Point (X,Y,Z) exports for comparisons with arch files. - FOR LCY
     - [ ] Use export to create visualisations to avoid imports into Revit Python Wrapper :dizzy_face:
+ Visulation types:
     - [x] Found filters by System Classification
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

