---
title: Extending Desktop to another device over VNC 
date: 2020-02-05
tags: VNC,Nomachine,Extend desktop,Linux
category: Blog
subtitle: in Arch Linux
slug: extending-desktop-to-another-device-over-vnc
author: Ashwin
summary: This post details the procedure to Extending Desktop to another device over VNC or other protocol in Linux
keywords: VNC,Nomachine,Extend desktop,linux
gittime: off

---

If you have an old tablet or old laptop, you might want to put it to good use by using its display as a secondary screen to your primary laptop. If you are using windows on your primary laptop, you have a host of applications that does this for you (like Builtin windows Wireless display, Synergy) but if you are using linux you can follow the following instructions.

**Assumptions**
I will list the steps on how to get it done wit the following configuration:

* The laptop screen is eDP-1
*  We are using the VIRTUAL1 output for the VNC server
* The resolution of the VNC monitor will be 1920x1080
* We are extending the desktop to the right of the laptop's screen

**Step 1:** Generate modeline for the resolution of the vpn screen you are going to use with your VNC display.
If xrandr already show the desired mode for any of the displays, generating a new one is not needed, we can use the existing one. If this is the case, you can jump directly to step 3.
Any random number can be used for the frequency, as we are not using the mode with any real monitor.

```bash
gtf 1920 1080 60
```

This command generates the following modeline:

```bash
 # 1920x1080 @ 60.00 Hz (GTF) hsync: 67.08 kHz; pclk: 172.80 MHz
  Modeline "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
```

**Step 2:** Generate a new mode based on the modeline we got from step 1.

```bash
xrandr --newmode "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
```

**Step 3:** Add the desired mode to our disconnected output:

```bash
xrandr --addmode VIRTUAL1 1920x1080_60.00
```

**Step 4:** Enable the disconnected monitor using the newly added mode and use it to extend the desktop to the right of eDP1:

```bash
xrandr --output VIRTUAL1 --mode 1920x1080_60.00 --right-of eDP1
```

This extends your desktop to the invisible monitor on your left. At this point you can't see it's picture but you can move your mouse there and drag your windows there. if your hardware dosnet support VIRTUAL1, you can also use VGA1  instead of VIRTUAL1

**Step 5:** Run xrandr to check if the new setup is listed.

**Step 6:** Export the invisible part of your desktop using VNC

```bash
x11vnc -clip 1920x1080+1920+0 
```

**Step 7:** VNC viewer
Some kind of VNC viewer that supports showing the remote cursor is needed on your secondary laptop / tablet.

Both of them needs to be on the same network and they need to be discover-able. After that you are asked the ip address of the remote computer. If your not happy with the performance of the setup you can use **NoMachine** instead of VNC viewer, it uses NX protocoal and seems to be better optimised for low bandwidth and low performance device (the secondary laptop).
This trick works on the more or less recent Intel drivers on an Optimus/Bumblebee system. It would be fun to know if this trick is also repeatable using other drivers. 



Once this is setup the parameters can be set in as a bash script

```bash
#!/bin/bash
#contents of virtual_display_to_right.sh
xrandr --newmode "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
xrandr --addmode VIRTUAL1 1920x1080_60.00
xrandr --output VIRTUAL1 --mode 1920x1080_60.00 --right-of eDP1
xrandr
x11vnc -clip 1920x1080+1920+0 
```

