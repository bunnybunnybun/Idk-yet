import gi
import subprocess
import os
gi.require_version('Gtk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib, GtkLayerShell

class WallpaperWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Wallpaper hopefully")

        current_pid = os.getpid()
        print(current_pid)

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.BACKGROUND)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_exclusive_zone(self, -1)

        self.background = GdkPixbuf.Pixbuf.new_from_file("/home/carlisle/Idk-yet/Idk-yet/custom_wallpaper_engine/space_background_2.jpg")
        self.foreground_1 = GdkPixbuf.Pixbuf.new_from_file("/home/carlisle/Idk-yet/Idk-yet/custom_wallpaper_engine/orange_planet.png")
        self.foreground_2 = GdkPixbuf.Pixbuf.new_from_file("/home/carlisle/Idk-yet/Idk-yet/custom_wallpaper_engine/blue_planet.png")

        self.mouse_x, self.mouse_y = 0, 0

        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.connect("draw", self.on_draw)
        #self.drawing_area.set_events(Gdk.EventMask.POINTER_MOTION_MASK)
        #self.drawing_area.connect("motion-notify-event", self.on_motion)
        GLib.timeout_add(50, self.update_mouse_position)

        self.connect("realize", self.on_realize)

        self.add(self.drawing_area)
        self.show_all()

    def on_realize(self, widget):
        display = self.get_display()
        for i in range(display.get_n_monitors()):
            monitor = display.get_monitor(i)
            geometry = monitor.get_geometry()
            self.screen_width, self.screen_height = geometry.width, geometry.height
            print(self.screen_width, self.screen_height)

    def update_mouse_position(self):
        try:
            coords = subprocess.check_output(
                [os.path.expanduser("~/wl-find-cursor/wl-find-cursor"), "-p"],
                text=True,
                timeout=1.0
            ).strip()

            self.mouse_x, self.mouse_y = map(int, coords.split())
            self.drawing_area.queue_draw()

            #print(f"pos{self.mouse_x}, {self.mouse_y}")
        
        except Exception as e:
            print(f"Mouse tracking error: {e}")

        return True

    def on_draw(self, widget, cr):
        #screen_width, screen_height = self.screen_width, self.screen_height
        img_width = self.background.get_width()
        img_height = self.background.get_height()
        scale_x = self.screen_width / img_width
        scale_y = self.screen_height / img_height

        scale = max(scale_x, scale_y)

        translate_x = (self.screen_width - img_width * scale) / 2
        translate_y = (self.screen_height - img_height * scale) / 2

        cr.translate(translate_x, translate_y)
        cr.scale(scale, scale)

        Gdk.cairo_set_source_pixbuf(cr, self.background, 0, 0)
        cr.paint()

        cr.identity_matrix()

        center_x = self.screen_width / 2
        center_y = self.screen_height / 2

        parallax_x_1 = center_x + (self.mouse_x - center_x) * 0.3
        parallax_y_1 = center_y + (self.mouse_y - center_y) * 0.3
        parallax_x_2 = center_x + (self.mouse_x - center_x) / 0.3
        parallax_y_2 = center_y + (self.mouse_y - center_y) / 0.3

        Gdk.cairo_set_source_pixbuf(
            cr,
            self.foreground_1,
            parallax_x_1 - self.foreground_1.get_width() / 2,
            parallax_y_1 - self.foreground_1.get_height() / 2
        )
        cr.paint()

        Gdk.cairo_set_source_pixbuf(
            cr,
            self.foreground_2,
            parallax_x_2 - self.foreground_2.get_width() / 2,
            parallax_y_2 - self.foreground_2.get_height() / 2

        )
        cr.paint()

    #def on_motion(self, widget, event):
        #self.fore_x, self.fore_y = event.x, event.y
        #self.drawing_area.queue_draw()

if __name__ == "__main__":
    win = WallpaperWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()