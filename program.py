

# load required files

group_num = 0

group_list = {}

for i in range(11):
    group_list["group_%s" % i] = {}
    group_list["group_%s" % i]["name"] = []
    group_list["group_%s" % i]["lines"] = []


group_list["group_%s" % group_num]["name"] = []
group_list["group_%s" % group_num]["lines"] = []

	# merged topol
title = []

with open("merged_topol.top") as topol:
	lines = [line.strip() for line in topol if not line.startswith(('#', '@'))]

	for line in lines:
		if line.startswith('['):
			group_num = group_num + 1
			group_list["group_%s" % group_num]["name"].append(line)

		elif not line.startswith(('[', ' ')):
			group_list["group_%s" % group_num]["lines"].append(line)
		else:
			if line.startswith(' '):
				group_num = group_num + 1


print("--------group 1 ")
print(group_list["group_1"]["name"])

# choose warhead

# acrylamide

	# mo2 file creation

	# for now load a ready mol2 file.
	# call acpype on the mol2 file to get .itp
	# load .itp in
# process

# first_atom = x
# second_atom = y

# test_bond = atm1 atm2 1 1.3150e-01    5.0827e+05 ;     C5 - C8
# test_angle = atm1 atm2 1    1.2162e+02    5.8626e+02 ;     C6_UNK - C7     - C8 
# test_dihedral = atm1 atm2 atm3 atm4 9   180.00   0.00000   2 ;     C6_UNK-    C7-    C8-    C5
# test_improper = atm1 atm2 atm3 atm4 4   180.00   4.60240   2 ;     C8-    C6_DCF-    C5-    C4 

# write output files

	# merged topol with added bond