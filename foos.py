import bpy

T_LONG = 3				# thickness on long sides
T_SHORT = 10			# thickness on short (goal) sides
L = 111.5/2				# distance from goal to goal (half, use mirror modifier)
W = 68
H = 12.5

GOAL_WIDTH = 27
GOAL_TOP_HEIGHT = 4		# height of the curved roof of the goals

BAR_HEIGHT = 8			# distance from bottom to middle of bars

PLAYER_TOP = -4.5		# distance from middle of bar to top of player's head
PLAYER_HEIGHT = 11.5	# total player height

verts = []
faces = []


bObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(bObject)

# boom
mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges = True)