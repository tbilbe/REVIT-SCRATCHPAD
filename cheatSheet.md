# Revit Cheat sheet

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

Edit the Init script so that you have access to a few selectino variables
[The init script is here](COPY_init.py)


