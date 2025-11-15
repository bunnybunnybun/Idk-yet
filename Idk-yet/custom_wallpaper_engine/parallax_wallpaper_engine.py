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

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.BACKGROUND)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_exclusive_zone(self, -1)

        self.background = GdkPixbuf.Pixbuf.new_from_file("/home/carlisle/Idk-yet/Idk-yet/swaybg/arch_rainbow.png")
        self.foreground = GdkPixbuf.Pixbuf.new_from_file("/home/carlisle/Idk-yet/Idk-yet/custom_wallpaper_engine/hmm.png")

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
        Gdk.cairo_set_source_pixbuf(cr, self.background, 0, 0)
        cr.paint()

        center_x = self.screen_width / 2
        center_y = self.screen_height / 2

        parallax_x = center_x + (self.mouse_x - center_x) * 0.3
        parallax_y = center_y + (self.mouse_y - center_y) * 0.3

        Gdk.cairo_set_source_pixbuf(
            cr,
            self.foreground,
            parallax_x - self.foreground.get_width() / 2,
            parallax_y - self.foreground.get_height() / 2

        )
        cr.paint()

    #def on_motion(self, widget, event):
        #self.fore_x, self.fore_y = event.x, event.y
        #self.drawing_area.queue_draw()

if __name__ == "__main__":
    win = WallpaperWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()