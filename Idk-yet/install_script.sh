#!/bin/bash
sudo pacman -Syu
sudo pacman -S --needed python-cairo kitty git base-devel fuzzel swaybg sddm gtk3 gtk4 gtk-layer-shell
sudo systemctl enable sddm
pip install PyGOBject --break-system-packages
if [ -f "$HOME/Idk-yet/.yay_has_been_installed" ]; then
    echo "Yay has already been installed"
else
    cd ~/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && cd .. && touch ~/Idk-yet/.yay_has_been_installed && rm -rf yay
fi
yay -S --needed mangowc-git quickshell fluent-gtk-theme
gsettings set org.gnome.desktop.interface gtk-theme "Fluent-pink-Light"
sudo cp -r ~/Idk-yet/Idk-yet/fuzzel /etc/xdg/
cp -r ~/Idk-yet/Idk-yet/kitty ~/.config/
mkdir ~/.config/mango
chmod +x ~/Idk-yet/Idk-yet/setup_mango_script.sh
~/Idk-yet/Idk-yet/setup_mango_script.sh
git clone https://github.com/cjacker/wl-find-cursor && cd wl-find-cursor && make