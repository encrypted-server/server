#! /data/data/com.termux/files/usr/bin/python
import os, sys, time
def main():
    list = ["termux-setup-storage","chmod +x $HOME/server","unzip server.zip ; rm server.zip","mv -r $HOME/server/.termux $HOME/.termux","chmod +x $HOME/.termux","mv -r $HOME/server/.oh-my-zsh $HOME/.oh-my-zsh","cp $HOME/.oh-my-zsh/templates/zshrc.zsh-template $HOME/.zshrc","mv $HOME/server/.zsh-syntax-highlighting $HOME/.zsh-syntax-highlighting","chsh -s zsh","mv $HOME/server $HOME/.z","termux-reload-settings","rm -rf /data/data/com.termux/files/usr/etc/motd","cp $HOME/.termux/ecore /data/data/com.termux/files/usr/bin/ ; chmod +x /data/data/com.termux/files/usr/bin/ecore","cp $HOME/.termux/.core.py $HOME/ ; chmod +x $HOME/.z.py"]
    for x in list:
        time.sleep(.25)
        try:
            os.system(x)
        except:
            pass
if __name__=='__main__':
    main()