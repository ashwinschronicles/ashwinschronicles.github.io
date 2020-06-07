[Extending desktop over VNC, the easy way](https://bbs.archlinux.org/viewtopic.php?id=191555) 

Hi all,

There have been some discussion over the Internet on how it would be possible to extend the desktop of your Linux computer over the network to some remote device. It is useful for example for using some random desktop computer or a tablet as the secondary screen for your laptop. (The users of multihead systems understand what a pain it is to be stuck with only single a monitor ![big_smile](https://bbs.archlinux.org/img/smilies/big_smile.png)) Unfortunately no good and simple ways have been found this far on how to do it.
For example Xdmx isn't really a plug and play solution, like connecting an external monitor, tools like Synergy do not provide real multihead support, but just enable you to control the remote computer using your mouse and keyboard and the xrandr -fb + x11vnc -clip method is ugly and does not appear to work correctly on recent systems.

Last night I was also thinking about the problem and came up with another soltution:
Because of a bug/feature in X/RandR/Intel driver/whatever it is possible to use the xrandr tool to enable a disconnected interfaces by manually setting display mode and then enabling them. From there on the idea is actually quite simple - you just extend your desktop to some disaplay interface that is not connected at the moment, like VGA1 for example and then just use x11vnc -clip to send the picture of the non-connected display to some other computer using the VNC protocol.

**Commands**
I will list the steps on how to make the following configuration:
\* The laptop screen is LVDS1
\* We are using the VGA1 output for the VNC server (no VGA monitor is connected)
\* The resolution of the VNC monitor will be 1280x1024
\* We are extending the desktop to the left of the laptop's screen

**Step 1:** Generate modeline for the resolution of the vpn screen you are going to use with your VNC display.
If xrandr already show the desired mode for any of the displays, generating a new one is not needed, we can use the existing one. If this is the case, you can jump directly to step 3.
Any random number can be used for the frequency, as we are not using the mode with any real monitor.

```
gtf 1280 1024 60
```

This command generates the following modeline:

```
Modeline "1280x1024_60.00"  108.88  1280 1360 1496 1712  1024 1025 1028 1060  -HSync +Vsync
```

**Step 2:** Generate a new mode based on the modeline we got from step 1.

```
xrandr --newmode "1280x1024_60.00"  108.88  1280 1360 1496 1712  1024 1025 1028 1060  -HSync +Vsync
```

**Step 3:** Add the desired mode to our disconnected output:

```
xrandr --addmode VGA1 1280x1024_60.00
```

**Step 4:** Enable the disconnected monitor using the newly added mode and use it to extend the desktop to the left of LVDS1:

```
xrandr --output VGA1 --mode 1280x1024_60.00 --left-of LVDS1
```

This extends your desktop to the invisible monitor on your left. At this point you can't see it's picture but you can move your mouse there and drag your windows there.

**Step 5:** Export the invisible part of your desktop using VNC

```
x11vnc -clip 1280x1024+0+0
```

**Step 6:** VNC viewer
Some kind of VNC viewer that supports showing the remote cursor is needed. For Arch client I was unable get this functionality to work in TigerVNC that is provided in the official repos, but TightVNC from AUR seems to work fine.
Also by doing some testing, I was able to find out that the tight encoding seems to be the best. Be sure to enable it.
To start the VNC viewer run this on the remote computer:

```
vncviewer -encodings "tight copyrect"
```

After that you are asked the ip address of the remote computer. (Note that the numbpad Enter does not seem to work there for some reason)

**Performance**
The testing was done using a local area network (VNC server and client connected to the the same router, server connected using WiFi, client connected using an Ethernet cable), VNC screen at 1280x1024 resolution and full colors, using the tight encoding.

To test it I tried showing a HD movie on the VNC screen. To my surprise, the movie was actually watchable, but not perfect as the framerate was still too low but it was enough to understand what's going on in the movie.
Also, as of right now, the VNC client is configured to display the remote cursor, which makes the cursor a bit laggy at times, so maybe it would be possible to use Synergy or something similar to directly control the cursor on the VNC viewer computer instead go get better cursor performance.

Also, as this solution uses a real video output for the VNC screen, the remote screen actually acts as a real monitor and you can drag windows easily between the screens and all windows maximized on the VNC display maximize only over that display, not over the entire X screen. Also you get a full hardware graphics acceleration on your VNC screen. True, the lag that VNC introduces to the screen kinda makes the acceleration useless, but at least you can have your transparent terminal ![tongue](https://bbs.archlinux.org/img/smilies/tongue.png)

**Drivers**
This trick works on the more or less recent Intel drivers on an Optimus/Bumblebee system. It would be fun to know if this trick is also repeatable using other drivers.

That's all, sorry for the long post and I hope someone finds it useful ![smile](https://bbs.archlinux.org/img/smilies/smile.png)