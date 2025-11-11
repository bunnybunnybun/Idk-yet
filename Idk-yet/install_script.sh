#!/bin/bash
sudo pacman -Syu
sudo pacman -S --needed kitty git base-devel fuzzel swaybg
if [ -f "$HOME/Idk-yet/.yay_has_been_installed" ]; then
    echo "Yay has already been installed"
else
    cd ~/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && cd .. && touch ~/Idk-yet/.yay_has_been_installed && rm -rf yay
fi
yay -S --needed mangowc-git quickshell
sudo cp -r ~/Idk-yet/Idk-yet/fuzzel /etc/xdg/
cp -r ~/Idk-yet/Idk-yet/kitty ~/.config/
mkdir ~/.config/mango
chmod +x ~/Idk-yet/Idk-yet/setup_mango_script.sh
~/Idk-yet/Idk-yet/setup_mango_script.sh
