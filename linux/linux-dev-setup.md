## shell

login shell, `/etc/passwd`

`.inputrc`, `.bashrc`

fzf

### fish

### zsh

`~/.zshrc`

oh-my-zsh, powerlevel10k, autojump, zsh-autosuggestions

## apt

`/etc/apt/source.list`

## tools

### search

ripgrep, fd, ag

```sh
# rg
curl -LO https://github.com/BurntSushi/ripgrep/releases/download/12.1.1/ripgrep_12.1.1_amd64.deb
sudo dpkg -i ripgrep_12.1.1_amd64.deb

# fd
wget https://github.com/sharkdp/fd/releases/download/v8.2.1/fd-musl_8.2.1_amd64.deb
sudo dpkg -i fd-musl_8.2.1_amd64.deb

# ag
sudo apt-get install silversearcher-ag
```

### build

gcc, llvm, python, node, java

configure package manager with domestic source

```sh
apt install build-essential cmake
```

### code navigation

ctags, cscope, global

```sh
sudo apt install exuberant-ctags cscope global
```

## vim

latest neovim and vim, guide from youCompleteMe

https://github.com/ycm-core/YouCompleteMe/wiki/Building-Vim-from-source

```sh
# neovim
wget https://github.com/neovim/neovim/releases/download/v0.4.4/nvim.appimage
sudo mv /usr/bin/nvim /usr/bin/nvim-bak
sudo ln -s ./nvim.appimage /usr/bin/nvim

# vim
# 1. prerequisite libraries
sudo apt install libncurses5-dev libgtk2.0-dev libatk1.0-dev libcairo2-dev libx11-dev libxpm-dev libxt-dev python3-dev ruby-dev lua5.2 liblua5.2-dev libperl-dev git
# 2. Remove vim if you have it already.
sudo apt remove vim vim-runtime gvim
# 3. build
./configure --with-features=huge \
            --enable-multibyte \
            --enable-rubyinterp=yes \
            --enable-python3interp=yes \
            --with-python3-config-dir=$(python3-config --configdir) \
            --enable-perlinterp=yes \
            --enable-luainterp=yes \
            --enable-cscope \
            --prefix=/usr/local

make VIMRUNTIMEDIR=/usr/local/share/vim/vim82
make install

# 4. Set vim as your default editor with update-alternatives.
sudo update-alternatives --install /usr/bin/editor editor /usr/local/bin/vim 1
sudo update-alternatives --set editor /usr/local/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /usr/local/bin/vim 1
sudo update-alternatives --set vi /usr/local/bin/vim

sudo update-alternatives --install /usr/bin/vim vim /usr/local/bin/vim 1
sudo update-alternatives --set vim /usr/local/bin/vim
```

## neovim