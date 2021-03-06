# REVIT-ScratchPad :star:
## Info
These code snippets can be run inside the python IDE in an active Revit project. :snake:

I will be adding more and more scripts as ideas come to me.

The main focus of this scratchpad is to test out and develop proof of concepts.

## Get involved
I have a cheatsheet for beginners to get involved and start the learning process of how to create scripts and buttons in Revit.
>the button building part builds off of the PyRevit library. Check the Cheatsheet for more information on PyRevit!

#### [The Revit Cheat Sheet](cheatSheet.md)  :octopus:
#### Be Warned once you start coding you'll probably get lost in the maze forever! :skull:

# What the BBK TAB and .PushButtons look like so far! - 
*update May '19*
![icons_for_git_20190424](https://user-images.githubusercontent.com/26323783/56657123-26dec180-668f-11e9-9189-02688a88dfd3.PNG)

# Visualisation Scripts
![test_gif1](https://user-images.githubusercontent.com/26323783/54753764-be0cb100-4bd9-11e9-97ad-5848818bb451.gif)
---
# Completed Features :construction_worker:
### Button Creation :beer:
Within the Revit Ribbon we can add buttons to execute scripts both with and without user input. This allows the Revit user to work with the tools without feeling like they are 'hacking' a solution together.
The source code to the buttons is available to the Revit user by using Alt + leftMouse Click this will show the folder location of the button on their local install of the software.

### Duct Length and Duct Surface Area Calculator :boom:
This script can calculate the quantities within the open Revit document to create a report for the BID/ Team or Project Delivery team ahead of site commencement works.

This report could also give some indication to the Offsite fabrication teams to help with resourcing and planning ahead of deliveries to site.

This tool could be ran in conjunction with Location tools to give support to planning and logistics teams around where, and when quantities of supplies would be delivered to site. 

### Write Location Parameter to MEP objects :pushpin:
This tool facilitates the creation of Location data on MEP objects within the Revit whereby it can be exported for use outside of the Revit environment.

The tool creates a Transaction within Revit writing to a *Global Parameter* -> **BBK_MEP_LOCATION**

Utilising the Revit Transaction process the script can be turned back, using the built in Undo function (at the top of the Revit window)

The tool writes to both fittings, and lengths (Revit: *MEP_Curves*) giving them a location built upon the space within the model.

The MEP Object has to be within the same model as the space it resides in, the function of the button does not work at this time with linked MEP files. It can however be modified to utilise **Revit Architectural ROOMS**.

### Room and Space Name Match :bookmark_tabs:
Quick report to check if Arch and MEP models match on naming.

## Warnings inside Revit Project :skull:
This tool outputs to chart.js window at the minute it is a pie chart :cake:

Write to excel database to collect information on project - and ultimately create understanding of what a consultant sees a stage 3 model is at.

---
# TODOs! :o:
- [ ] Builders work clash tool 
     - [x] Utilise Dynamo script created by BBK in India
     - [x] Schedule out Builderswork applying Hole-number property
     - [ ] Refactor to apply Shared Parameters
- [ ] BBK_MEP_LOCATION
     - [x] Duct Accessories - BuiltInCategory.OST_DuctAccessory
     - [x] Pipe Accessories - BuiltInCategory.OST_PipeAccessory
     - [x] Electrical Fixtures - BuiltInCategory.OST_ElectricalFixtures
     - [x] Electrical Equipment - BuiltInCategory.OST_ElectricalEquipment
- [ ] Create MEP System analytics
     - [x] Captured how to generate system assignment - All MEP systems :octocat:
     - [x] Break systems down into MEP classes - Duct/ Air : Pipe/Liquid fluid : CableTray/ Elec
     - [ ] Capture all plant not assigned to MEP System - Number of items, analysis of which system is worse (Elec / Mech)
- [ ] Create possible d3 visualisations of all this data collection?
     - [x] Create output of Warnings on project
     - [x] Understand how to transact and with document and create file.writeStream()
     - [x] Create a file either .txt or .csv as direct export from Revit document
     - [ ] Create CSV Point (X,Y,Z) exports for comparisons with arch files. - FOR LCY
     - [ ] Use export to create visualisations to avoid imports into Revit Python Wrapper :dizzy_face:
- Visulation types:
     - [x] Find filters by System Classification
     - [ ] Systems - Named vs. Unnamed
     - [ ] Systems - MEP Broken down by DUCT vs. PIPE vs. ELEC 
     - [x] Systems - MEP Broken down by Service: - This is a new filtered window implementation
          + DUCT - Services
          + PIPE - Services
          + Elec - Services
     - [ ] Linked model data vs MEP consultant model
          * If MEP model has been linked to room names/ numbers
          * If Grids/Levels have Copy/Monitor applied

---
# UNKNOWNS
These are obviously unknown :space_invader:
