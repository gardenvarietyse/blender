

import bpy
import math

verts = []

numSteps = 10
depth = 1.4


# magic
for x in range(numSteps):
	verts.append((0, depth * x, x))
	
	if(x < numSteps-1):
		verts.append((0, depth * x, x+1))

# connect vertices automatically in order
numEdges = len(verts) - 1

edges = []
for i in range(numEdges):
	edges.append((i, i + 1))

# boilerplate stuff from here on
mesh = bpy.data.meshes.new("SpiralMesh")
bObject = bpy.data.objects.new("Spiral",  mesh)

bObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(bObject)

# no faces in this mesh
mesh.from_pydata(verts, edges, [])
mesh.update()