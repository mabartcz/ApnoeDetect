![](media/image1.tiff){width="2.1149431321084866in"
height="1.1448687664041994in"}**ApnoeDetect**

*"Simple software for automatic sleep apnea and oxygen desaturation
detection based on neural networks for EASYS2 .d files"*

**Authors:**

-   Martin Bartoň

-   Vlastimil Koudelka

**Description**

This experimental program can detect decrees in airflow and decrees in
oxygen the main features of sleep apnea. The main advantage is that,
detection algorithm is made by convolution neural network and this
network was learned from previously scored data by the doctors from
NUDZ. The program is working with ".d" files from EASYS2 Brainscope. The
tags are saved into new copied file.

**Technical requirements**

-   Python 3.6 with libraries:

    -   Keras 2.3.1

    -   Tensorflow 2.0.0

    -   AppJar 0.94.0

    -   Numpy 1.18.0

    -   Scipy 1.4.1

    -   Struct

    -   Window\_slider 0.8

    -   Collections

    -   Pytictoc

    -   Shutil

> (all available from pip: <https://pypi.org/>)

-   Input data -- ".d" file with flow and SpO~2~ signal.

If you are new to python environment follow:
<https://wiki.python.org/moin/BeginnersGuide>

On windows a recommend using python portable:

<http://winpython.github.io/>

or Anaconda:

<https://www.anaconda.com/>

In case of error or any questions please contact me on
<ma.barton@seznam.cz>

This detector is not final product. We are still working on
improvements.\
**How to use ApnoeDetect**

1)  Launch file *AD\_GUI.py* with installed python3.

2)  The application will pop up window.

![](media/image2.png){width="6.295833333333333in"
height="3.3819444444444446in"}

3)  Click on "*Add file*". The classic dialog window for file selection
    will show up. Select your file with suffix ".d".

![](media/image3.png){width="6.295833333333333in"
height="3.408333333333333in"}

4)  Name of your file will show up in the window. Check if it is
    correct.

5)  Click on *"Analyze"* . After that the copy of the original file will
    be created in the same location with suffix *"\_AUTO".* Than process
    of detection will start. There is no loading bar available, but you
    can track progress in console. The detection process may be long
    (few minutes based on computation power).

![](media/image4.png){width="6.295833333333333in"
height="3.3965277777777776in"}

6)  After detection is done, the tags will be saved into copied file. On
    screen you will see results. Than you can close the window.

7)  Example viewed in EEGviewer.

![](media/image5.png){width="6.295833333333333in"
height="3.6104166666666666in"}
