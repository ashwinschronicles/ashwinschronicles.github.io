---
Title:Interfacing Arduino Mega using LabVIEW
Date: 2017-12-15
Tags: Arduino,LabVIEW,Review
Category:Engineering
Slug:arduino-labview-review
Author: Ashwin
Summary: This post is about Interfacing Arduino Mega with LabVIEW
gittime: off
---

This post is about Interfacing Arduino Mega using LabVIEW. It was originally posted [here](https://www.element14.com/community/roadTestReviews/2581/l/arduino-a000067-mega2560-rev3-development-board-review) as a part of element14’s RoadTest. I thank element14 for sending me the review unit.

- **Evaluation Type:** Independent Products

- **Was everything in the box required?:** Yes

- **Comparable Products/Other parts you considered:** Arduino due , Raspberry Pi

- **What were the biggest problems encountered?:** When arduino ide is running, other programs such as Labview cant programme the mega.This is true in general of all arduino device.The only solution i found was to close arduino ide , log off and then log back in.

- 

- Detailed Review:

  Arduino Mega the big brother of Arduino Uno has 54 digital I/O pins, 16 analogue inputs. That's a whopping difference of 40 digital and 10 analogue pins.the closest to it in the Arduino family is the Arduino Due.

  Arduino mega is generally used for projects that require a high number of I/O and memory thus they are commonly found in 3D printers and robotics projects.

   

  LabView is a system-design platform that allows you to visually write a program.It is generally used by engineers and scientists to create programs to automate the process of data acquisition from lab instruments. In this review, i try to Arduino mega to interface between the LabVIEW software and an instrument.

   

   

   

  ## Part 1: Installing LabVIEW and NI-VISA.

   

  Go to [www.ni.com/trylabview](https://www.element14.com/community/external-link.jspa?url=http%3A%2F%2Fwww.ni.com%2Ftrylabview)

   

  Click on Download LabVIEW.

   

  Right-Click and then run LabVIEW Setup as administrator.

   

  Follow the instructions and wait for the installation to finish

   

  Note: You might get an error while installing Click on decline support as you do not have any device drivers. We have to download driver later.

   

  LabVIEW 2017 is successfully installed.

   

  Restart system later if prompted for a restart.

   

  To download NI-VISA driver for serial communication go to [https://www.ni.com/visa/](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fwww.ni.com%2Fvisa%2F) and download the appropriate version of the software, Install it in the same way as before.

   

   Labview has so many addons both by a 3rd party and NI itself that by default the software comes with a few basic tool set. This set can be expanded by installing add-ons, we shall now look into the process of installing the Arduino interfacing addon.

   

  Open the VI Package Manager and wait for it to download all the repository (this could take several minutes depending on your bandwidth)

   

  Search for "Arduino" in the search bar.

   

  Install Digilent LINX and "LabVIEW Interface for Arduino".

   

  Once the installation is done without any errors you should Notice an "installed" symbol to the left of Digilent LINX toolbox, click finish.

  [![img](https://www.element14.com/community/servlet/JiveServlet/downloadImage/293607990-2581-494997/Screenshot+%282%29.png)](https://www.element14.com/community/servlet/JiveServlet/showImage/293607990-2581-494997/Screenshot+(2).png)

  In order to verify if all softwares are installed correctly, Open LabVIEW.Click on File > New VI.

  On one the panels, click on Window > Tile Left and Right. Right-click on the block diagram, scroll down to see that Arduino (LabView interface for Arduino: LIFA) and LINX is installed.

   

  ### **Uploading LabView Interface for Arduino Firmware**

  In order to interface Arduino with the LabView, we need to upload a sketch that acts as a firmware.

  For that make sure that you have Arduino ide already installed

   

  Open the arduino ide and upload the sketch that has the path:

  C:\Program Files (x86)\ National Instruments\

  LabVIEW 2017\ vi.lib\ LabVIEW Interface for Arduino\ Firmware\ LIFA_Base\ LIFA_Base.ino

  [![img](https://www.element14.com/community/servlet/JiveServlet/downloadImage/293607990-2581-494998/Screenshot+%284%29.png)](https://www.element14.com/community/servlet/JiveServlet/showImage/293607990-2581-494998/Screenshot+(4).png)

  (adjust the path based on the installation location of the LabView)

  Check for Board type and COM Port under Tools menu

   

  NOTE: Do not upload any code to Arduino Board

  hereafter. Arduino Board with LIFA_Base firmware is now ready to be used with LabVIEW 2017.

   

  ## **PART 2: Interfacing and Controlling an LED using LabVIEW, Arduino and LIFA**

  The hello world equivalent in Arduino is an LED blink sketch, let us look at the implementation of led blink in LabView. Every program in LabVIEW is called a VI it ends with an extension dot VI click.

  On creating a new project in Labview you will see two windows opening the first one has a front panel and the second one is the block diagram

  [![img](https://www.element14.com/community/servlet/JiveServlet/downloadImage/293607990-2581-495107/Screenshot+%283%29.png)](https://www.element14.com/community/servlet/JiveServlet/showImage/293607990-2581-495107/Screenshot+(3).png)

  the front panel will usually house all kinds of numeric controls knobs dials meters gauge

  boolean buttons LED graphs charts indicators and the block diagram will have all programming tools structures numeric functions like addition subtraction boolean functions etc.

   

  now what we have to start with is right click on the block diagram scroll down to Arduino.

  For this particular program, we need four major functions to control led. Initialization, Set digital pin mode (analogous to pinMode), digital write and Close.

  to know what each of these functions does or what each of these blocks does click on it and press on the question mark on the right corner which is called as context help context help will explain what each of these blocks does and what has to be connected to each of these terminals.

  For example, in initialization, the first option is visa resource that is where you specify which

  communication port your Arduino is connected to say COM4 port for example

  second, you specify the baud rate (whatever is in the bracket is by default so

   

  you don't have to specify it again) Board type would be Mega.

  Now let us think about the flow of the program, first the led will be initialised as output then its is set high and then the loop continues till an event triggers the end. We represent the flow of the program in LabView in the same way. The following would be the possible connection in the flow.

  [![img](https://www.element14.com/community/servlet/JiveServlet/downloadImage/293607990-2581-495108/Screenshot+%286%29.png)](https://www.element14.com/community/servlet/JiveServlet/showImage/293607990-2581-495108/Screenshot+(6).png)

  Error out pin of initialisation module is wired in series to an error in pin of digital pin mode and digital write and finally the close module. The same arrangement is made with Arduino resource pin of each module.

  the pin number is set by creating a constant at the io pin of the pinmode module and setting its value to 13 and output.The value of 0 1 at the value point in digital write module is equivalent to the High and Low mode.

  Now to set the loop right click go to programming > structure find the while loop module and draw a square around the digitalwrite module (the one we want to repeat). set the constitutional terminal to a boolean control such as a button in the front end editor.

  Now the program is complete. Click on run program.

   

  This exercise demonstrates how Arduino can be used to interface a device(an led in this case) using Labview.

### Scoring

| **Product Performed to Expectations:**             | 10      |
| -------------------------------------------------- | ------- |
| **Specifications were sufficient to design with:** | 10      |
| **Demo Software was of good quality:**             | 10      |
| **Product was easy to use:**                       | 10      |
| **Support materials were available:**              | 10      |
| **The price to performance ratio was good:**       | 9       |
|                                                    |         |
| **TotalScore:**                                    | 59 / 60 |