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
    "version": (0, 0, 1),
    "location": "3D View > Properties > Weight Transfer",
    "warning": "",
    "category": "Rigging",
}

class VIEW3D_PT_WeightTransferPanel(bpy.types.Panel):
    bl_label = "Weight Transfer"
    bl_idname = "VIEW3D_PT_Weight_Transfer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Weight Transfer"

    def draw(self, context):
        """Define the layout of the panel"""
        layout = self.layout
        scene = context.scene
        row = layout.row()
        
        layout.label(text="Source Mesh:")
        row = layout.row(align=True)
        row.prop_search(scene, "target_rig", bpy.data, "objects", text="")
        row.operator("object.pick_mesh", text="", icon='EYEDROPPER')

        layout.label(text="Target Mesh:")
        row = layout.row(align=True)
        row.prop_search(scene, "target_rig", bpy.data, "objects", text="")
        row.operator("object.pick_mesh", text="", icon='EYEDROPPER')

        
def register():
    bpy.utils.register_class(VIEW3D_PT_WeightTransferPanel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_WeightTransferPanel)

if __name__ == "__main__":
    register()
