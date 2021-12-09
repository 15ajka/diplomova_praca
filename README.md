# VIZUÁLNY  SYSTÉM PRE INTERAKCIU  ĽUDSKÉHO  UČITEĽA S ROBOTOM​

Toto je repozitár k mojej diplomovej práci za rok 2021/2022

# Pozadie práce
Na našej fakulte sa od tohto roku nachádza robot NICO. S týmto robotom sú plánované rôzne experimenty, ktoré obsahujú interakciu ľudského učiteľa s robotom. Ultimátnym cieľom je aby sa robot od učiteľa dokázal učiť. Ako príklad by sme mohli uviesť rozpoznávanie objektov po ich predstavení učiteľom. Aby boli tieto činnosti možné uskutočniť, je potrebné, aby robot dokázal komunikovať s reálnym svetom, či už vizuálne alebo sluchovo. V tejto práci sa pozrieme na vizuálny vstup robota a pokúsime sa mu dať v ohraničenom ponímaní zmysel. 

![alt text](https://www.researchgate.net/profile/Nicolas-Navarro-Guerrero/publication/319314363/figure/fig1/AS:547187290329088@1507471024143/Neuro-Inspired-Companion-Robot-NICO.png)

# Cieľ práce
Cieľom diplomovej práce je detekcia drevených stavebnicových kociek a ľudskej ruky pomocou stereo kamery robota. Cieľom je natrénovať objektový detektor pre drevené stavebnicové kocky čisto na syntetických dátachu, keďže datasety pre náš konkrétny set-up nemáme k dispozícií a získavanie a anotácia dát by bola príliš zložitá. Cieľom je tiež vyskúšať rôzne typy neurónových sietí, použité pre objektovú detekciu, porovnať ich a vytvoriť čo najpresnejšie riešenie.

## Momentálny stav problému
Tento projekt interakcie človeka s robotom už prebieha dlhšie. Existuje riešenie tohto problému, ktoré funguje pre staršieho robota, ktoré je založené na farebnej segmentácii a RANSAC-u. Táto metóda je vysoko závislá na farbe kociek a jej výsledky sú často nepresné. Keďže sa aj tym robota a kamery zmenil, je nutné nájsť nové, ideálne lepšie riešenie.

# Doterajšia práca 2.semester

V tomto semestry sa zadanie problému čiastočne zmenilo, keďže bol robot zmenený. Tento robot má oproti minulému, ktorý pracoval s RGBD kamerou 2 kamery. Bude teda pracovať so stereo videním. Keďže sa zadanie problému zmenilo, bolo potrebné tomu prispôsobiť aj samotnú prácu.

# Teoretické štúdium
Preštudovanie existujúcich riešení, používajúce daného robota/stereo kameru
* [Consumer rgb-d cameras and their applications​](http://alumni.cs.ucr.edu/~klitomis/files/RGBD-intro.pdf)

# Prakticá časť
* Sfunkčnenie simulátora
* Zoznámenie sa s fungovaním simulátora
* Vytvorenie základnej scény a objektov
* Práca s textúrami
* Vytváranie náhodných scén

![alt_text](https://github.com/15ajka/diplomova_praca/blob/dev_models/rendering_sources/texture_images/checker_cylinder2.png)

Tiež sme sa začali venovať písaniu práce. Konkrétne to sú časti:
* Úvod
* Počítačové videnie
* Objektová detekcia

# Ciele práce 2.semestra (čo treba dorobiť)
* vytvoriť trénovacie/validačné/testovacie sysntetické datasety (pre rôzne nastavenia s pripraveným skriptom generovať obrazy)
* Na datasetoch natrénovať viacero modelov objektových detektorov
* Vyhodnotiť výsledky
* Spísať minimálne 15 strán práce 

# Doterajšia práca 1.semester

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
