# VIZUÁLNY  SYSTÉM PRE INTERAKCIU  ĽUDSKÉHO  UČITEĽA S ROBOTOM​

Toto je repozitár obsahujúci stav diplomovej práce a dôležité linky. Práca je písana v rokoch 2021/2022

# Pozadie práce
Na našej fakulte sa už dlhšiu dobu zaoberáme experimentami, ktoré obsahujú interakciu ľudského učiteľa s robotom. Ultimátnym cieľom je, aby sa robot od učiteľa dokázal učiť rôznym zručnostiam. Ako príklad by sme mohli uviesť rozpoznávanie objektov robotom po ich ukážke a pomenovanú učiteľom. Aby boli tieto činnosti možné uskutočniť, je potrebné, aby robot dokázal komunikovať s reálnym svetom, či už vizuálne alebo sluchovo. V tejto práci sa pozrieme na vizuálnu časť tohto problému a pokúsime sa robotovi z kamerového vstupu poskytnúť čo najelpšie informácie v rámci skúmaného problému. Konkrétne budeme pracovať s robotom NICO, ktorého môžeme vidieť na obrázku.

![alt text](https://www.researchgate.net/profile/Nicolas-Navarro-Guerrero/publication/319314363/figure/fig1/AS:547187290329088@1507471024143/Neuro-Inspired-Companion-Robot-NICO.png)

# Cieľ práce
Cieľom diplomovej práce je detekcia drevených stavebnicových kociek a ľudskej ruky pomocou stereo kamery robota. Cieľom je natrénovať objektový detektor pre drevené stavebnicové kocky čisto na syntetických dátachu, keďže datasety pre náš konkrétny set-up nemáme k dispozícií. Získavanie a anotácia dát by bola príliš zložitá a zdĺhavá. Cieľom je tiež vyskúšať rôzne typy neurónových sietí, použité pre objektovú detekciu. Chceme ich porovnať a vytvoriť čo najlepšie riešenie.

## Momentálny stav problému
Tento projekt interakcie človeka s robotom už prebieha dlhšie. Existuje riešenie tohto problému, ktoré funguje pre staršieho robota, ktoré je založené na farebnej segmentácii a RANSAC-u. Táto metóda je vysoko závislá na farbe kociek a jej výsledky sú často nepresné. Keďže sa robot a typ kamery zmenili, je nutné nájsť nové, ideálne lepšie riešenie.

# Doterajšia práca 2.semester

V tomto semestry sa zadanie problému čiastočne zmenilo, preto bolo potrebné sa prispôsobiť. Tento robot má oproti minulému, ktorý pracoval s RGBD kamerou 2 kamery. Bude teda potrebné pracovať so stereo videním. Istú časť semestra sme preto venovali teoretickému štúdiu a návrhu riešenia.

# Teoretické štúdium
Preštudovanie existujúcich riešení, používajúce daného robota/stereo kamery.
* [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World​](https://arxiv.org/abs/1703.06907)
* [Weakly-Supervised Object Detection Learning through Human-Robot Interaction](https://ieeexplore.ieee.org/document/9555781)
* [EPOS: Estimating 6D Pose of Objects with Symmetries](http://cmp.felk.cvut.cz/epos/)
* [Deep Object Pose Estimation for Semantic Robotic Grasping of Household Objects](https://arxiv.org/abs/1809.10790)

Následne sme zo spomínaných riešení vybrali jeden článok, ktorý bude hlavným zdrojom pri tvorení nášho riešenia. Bol to konkrétne prvý spomínaný članok, ktorý sme vybrali kvôli tomu, že pri trénovaní nevyužíval žiadne dáta z reálneho sveta. Keďže tento článok používa staršiu architektúru siete a zároveň vytvára jeden objektový detektor pre každý objekt, túto časť článku sa chystáme nahradiť iným riešením. Konkrétny postup je ešte v procese skúmania.

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
