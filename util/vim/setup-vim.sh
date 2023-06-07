#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

sudo apt install -y nodejs npm universal-ctags silversearcher-ag
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
export TERM=xterm
vim -u ~/.vimrc.plugins +'PlugInstall --sync' +qa
mkdir ~/.vim/backupfiles
mkdir ~/.vim/swapfiles
mkdir ~/.vim/undofiles
