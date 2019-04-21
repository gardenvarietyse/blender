###
#
# Generates a spherical-shaped spiral
#
####

import bpy
import math

def spiral(numLoops, radsPerEdge, rPerPoint, zOffset = 0, zDelta = 0):
	verts = []

	# total number of points needed
	numPoints = int((numLoops * math.pi * 2) / radsPerEdge)

	# spiral state: radius and angle
	r = 0
	theta = 0
	reverse = False
	
	# magic
	for x in range(1, numPoints):
		verts.append((math.cos(theta) * r, math.sin(theta) * r, zOffset))
		r = r + rPerPoint if reverse else r - rPerPoint
		theta = theta + radsPerEdge
		zOffset = (zOffset + zDelta)

		if x == numPoints/2:
			reverse = True
		
	return verts

numLoops = 5
verts = spiral(numLoops, math.pi * 0.25, 1 / (numLoops / 0.1), 0, 0.1 / numLoops)

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