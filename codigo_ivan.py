import dearpygui as dpg 

# Inicializar Dear PyGui
with dpg.handler_registry():
    with dpg.theme(default=dpg.mvGuiCol_Text, value=(255, 255, 255, 255)):
        with dpg.handler(handler=dpg.mvGuiCol_Text, data=(255, 255, 0, 255)):
            dpg.add_text("¡Hola, Dear PyGui!")

# Crear una ventana
with dpg.handler_registry():
    with dpg.theme(default=dpg.mvThemeCol_WindowBg, value=(30, 30, 30, 255)):
        with dpg.handler(handler=dpg.mvThemeCol_WindowBg, data=(0, 0, 0, 0)):
            with dpg.handler_registry():
                dpg.create_viewport(title="Mi Ventana", width=800, height=600)

# Ejecutar el bucle principal de Dear PyGui
with dpg.handler_registry():
    dpg.create_context()
    dpg.setup_dearpygui()
    dpg.create_viewport(title="Dear PyGui")
    dpg.setup_viewport()
    dpg.show_viewport()
    with dpg.handler_registry():
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()

    dpg.cleanup_dearpygui()
    dpg.destroy_context()