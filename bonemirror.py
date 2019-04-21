import bpy
import math

def findBone(armature, name):
	for bone in armature.pose.bones:
		if bone.name == name:
			return bone
	return None

print('\n----\n')

armature = None
for obj in bpy.context.scene.objects:
	if obj.type == 'ARMATURE':
		armature = obj
		break

if not armature:
	print('No armature found')
	quit()

bpy.context.scene.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# source bones
bones_right = [ ]
bones_left = [ ]

print('Armature found')
for bone in armature.pose.bones:
	if bone.name[-2:] == '.R':
		bones_right.append(bone)
		otherBone = findBone(armature,  bone.name.replace('.R', '.L'))

		if not otherBone:
			print('ERROR: Found no corresponding bone for ' + bone.name)
			quit()

		bones_left.append(bone)
		bone.bone.select = True
		otherBone.bone.select = False

print('Copying R pose ..')
bpy.ops.pose.copy()

for bone in bones_right:
	bone.bone.select = False

print('Pasting L pose ..')
for bone in bones_left:
	bone.bone.select = True

bpy.ops.pose.paste(True, True)
