#!/bin/bash
sudo pacman -Syu
sudo pacman -S --needed kitty git base-devel fuzzel swaybg
if [ -f "$HOME/Idk-yet/.yay_has_been_installed" ]; then
    echo "Yay has already been installed"
else
    cd ~/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && cd .. && touch ~/Idk-yet/.yay_has_been_installed && rm -rf yay
fi
yay -S --needed mangowc-git quickshell
sudo cp -r ~/this_distro_thingy/this_distro_thingy/fuzzel /etc/xdg/
cp -r ~/this_distro_thingy/this_distro_thingy/kitty ~/.config/
mkdir ~/.config/mango
chmod +x ~/Idk-yet/this_distro_thingy/setup_mango_script.sh
~/Idk-yet/this_distro_thingy/setup_mango_script.sh
