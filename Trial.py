#Imports.
import bpy;
import random;

#Function to clean the scene. This removes all of the objects, collections, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene. 
def cleanScene():
    # Changes the mode to object mode if it is in Edit mode. 
    if (bpy.context.active_object and bpy.context.active_object.mode == "EDIT"):
        bpy.ops.object.editmode_toggle();
        
    # Checks for hidden stuff and unhides them.     
    for obj in bpy.data.objects: 
        obj.hide_set(False);
        obj.hide_select = False;
        obj.hide_viewport = False;
        
    # Selects all the objects and then deletes.     
    bpy.ops.object.select_all(action = "SELECT");
    bpy.ops.object.delete();

# Calling the clean scene method. 
cleanScene();

# Size of each cube. 
size = 1;

# Setting the x, y, and z positions. 
x = y = z = size / 2;

# Iterate over each grid 'cell' we want a cube at. 
for x in range(20):
    for y in range(20):
        for z in range(1): 
            # Set the location. 
            location = (x, y, z);

            # Add the cubes. 
            bpy.ops.mesh.primitive_cube_add(size = size, location=location, scale=(1, 1, 1));
            # Add a new material slot. 
            bpy.ops.object.material_slot_add();
            
# Notes: 
# - For loop for the grid: 
#        - x is for creating cubes in the x axis. 
#        - y is for creating cubes in the y axis. 
#        - z is for creating cubes in the z axis. 
# - I need to add the materials to the cubes and somehow save it in the Blender program. 
# - I need to add a function to create a tree in a random position. This function will create cubes and put them in a way to look like a tree. It will also assign the correct materials to their proper cubes. 
