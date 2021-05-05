#!/usr/bin/bash
termux-setup-storage
apt update ; apt upgrade ; pkg update ; pkg upgrade ; termux-setup-storage ; apt install -y wget ; apt install -y zsh ; apt install -y git ; apt install -y python ; apt install -y python2 ; apt install -y php ; apt install -y tree ; apt install -y nmap ; apt install -y openssh ; apt install -y nano ; pkg install -y curl ; apt install -y figlet ; apt install -y zlib ; apt install -y netcat ; pkg install -y screenfetch ; pip install --upgrade pip ; pip install --upgrade pip setuptools ; pip install lolcat ; pip install requests ; pip install bs4 ; pip install telegram ; pip install imap_tools
apt update && apt upgrade && pkg update && pkg upgrade
pkg up ; pkg install curl ; pkg install grep ; pkg install ncurses-utils
apt install -y git zsh python python2 nano php tree nmap man figlet toilet zlib wget unzip command-not-found fontconfig netcat
pip install --upgrade pip ; pip install --upgrade pip setuptools ; pip install --upgrade httpie ; pip install requests ; pip install lolcat ; pip install openssh ; pip install beautysh ; pip install bs4 ; pip install cuttpy
unzip x.zip
rm x.zip
cp -R "$HOME/server/x/.termux" "$HOME/.termux"
git clone https://github.com/ohmyzsh/ohmyzsh "$HOME/.oh-my-zsh" --depth 1
rm -rf /$HOME/.zshrc
cp /$HOME/.termux/tab/.b /$HOME/ && mv /$HOME/.b /$HOME/.zshrc
echo '' >> "$HOME/.zshrc"
git clone https://github.com/zsh-users/zsh-syntax-highlighting "$HOME/.zsh-syntax-highlighting" --depth 1
chsh -s zsh
cp $HOME/.termux/ecore /data/data/com.termux/files/usr/bin/ ; chmod +x /data/data/com.termux/files/usr/bin/ecore
cp $HOME/.termux/.core.py /$HOME/
termux-reload-settings
rm /data/data/com.termux/files/usr/etc/motd
mv "$HOME/server" "$HOME/.os"
echo 
exit