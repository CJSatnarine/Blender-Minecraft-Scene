#Imports.
import bpy;
import random;

# Variables: 

size = 1; # Size of each cube. 

x = y = z = size / 2; # Setting the x, y, and z positions. 


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

# Iterate over each grid 'cell' we want a cube at.
def spawnGround():  
    for x in range(20):
        for y in range(20):
            for z in range(1): 
                # Set the location. 
                location = (x, y, z);

                # Add the cubes. 
                bpy.ops.mesh.primitive_cube_add(size = size, location=location, scale=(1, 1, 1));
                # Set the newly created cube as the active object. 
                activeObject = bpy.context.active_object;
                # Add a new material slot. 
                # bpy.ops.object.material_slot_add();
                # Creating a new material and assigning it to the active cube. 
                material = bpy.data.materials.new("Material");
                material.use_nodes = True;
                materialNodes = material.node_tree.nodes;
                materialLinks = material.node_tree.links;

                activeObject.data.materials.append(material);

                # Change the base colour. 
                materialNodes['Principled BSDF'].inputs['Base Color'].default_value = (1.0, 0.47, 1.0, 1.0);

# Calls the functions: 
cleanScene();
spawnGround();

# Notes: 
# - For loop for the grid: 
#        - x is for creating cubes in the x axis. 
#        - y is for creating cubes in the y axis. 
#        - z is for creating cubes in the z axis. 
# - I need to add the materials to the cubes and somehow save it in the Blender program. 
# - I need to add a function to create a tree in a random position. This function will create cubes and put them in a way to look like a tree. It will also assign the correct materials to their proper cubes. 