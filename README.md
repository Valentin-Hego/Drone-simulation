# 🚁 Simulation de communication Drone - ESP32 + LoRa / ELRS

**Projet personnel - M2 Cybersécurité | En cours**

Ce projet consiste à simuler la communication entre une **télécommande** et un **drone** à l'aide de deux ESP32 et de modules radio **LoRa SX1276** pour ensuite attaquer ce système pour simuler une attaque sur du matériel réel.

L'objectif est de comprendre concrètement comment fonctionne une communication radio embarquée, depuis l'échange de données entre les microcontrôleurs jusqu'au signal radio.

Je m'intéresse notamment à :

* la communication **ESP32 ↔ SX1276** et le protocole SPI ;
* le fonctionnement et la structure des communications **LoRa / ELRS** ;
* l'implémentation de protocoles en **C++ et Python** ;
* l'analyse des signaux radio à l'aide d'une **clé SDR** ;
* les problématiques de **sécurité des communications radio** : authentification, intégrité, rejeu, etc.

Le projet me permet de découvrir ou approfondire plusieurs domaines qui m'intéressent en cybersécurité : **systèmes embarqués, protocoles réseau, radiofréquence et analyse de signaux**.

### 🛠️ Technologies

`ESP32` · `LoRa` · `ELRS` · `C++` · `Python` · `SDR`

On vas simuler le drone et la commande avec des esp32 pour des questions de coûts. 

Avancement actuel : 
- Après des soucis de livraison, toutes les pieces pour débuter le projet sont arrivées
- Soudure des modules radios SX1276 aux esp32 effectuée
- Premier ping radio entre les deux esp effectué avec succès

A suivre :
- Mettre en place le protocol ELRS pour coller aux standards de communications sans fil dans le monde des drones
- Achat d'une clé SDR
- Attaque des communications entre la commande et le drone (brouillage, prise de controle,...)
