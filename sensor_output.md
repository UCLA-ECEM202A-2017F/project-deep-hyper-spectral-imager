---
layout: default
title: Sensor data
description: Hyperspectral Output
---

# Sensor Outputs

## Device setup

   * The Intel RealSense SR300 camera is placed above the Matrix creator with the displacement of *8CM* as shown in the image below:

   ![Image_Setup](/Sound_Localisation/image_setup.jpg)

   * The Matrix Microphone array is placed such that the mic geometry is as shown below:

   ![Mic Geometry](/Sound_Localisation/Mic.png)

## Frame Size Calculations

1. Field of view: Intel Realsense
  * Vertical Field of View: 55 Deg
  * Horizontal field of View: 71.5 Deg
2. Field of view: Matrix
  * Azimuthal plane range: -pi/2 to pi/2
  * Polar plane range: -pi/2 to pi/2
3. Frame Size: 1.43mx1.04mx1m (Limited by IR camera) (Calculated using the field of view of the Intel Realsense Camera at Depth 1m). Depth is chosen as 1m as the Depth camera has a maximum range as 1.2m.
4. Displacement between the center of the IR camera and Matrix: 8cm

## Matrix Results

  * Source Location 1:

  ![Left_Acoular](/Sound_Localisation/Left_Acoular.png)

  * Source Location 2:

  ![Right_Acoular](/Sound_Localisation/Right_Acoular.png)

  * Source Location 3:

  ![Right_Down_Acoular](/Sound_Localisation/Right_Down_Acoular.png)

## Realsense IR Images

  * Source Location 1: (-0.56,0.50,0.75)m

  ![Left_IR](/RealSenseImages/ir_left.png)

  * Source Location 2: (0.58,0.58,0.6)m

  ![Right_IR](/RealSenseImages/ir_right.png)

  * Source Location 3: (0.27,-0.35,0.9)m

  ![Right_Down_IR](/RealSenseImages/ir_right_down.png)

## Realsense Depth Images

  * Source Location 1: (-0.56,0.50,0.75)m

  ![Left_depth](/RealSenseImages/d_left.png)

  * Source Location 2: (0.58,0.58,0.6)m

  ![Right_Depth](/RealSenseImages/d_right.png)

  * Source Location 3: (0.27,-0.35,0.9)m

  ![Right_Down_Depth](/RealSenseImages/d_right_down.png)
