## PyGame 

Pygame is usually straightforward to install, but it can get tricky depending on your operating system and the version of Python you have installed. These instructions can help you get Pygame installed quickly, so you can focus on building games.

- [Pygame on Linux](#pygame-on-linux)
- [Pygame on OS X](#pygame-on-os-x)
- [Pygame on Windows](#pygame-on-windows)

### Python 3

Setting up Pygame for Python 3 is a two-step process; first you'll install some packages that Pygame depends on, then you'll download and install Pygame.

Run the following commands to install the packages required to run Alien Invasion. (If you use a command such as `python3.5` on your system, replace `python3-dev` with `python3.5-dev`):

    $ sudo apt-get install python3-dev mercurial
    $ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

If you want to enable some more advanced functionality in Pygame such as the ability to add sounds, you can also install the following libraries:

    $ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
    $ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
    $ sudo apt-get install python-numpy

You'll need pip for the next step; if you haven't set up pip yet, see the [instructions for seting up pip](installing_pip.md). Enter the following to install Pygame:

    $ pip install --user hg+http://bitbucket.org/pygame/pygame

The output will pause for a moment, informing you which libraries were found. Press **Enter**, even if there are some libraries missing. You should see a message that Pygame installed successfully. To confirm the installation was successful, start a Python terminal session and try to import Pygame by entering the following:

    $ python3
    >>> import pygame
    >>>

If you see no error messages, you're ready to start working on Alien Invasion!

<a href='pygame_osx'></a>Pygame on OS X
---

You'll need [Homebrew](http://brew.sh) to install some packages that Pygame depends on.

To install the libraries that Pygame depends on, enter the following:

    $ brew install hg sdl sdl_image sdl_ttf

This installs the minimum number of packages needed to run Alien Invasion. If you want Pygame to have a little more functionality such as working with sound, you can install two additional libraries:

    $ brew install sdl_mixer portmidi

You'll need [pip](installing_pip.md) to install Pygame. Once you have pip set up correctly, issue the following command:

    $ pip3 install --user  hg+http://bitbucket.org/pygame/pygame

To confirm the installation, start a Python terminal session and try to import Pygame:

    $ python3
    >>> import pygame
    >>>

If this works, you're ready to start building Alien Invasion!