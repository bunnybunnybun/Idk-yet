import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

script_dir = os.path.dirname(os.path.abspath(__file__))

css_provider = Gtk.CssProvider()
css_provider.load_from_path(f"{script_dir}/wallpaper_creator_style.css")

screen = Gdk.Screen.get_default()
style_context = Gtk.StyleContext()
style_context.add_provider_for_screen(
    screen,
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Wallpaper creator")
        self.set_default_size(500, 500)

        self.background_label = Gtk.Label(label="Choose the background image:")
        self.background_label.set_halign(Gtk.Align.START)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.choose_background_image_button = Gtk.FileChooserButton(title="Select image", action=Gtk.FileChooserAction.OPEN)
        self.choose_background_image_button.connect("file-set", self.on_file_selected)
        self.choose_background_image_button.set_name("background")
        self.choose_background_image_button.set_halign(Gtk.Align.START)

        self.background_intensity_slider = Gtk.Scale.new_with_range(orientation=Gtk.Orientation.HORIZONTAL, min=0, max=100, step=1)
        self.background_intensity_slider.set_halign(Gtk.Align.START)
        self.background_intensity_slider.set_value(30)

        self.foreground_1_label = Gtk.Label(label="Choose the first foreground image:")
        self.foreground_1_label.set_halign(Gtk.Align.START)

        self.choose_foreground_1_image_button = Gtk.FileChooserButton(title="Select image", action=Gtk.FileChooserAction.OPEN)
        self.choose_foreground_1_image_button.connect("file-set", self.on_file_selected)
        self.choose_foreground_1_image_button.set_name("foreground_1")
        self.choose_foreground_1_image_button.set_halign(Gtk.Align.START)

        self.foreground_1_intensity_slider = Gtk.Scale.new_with_range(orientation=Gtk.Orientation.HORIZONTAL, min=0, max=100, step=1)
        self.foreground_1_intensity_slider.set_halign(Gtk.Align.START)
        self.foreground_1_intensity_slider.set_value(30)

        self.foreground_2_label = Gtk.Label(label="Choose the second foreground image:")
        self.foreground_2_label.set_halign(Gtk.Align.START)

        self.choose_foreground_2_image_button = Gtk.FileChooserButton(title="Select image", action=Gtk.FileChooserAction.OPEN)
        self.choose_foreground_2_image_button.connect("file-set", self.on_file_selected)
        self.choose_foreground_2_image_button.set_name("foreground_2")
        self.choose_foreground_2_image_button.set_halign(Gtk.Align.START)

        self.foreground_2_intensity_slider = Gtk.Scale.new_with_range(orientation=Gtk.Orientation.HORIZONTAL, min=0, max=100, step=1)
        self.foreground_2_intensity_slider.set_halign(Gtk.Align.START)
        self.foreground_2_intensity_slider.set_value(30)

        self.set_as_wallpaper_button = Gtk.Button(label="Set as wallpaper")
        self.set_as_wallpaper_button.set_halign(Gtk.Align.START)

        self.main_box.pack_start(self.background_label, False, False, 0)
        self.main_box.pack_start(self.choose_background_image_button, False, False, 0)
        self.main_box.pack_start(self.background_intensity_slider, False, False, 0)
        self.main_box.pack_start(self.foreground_1_label, False, False, 0)
        self.main_box.pack_start(self.choose_foreground_1_image_button, False, False, 0)
        self.main_box.pack_start(self.foreground_1_intensity_slider, False, False, 0)
        self.main_box.pack_start(self.foreground_2_label, False, False, 0)
        self.main_box.pack_start(self.choose_foreground_2_image_button, False, False, 0)
        self.main_box.pack_start(self.foreground_2_intensity_slider, False, False, 0)
        self.main_box.pack_start(self.set_as_wallpaper_button, False, False, 0)
        self.add(self.main_box)

    def on_file_selected(self, file_chooser):
        button_id = file_chooser.get_name()
        filename = file_chooser.get_filename()
        print(f"[{button_id}] {filename}")

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()