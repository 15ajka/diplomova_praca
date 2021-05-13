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
* Consumer rgb-d cameras and their applications​
* An Overview Of 3D Object Detection​
* RGB-D image-based Object Detection: from Traditional Methods to Deep Learning Techniques
* Objects as Points
* PIXOR: Real-time 3D Object Detection from Point Clouds​
* Deep Object Pose Estimation for Semantic Robotic Grasping of Household Objects
* Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World​

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
