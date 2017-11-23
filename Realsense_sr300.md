---
layout: default
title: Time of flight
description: Implementation
---

# 3. Depth Imaging Using Intel RealSense SR300 Camera

* Depth Sensing is carried out commonly with the help of IR projector and the IR camera. The principle behind the depth sensing can be summarized as follows:
  + The IR projectors shoots the irregular pattern of dots of IR wavelength over the space. The   Projector has a Diffractive optical element which forms irregular patterns of dot.
  + The IR camera capable of recording the infrared light. The infrared light falling on the objects bounces back with different intensities, which is captured by the IR camera.
  + Finally the image captured by the IR camera and the irregular pattern of dots that was initially projected is compared to find the depth.
* The Commonly used cameras are RGB-D cameras which capture the RGB images along with the per pixel depth information.

## Implementation

We propose the use of Intel RealSense SR300 camera for depth sensing.
[Installing RealSense Library on Jetson TX2](http://www.jetsonhacks.com/2017/03/26/intel-realsense-camera-installation-nvidia-jetson-tx2/)

![RealSense](sr300.jpg)

## Literature Survey

Depth sensing technology is currently used in widespread applications like 3D indoor mapping, Augmented Reality, Medical imaging and object detection. [1] talks about basic RGBD mapping for an indoor environment while [2] talks about the the real time human detection in the dynamically cluttered environment. [3] suggests pose detection using the depth sensors.

* [1]Peter Henry, Micheal Krainin, Evan Herbst, Xiaofeng Ren, Dieter Fox, “ RGB-D mapping : Using Kinect- style depth cameras for dense   #D modelling of indoor environments”.
* [2] Jingwen Zhao, Guyue Zhang, Luchao Tian, Yan Qiu Chen, “REAL-TIME HUMAN DETECTION WITH DEPTH CAMERA VIA A PHYSICAL RADIUS-DEPTH       DETECTOR AND A CNN DESCRIPTOR”
* [3] Noel S. Kropf, Mattias Marder, Charles F Wiecha, “Pose detection using depth camera”.
