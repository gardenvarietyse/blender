###
#
# Generates a diamond shape (like two pyramids stuck to eachother)
#
####

import bpy

verts = [(-1, -1, 0), (-1, 1, 0), (1, 1, 0), (1, -1, 0), (0, 0, 1), (0, 0, -1)]
faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4), (0, 1, 5), (1, 2, 5), (2, 3, 5), (3, 0, 5)]

# boilerplate stuff from here on
mesh = bpy.data.meshes.new("DiamondMesh")
bObject = bpy.data.objects.new("Diamond",  mesh)

bObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(bObject)

# generate edges automatically
mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges = True)
