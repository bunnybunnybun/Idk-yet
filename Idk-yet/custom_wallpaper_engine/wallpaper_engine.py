import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GdkPixbuf, GtkLayerShell

def set_wallpaper(image_path):
    windows = []
    display = Gdk.Display.get_default()

    for i in range(display.get_n_monitors()):
        monitor = display.get_monitor(i)
        monitor_geometry = monitor.get_geometry()

        window = Gtk.Window()
        GtkLayerShell.init_for_window(window)
        GtkLayerShell.set_layer(window, GtkLayerShell.Layer.BACKGROUND)
        GtkLayerShell.set_monitor(window, monitor)
        # makes other apps render above the wallpaper
        GtkLayerShell.set_exclusive_zone(window, 0)
        panel_height = 50

        pixbuf = GdkPixbuf.Pixbuf.new_from_file(image_path)
        img_width, img_height = pixbuf.get_width(), pixbuf.get_height()
        screen_width, screen_height = monitor_geometry.width, monitor_geometry.height + panel_height

        img_ratio = img_width / img_height
        screen_ratio = screen_width / screen_height

        if img_ratio > screen_ratio:
            crop_height = img_height
            crop_width = int(img_height * screen_ratio)

        else:
            crop_width = img_width
            crop_height = int(img_width / screen_ratio)

        x = (img_width - crop_width) // 2
        y = (img_height - crop_height) // 2

        cropped = pixbuf.new_subpixbuf(x, y, crop_width, crop_height)

        scaled = cropped.scale_simple(
            monitor_geometry.width,
            monitor_geometry.height + panel_height,
            GdkPixbuf.InterpType.BILINEAR
        )

        image = Gtk.Image.new_from_pixbuf(scaled)
        window.add(image)
        window.fullscreen()
        window.show_all()
        windows.append(window)

    Gtk.main()

if __name__ == "__main__":
    set_wallpaper("/home/carlisle/Idk-yet/Idk-yet/swaybg/arch_rainbow.png")