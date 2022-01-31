# VIZUÁLNY  SYSTÉM PRE INTERAKCIU  ĽUDSKÉHO  UČITEĽA S ROBOTOM​

Toto je repozitár obsahujúci stav diplomovej práce a dôležité linky. Práca je písana v rokoch 2021/2022

# Pozadie práce
Na našej fakulte sa už dlhšiu dobu zaoberáme experimentami, ktoré obsahujú interakciu ľudského učiteľa s robotom. Ultimátnym cieľom je, aby sa robot od učiteľa dokázal učiť rôznym zručnostiam. Ako príklad by sme mohli uviesť rozpoznávanie objektov robotom po ich ukážke a pomenovanú učiteľom. Aby boli tieto činnosti možné uskutočniť, je potrebné, aby robot dokázal komunikovať s reálnym svetom, či už vizuálne alebo sluchovo. V tejto práci sa pozrieme na vizuálnu časť tohto problému a pokúsime sa robotovi z kamerového vstupu poskytnúť čo najelpšie informácie v rámci skúmaného problému. Konkrétne budeme pracovať s robotom NICO, ktorého môžeme vidieť na obrázku.

![alt text](https://www.researchgate.net/profile/Nicolas-Navarro-Guerrero/publication/319314363/figure/fig1/AS:547187290329088@1507471024143/Neuro-Inspired-Companion-Robot-NICO.png)

# Cieľ práce
Táto diplomová práca má viacero cieľov:
* 3D objektová detekcia drevených stavebnicových kociek
* Vytvorenie syntetického datasetu na tréning detektora
* Natrénovanie objektového detektora
* Vytvorenie reálneho datasetu na testovanie riešenie
* Vyhodnotenie testovacích metrík

## Momentálny stav problému
Tento projekt interakcie človeka s robotom už prebieha dlhšie. Existuje riešenie tohto problému, ktoré funguje pre staršieho robota, ktoré je založené na farebnej segmentácii a RANSAC-u. Táto metóda je vysoko závislá na farbe kociek a jej výsledky sú často nepresné. Keďže sa robot a typ kamery sa zmenili, je nutné nájsť nové, ideálne lepšie riešenie.

# Doterajšia práca 2.ročník, 1.semester
V tomto semestry sa zadanie problému čiastočne zmenilo, preto bolo potrebné sa prispôsobiť. Tento robot má 2 kamery, ktoré poskytujú využitie stereovidenia. Minulí robot narozdiel od toho pracoval s jednou RGBD kamerou. Nebude teda možné pracovať s hĺbkovým obrazom a bude možnosť využiť stereovidenie. Aktívne sme sa začali venovať praktickej časti diplomovej práce. Zhodnotili sme aktuálne prístupné vstupy a výstupy, situáciu na fakulte a existujúce riešenia a navrhli sme postup práce pre tento a ďalší semester.

# Teoretické štúdium
Doštudovanie článkov týkajúcich sa teoretického zázemia práce a lepšie preskúmanie riešení, ktoré by sme vedeli pri práci využiť.
* [Understanding of a convolutional neural network](https://ieeexplore.ieee.org/abstract/document/8308186)
* [Computer vision: algorithms and applications](https://books.google.sk/books?hl=sk&lr=&id=bXzAlkODwa8C&oi=fnd&pg=PR4&dq=Computer+vision:+algorithms+and+applications&ots=g--5aZqGEH&sig=ys7UlVYdqmcTchGUDDDB8GAyna4&redir_esc=y#v=onepage&q=Computer%20vision%3A%20algorithms%20and%20applications&f=false)
* [Pixor: Real-time 3d object detection from point clouds](https://openaccess.thecvf.com/content_cvpr_2018/html/Yang_PIXOR_Real-Time_3D_CVPR_2018_paper.html)
* [Object detection in 20 years: A survey](https://arxiv.org/abs/1905.05055)
* [Image features detection, description and matching](https://link.springer.com/chapter/10.1007/978-3-319-28854-3_2)
* [NViSII: A Scriptable Tool for Photorealistic Image Generation](https://arxiv.org/abs/2105.13962)
* [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World​](https://arxiv.org/abs/1703.06907)
* [Deep Object Pose Estimation for Semantic Robotic Grasping of Household Objects](https://arxiv.org/abs/1809.10790)

# Praktická časť
* Rozbehanie simulátora pre renderovanie jednoduchých obrazov
* Zoznámenie sa s fungovaním simulátora, vytvorenie základnej scény, objektov, práca s textúrami, randomizácia prostredia
* Vytváranie náhodných scén - [ukážka scény 1](https://github.com/15ajka/diplomova_praca/blob/camera_movement/rendering_sources/dataset_images/scene_14.png), [ukážka scény 2](https://github.com/15ajka/diplomova_praca/blob/camera_movement/rendering_sources/dataset_images/scene_29.png)
* Rozbehanie DOPE generátora dát
* Vygenerovanie prvých datasetov pre tréning - [ukážka scény s veľa kockami](https://github.com/15ajka/diplomova_praca/blob/gcloud2/gcloud/dataset/000/00001.png), [ukážka scény s jednou kockou](https://github.com/15ajka/diplomova_praca/blob/one_img/gcloud/026/00001.png), [ukážka scény s farebnými kockami](https://github.com/15ajka/diplomova_praca/blob/green_4cubes/gcloud/dataset4_g/000/00001.png)
* Rozbehanie trénovanie DOPE CNN
* Trénovanie na jednoduchých datasetoch - [ukážka výsledku natrénovanej siete](https://github.com/15ajka/diplomova_praca/blob/one_img/gcloud/inference_dataset4_val/00003.png.png)

# Postup práce 2.ročník, 2.semestra
* Vytvoriť rozsiahlejšie/variabilnejšie syntetické datasety
* Vytvoriť program na rátanie metrík výsledkov
* Trénovanie siete na rozsiahlejších datasetoch
* Vyhodnotenie siete na syntetických dátach
* Vytvorenie malého datasetu z reálneho sveta
* Určenie metrík na reálnom datasete
* Písanie časti práce: Výskum

# Doterajšia práca 1.ročník, 2.semester

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
