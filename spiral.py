###
#
# Generates a spiral out of vertices and edges
#
# has to be run manually for now (paste into script editor, Alt+P to run)
#
####

import bpy
import math

verts = []

# 10 loops in the spiral
numLoops = 10

# each edge covers 0.1 of a half turn
# (0.5 gives a diamond shape, for instance)
radsPerEdge = math.pi * 0.1

# distance to extend from center at each point
# (chosen arbitrarily, didn't mess with it yet)
rPerPoint = 1 / (numLoops * 10)

# total number of points needed
numPoints = int((numLoops * math.pi * 2) / radsPerEdge)

# magic
for x in range(numPoints):
	verts.append((math.cos(radsPerEdge * x) * (rPerPoint * x), 0, math.sin(radsPerEdge * x) * (rPerPoint * x)))

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