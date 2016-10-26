import bpy

bl_info = {
    "name": "Subsurf Toggler",
    "author": "Stefan Heinemann",
    "blender": (2, 77, 0),
    "version": (0, 0, 2),
    "location": "Key Bindings",
    "description": "Provide option to bind a key so it togglers the subsurf",
    "category": "User Interface"
}


class ToggleSubsurf(bpy.types.Operator):
    bl_idname = 'object.toggle_subsurf'
    bl_label = "Subsurf Toggler"

    def cur_object(self):
        return bpy.context.scene.objects.active

    def execute(self, context):
        obj = self.cur_object()
        modifiers = obj.modifiers

        for mod in modifiers:
            if mod.type == 'SUBSURF':
                mod.show_viewport = not mod.show_viewport

        return {'FINISHED'}


addon_keymaps = []


def register_keymaps():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(
        name = "Object", space_type='EMPTY')
    kmi = km.keymap_items.new(
        ToggleSubsurf.bl_idname)
    kmi.properties.name = "Subsurf Toggler"
    addon_keymaps.append(km)


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()
