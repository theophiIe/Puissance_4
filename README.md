# Puissance_4

## Arborescence
Notre application se découpe en plusieurs dossiers :
- assets, qui contient les fichiers image et son,
- data, qui contient le dossier contenant les sauvegardes de parties,
- scripts, qui contient les scripts pour l'installation des dépendances pour Windows, MacOS et Linux,
- src, qui contient tous les fichiers source de notre application,
- executable_windows, qui contient tous les fichiers et dossiers nécessaires à l'exécution du fichier `main.exe` sous Windows,
- executable_linux, qui contient tous les fichiers et dossiers nécessaires à l'exécution du fichier `main` sous Linux,
- executable_mac, qui contient tous les fichiers et dossiers nécessaires à l'exécution du fichier `main` sous Mac,
- un fichier main.py, qui permet le lancement de l'application,
- un fichier Makefile,
- un fichier README.md.

## Dépendances
Les dépendances obligatoires au bon fonctionnement de l'application sont : 
-python3 (version supérieure à 3.6.9),
-pip3.

Les dépendances supplémentaires sont :
-numpy,
-pygame (sous la version 2.0.0dev6 pour MacOS).

Pour l'installation de numpy et de pygame, voir ci-dessous.

### Linux
Afin d'installer les dépendances nécessaires au bon fonctionnement de l'application, se placer dans le dossier Puissance_4,
ouvrir un terminal et exécuter la commande ```make install_linux```, ou se placer dans le dossier scripts, ouvrir un terminal,
et exécuter la commande ```sudo ./setupLinux.sh```.

### MacOS
Afin d'installer les dépendances nécessaires au bon fonctionnement de l'application, se placer dans le dossier Puissance_4,
ouvrir un terminal et exécuter la commande ```make install_mac```, ou se placer dans le dossier scripts, ouvrir un terminal,
et exécuter la commande ```sudo ./setupMac.sh```.

### Windows

Afin d'installer les dépendances nécessaires au bon fonctionnement de l'application, se placer dans le dossier scripts,
ouvrir un terminal, et exécuter la commande ```./setup.bat```.


## Exécution
### Linux
Pour exécuter le programme depuis les fichiers source, se placer dans le dossier Puissance_4, ouvrir un terminal
et exécuter la commande : ```make```, ou faire ```python3 main.py```.
Pour exécuter le programme avec le fichier exécutable, se placer dans le dossier executable_linux, ouvrir un terminal
et exécuter la commande ```./main```.

### MacOS
Pour exécuter le programme depuis les fichiers source, se placer dans le dossier Puissance_4, ouvrir un terminal
et exécuter la commande : ```make```, ou faire ```python3 main.py```.
Pour exécuter le programme avec le fichier exécutable, se placer dans le dossier executable_mac, ouvrir un terminal
et exécuter la commande ```./main```.

### Windows
Pour exécuter le programme depuis les fichiers source, se placer dans le dossier Puissance_4, ouvrir un terminal
et exécuter la commande : ```python3 main.py``` (python3 peut ne pas marcher, essayer avec py, python ou python3.9).
Pour exécuter le programme avec le fichier exécutable, se placer dans le dossier executable_windows, ouvrir un terminal
et exécuter la commande ```.\main```.

## Auteurs
Cette application a été développée par :
- Gabriel Scrève,
- Léo Lamoureux,
- Lola Pires Pinto,
- Louis-Albert Sottas,
- Romain Gicquiaud--Rousset,
- Théophile Molinatti,
- Thomas Pittis,
- Victor Chhun.
