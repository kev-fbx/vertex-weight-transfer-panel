# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name": "Weight Transfer Panel",
    "author": "kev-fbx",
    "description": "N-panel menu for easy weight transfer",
    "blender": (4, 2, 0),
    "version": (1, 0, 0),
    "location": "3D View > Properties > Weight Transfer",
    "warning": "",
    "category": "Rigging",
}

class transfer_weights(bpy.types.Operator):
    """Transfers vertex weights between meshes"""
    bl_label = "Transfer weights"
    bl_idname = "view3d.transfer_weights"
    bl_info = "Transfers vertex weights between meshes"
    
    def execute(self, context):
        bpy.ops.paint.weight_paint_toggle()
        bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', vert_mapping='POLYINTERP_NEAREST', layers_select_src='NAME', layers_select_dst='ALL')
        return {"FINISHED"}

class WEIGHT_TRANSFER_PT_ui(bpy.types.Panel):
    bl_label = "Weight Transfer"
    bl_idname = "VIEW3D_PT_Weight_Transfer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        """Define the layout of the panel"""
        layout = self.layout
        scene = context.scene
        row = layout.row()
        
        row = layout.row(align=True)
        layout.operator("view3d.transfer_weights")
        
classes = [transfer_weights, WEIGHT_TRANSFER_PT_ui]
        
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()