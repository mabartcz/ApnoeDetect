<h1>ApnoeDetect</h1>

*"Simple software for automatic sleep apnea and oxygen desaturation
detection based on neural networks for EASYS2 .d files"*

<h2>Authors:</h2>

-   Martin Bartoň

-   Vlastimil Koudelka

<h2>Description</h2>

This experimental program can detect decrees in airflow and decrees in
oxygen the main features of sleep apnea. The main advantage is that,
detection algorithm is made by convolution neural network and this
network was learned from previously scored data by the doctors from
NUDZ. The program is working with ".d" files from EASYS2 Brainscope. The
tags are saved into new copied file.

<h2>Technical requirements</h2>

-   Python 3.6 with libraries:

    -   Keras 2.3.1

    -   Tensorflow 2.0.0

    -   AppJar 0.94.0

    -   Numpy 1.18.0

    -   Scipy 1.4.1

    -   Struct

    -   Window_slider 0.8

    -   Collections

    -   Pytictoc

    -   Shutil

> (all available from pip: <https://pypi.org/>)

-   Input data = ".d" file with flow and SpO2 signal.

If you are new to python environment follow:
<https://wiki.python.org/moin/BeginnersGuide>

On windows a recommend using python portable:

<http://winpython.github.io/>

or Anaconda:

<https://www.anaconda.com/>

In case of error or any questions please contact me on
<ma.barton@seznam.cz>

This detector is not final product. We are still working on
improvements
<h2>How to use ApnoeDetect</h2>

1)  Launch file *AD\_GUI.py* with installed python3.

2)  The application will pop up window.

![](https://github.com/mabartcz/ApnoeDetect/blob/master/screens/AD_1.png?raw=true)

3)  Click on "*Add file*". The classic dialog window for file selection
    will show up. Select your file with suffix ".d".

![](https://github.com/mabartcz/ApnoeDetect/blob/master/screens/AD_2.png?raw=true)

4)  Name of your file will show up in the window. Check if it is
    correct.

5)  Click on *"Analyze"* . After that the copy of the original file will
    be created in the same location with suffix *"\_AUTO".* Than process
    of detection will start. There is no loading bar available, but you
    can track progress in console. The detection process may be long
    (few minutes based on computation power).

![](https://github.com/mabartcz/ApnoeDetect/blob/master/screens/AD_3.png?raw=true)

6)  After detection is done, the tags will be saved into copied file. On
    screen you will see results. Than you can close the window.

7)  Example viewed in EEGviewer.

![](https://github.com/mabartcz/ApnoeDetect/blob/master/screens/EEGviewer.png?raw=true)
