# Revit Cheat sheet :100:

Use this sheet to get up and running with creating python scripts in revit.

## Set up and Configuration of the Revit Python Shell (RPS) :snake:

Download link: <https://github.com/architecture-building-systems/revitpythonshell> 

Once downloaded the Revit Python Shell will be available on the Add-Ins tab

![addin](https://user-images.githubusercontent.com/26323783/57065518-94a77080-6cc1-11e9-9a6c-c40c58bc8fec.PNG)

You can jump right into using the RPS but configuring the shell so its easier to use the REPL will give us some nice functionality.
We get the ability to select elements in the project and then go straight to the RPS and test scripts against the Revit Element.

### Configure the shell for use in the active model
![configue_1](https://user-images.githubusercontent.com/26323783/57065822-8148d500-6cc2-11e9-9779-923228f4cbeb.png)
![configure_2](https://user-images.githubusercontent.com/26323783/57065964-e7cdf300-6cc2-11e9-9cbb-8a264d0463d8.png)

Edit the Init script so that you have access to 2 key variables:
[The init script is here](COPY_init.py)

#### Inside the REPL
```python
el = '''gives us a list object of the selection so to interact 
        further with the element use bracket notation el[0]'''
s0 = '''gives us the first element in the list so jumps a 
        step on the el variable'''

# From here you can access methods on the specific elements, for example
categoryName = s0.Category.Name

# Note the lookup parameter takes a string which matches 
# the name of the parameter in the project properties window
elevation = s0.LookupParameter('Elevation').AsValueString()
```
![REPL](https://user-images.githubusercontent.com/26323783/57067342-9e7fa280-6cc6-11e9-8892-6b4e1238cb68.png)

## Selectors and Collectors
Programmatically we can interact with any element within the live Revit model (we can interact with the linked model also, but that’s a little more advanced). We have to use `FilteredElementCollector()` to store the elements in a list object. Building a collector is a simple process, and it will become muscle memory!

Heres where the Revit API docs come in! <http://www.revitapidocs.com/>

The documentation will give an indication of how to interact with the elements in the model and it will become your best friend :couple_with_heart:

##### Scenario: Can you get me all the electrical equipment in the model? - Yes with a `FilteredElementCollector()`

looking into the docs , searching for FilteredElementCollector class will yeild ->  
**_This class is used to search, filter and iterate through a set of elements_**  
+ `FilteredElementCollector(doc)` requires a doc parameter which is the reference to the open project. (we've got this because of the init script edit)
+ `.OfCategory(BuiltInCategory.OST_ElectricalEquipment)` inside the docs we can see this method is available to us. It also takes a parameter, a `BuiltInCategory`(a list of these can be seen below!
+ `WhereElementIsNotElementType()` self explanatory here, we dont want types we want the instances.
+ `ToElements()` Returns the complete set of elements that pass the filter(s).

![REPL2](https://user-images.githubusercontent.com/26323783/57070019-19988700-6cce-11e9-8f77-890e44cb0bb0.png)

There you have your first collector :metal: 
##### Scenario Answer: There are 29 pieces of Electrical Equipment

### BuiltInCategory.OST_
I have collated a few categories, but the page has about 1000 to search, just use `Ctrl + f` on [the Revit API docs page](http://www.revitapidocs.com/2018.1/ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm) try and find some more to experiment with.

Use this table for inspo | :fire: | :construction_worker:
:---: | :---: | :---:
OST_MechanicalEquipment | OST_DuctFitting | OST_PipeAccessories
OST_ElectricalEquipment | OST_DuctCurves | OST_CableTrayFitting
OST_ElectricalFixtures | OST_DuctAccessories | OST_CableTray
OST_MEPSpaces | OST_PipeFitting | OST_Conduit
OST_Rooms | OST_PipeCurves | OST_ConduitFitting

---
> Hey that's nice that you can read from the Revit project Database, but I need to write loads of data to multiple parameters...:rage:


## Transaction Object
> Here is your cue to go back to your Revit API docs tab!
We have to use the `Transaction()` class and construct the object, just like the `FilteredElementCollector()` object.  
The Transaction has a name which is referred to when using the undo, redo keys!  

```python
t = Transaction(doc, 'Electrical Equipment Space Naming Util')
t.Start()
'''
DO SOME REALLY REALLY COOL STUFF!
'''
t.Commit()
```

In the above example in the undo dropdown we would see ‘CableTray Space Naming’ – this parameter can literally be a string!  
Place you script logic between the transaction such as writing to a parameter, for example giving an element a room name/ space that an element is residing in.



> Its all very well and good using the REPL to script a few easy things but we want **repeatability!**
lets build a Button!

## Button Creation
##### Using the PyRevit Api
**TODO**
+ link the PyRevit github
+ write up on Pyrevit
+ PyRevit Docs
+ Complete how to create a button


## Addtional Resources
+ [The Building Coder - Autodesk Developer Network](https://thebuildingcoder.typepad.com/)
+ [PyRevit Github Repo and blog pages](https://github.com/eirannejad/pyRevit)
+ [Cool Macros, Ideas for new scripts](https://boostyourbim.wordpress.com/)
+ [Dynamo package creation - how to create python nodes](http://archi-lab.net/)
+ [Generic Revit add-ins and python scripts](http://dp-stuff.org/)
+ [SpiderInnet Blog](https://spiderinnet.typepad.com/)
