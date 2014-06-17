"""This module provides a way to access neutron spatial solver codes.  It primarily consists of wrapped fortran code's being called with python via f2py"""

from AHOTN.src_LN.input import input as ahot_ln_input
#from AHOTN.src_LN.solve import solve as ahot_ln_solve
#from AHOTN.src_LN.output import output as ahot_ln_output

from dict_util import dict_complete

def ahotn(inputdict_unchecked):
	inputdict = dict_complete(inputdict_unchecked)
	ahot_ln_input("test title in",
	inputdict['spatial_order'],
	inputdict['spatial_method'],
	inputdict['quadrature_order'],
	inputdict['quadrature_type'],
	inputdict['nodes_xyz'][0],
	inputdict['nodes_xyz'][1],
	inputdict['nodes_xyz'][2],
	inputdict['num_groups'],
	inputdict['num_materials'],
	inputdict['x_cells_widths'],
	inputdict['y_cells_widths'],
	inputdict['z_cells_widths'],
	inputdict['x_boundry_conditions'][0],
	inputdict['x_boundry_conditions'][1],
	inputdict['y_boundry_conditions'][0],
	inputdict['y_boundry_conditions'][1],
	inputdict['z_boundry_conditions'][0],
	inputdict['z_boundry_conditions'][1],
	inputdict['material_id'],
	inputdict['quadrature_file'],
	inputdict['xs_file'],
	inputdict['src_file'],
	inputdict['converge_critical'],
	inputdict['max_iterations'],
	inputdict['moments_converged'],
	inputdict['converge_tolerence'],
	inputdict['ichk'],
	inputdict['ichk_tolerence'],
	inputdict['momp'],
	inputdict['momsum'],
	inputdict['mompt'],
	inputdict['qdflx'])
	#ahot_ln_solve()
  #ahot_ln_output()
