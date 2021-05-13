# VIZUÁLNY  SYSTÉM PRE INTERAKCIU  ĽUDSKÉHO  UČITEĽA S ROBOTOM​

Toto je repozitár k mojej diplomovej práci za rok 2021/2022

# Cieľ práce
Detekcia kociek a ľudskej ruky pomocou RGBD kamery. Cieľom je využiť neurónovú sieť a vytvorenie syntetického datasetu pre trénovanie tejto siete.

## Momentálne riešenie
Existuje momentálne riešenie tohto problému, ktoré je založené na farebnej segmentácii a RANSAC-u. Táto metóda je napr. závislá na farbe kociek a jej výsledky nie sú ideálne. Preto hľadáme lepšie riešenie.

# Doterajšia práca

Oblasti počítačového videnia venujem iba krátku dobu. Preto som sa tento semester zamerala na naštudovanie základov počítačového videnia a spracovania. Tiež som študovala pokročilejšie techniky a články zaoberajúce sa tematikou mojej práce. 

## Teoretické štúdium
V tomto semestry som si naštudovala základy pre:
* RGBD kamera​
* BAG formát  súborov​
* Point cloud​
* CNN

Naštudované články:
* [Consumer rgb-d cameras and their applications​](http://alumni.cs.ucr.edu/~klitomis/files/RGBD-intro.pdf)
* [An Overview Of 3D Object Detection​](https://arxiv.org/abs/2010.15614)
* [RGB-D image-based Object Detection: from Traditional Methods to Deep Learning Techniques](https://arxiv.org/abs/1907.09236)
* [Objects as Points](https://arxiv.org/abs/1904.07850)
* [PIXOR: Real-time 3D Object Detection from Point Clouds​](https://arxiv.org/abs/1902.06326)
* [Deep Object Pose Estimation for Semantic Robotic Grasping of Household Objects](https://arxiv.org/abs/1809.10790)
* [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World​](https://arxiv.org/abs/1703.06907)

## Praktická práca
- Naštudovanie  práce s ROS - The Robot Operating System – práca s BAG​
  -   Zobrazovanie  vstupných  dát​
  -   Extrakcia  rgb a hĺbkových  obrazov​
    
-   Nainštalovanie  potrebného  softvéru​
    -   Ros-kinetic​
    -   Catkin​
    -   Intel Realsense SDK 2.0​
    -   Python knižnice (pyrealsense2, python-opencv, ...)​
    
-   Rozbehanie  existujúceho  riešenia​

# Súbory
Obrázky príkladov vstupných dát môžete vidieť v priečinku output.
