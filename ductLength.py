import Autodesk.Revit.DB as DB

doc = __revit__.ActiveUIDocument.Document

# duct collector 
duct_cl = DB.FilteredElementCollector(doc) \
            .OfClass(DB.Mechanical.Duct) \
            .ToElements()

all_parameters = []
            
for params in duct_cl:
    all_parameters.append(params.Parameters)

for properties in all_parameters:
    print(properties.ToString())

total_duct_len = 0.0
sa_calc_total = 0.0

duct_dict = {}
duct_arr = []
index = 0


for duct in duct_cl:
    width_param = duct.LookupParameter('Width')
    if width_param.AsValueString() != None:
        width_dim =  width_param.AsValueString()
        duct_dict['Width' + index.ToString()] = width_dim
        
    len_param = duct.LookupParameter('Length')
    if len_param.AsValueString() != None:
        len_dim =  len_param.AsValueString()
        duct_dict['Length' + index.ToString()] = len_dim
        
    height_param = duct.LookupParameter('Height')
    if height_param.AsValueString() != None:
        height_dim =  height_param.AsValueString()
        duct_dict['Height' + index.ToString()] = height_dim
    index = index + 1

duct_arr.append(duct_dict)
print(duct_arr)


total_duct_len = 0.0
sa_calc_total = 0.0

for duct in duct_cl:
    width_param = duct.LookupParameter('Width').AsValueString()
    len_param = duct.LookupParameter('Length').AsValueString()
    high_param = duct.LookupParameter('Height').AsValueString()
    if width_param:
        sa_calc = (int(width_param) * int(len_param) * 2) + (int(high_param) * int(len_param) *2)
        sa_calc_meters = sa_calc / 1000000
        total_duct_len = total_duct_len + int(len_param)
        sa_calc_total = sa_calc_total + sa_calc
        print('the width of the duct is: ' + str(width_param) + 'mm')
        print('the height of the duct is: ' + str(high_param) + 'mm')
        print('the length of the duct is: ' + str(len_param + 'mm'))
        print('the surface area of the duct is: ' + str(sa_calc_meters) + 'm2\n')

print('the total length of the duct is: '+str(total_duct_len / 1000) + 'm')
print('the total surface area of all the duct is: '+str(sa_calc_total / 1000) + 'm2\n')