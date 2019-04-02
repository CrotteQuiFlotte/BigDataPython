# Labo AV/HIDS

Ce document contient les informations suivantes pour le cours AV/HIDS:

* comment utiliser le labo virtuel mis en place pour le cours
* liens sur l'installation de Prelude SIEM
* liens sur l'installation de OSSEC

## Configuration du labo

Le labo contient plusieurs machines virtuelles gérées avec PROXMOX et installées avec une image cloud de Ubuntu 18.04:

* `pfsense`: firewall/DHCP/DNS
* `linux[1-8]`: machines de test (agents)
* `prelude`: serveur Prelude SIEM
* `ossec`: serveur OSSEC
* `wazuh`: serveur Wazuh

Le domaine local est: `labo`

Toutes les machines peuvent communiquer entre elles sans restriction et peuvent initier des connexions sortantes vers Internet.

Toutes les machines sont accessibles en SSH via un tunnel utilisant la machine `pfsense`.


## Mise en place du tunnel SSH

### Configuration

1. copier les clés SSH

```Bash
cp lab.dechelle.net* $HOME/.ssh
```

2. copier la configuration SSH

```Bash
cat config-ssh-simple.txt >> $HOME/.ssh/config
```

Alternative:

```Bash
cat config-ssh-socks5.txt >> $HOME/.ssh/config
```

Cette alternative est plus simple, mais nécessite d'avoir la commande `ncat` (sur Ubuntu: `apt-get ins
tall nmap`). De plus, cette alternative ne fonctionne pas dans certains cas.


3. vérifier les permissions des fichiers

```Bash
ls -l $HOME/.ssh/lab.dechelle.net* $HOME/.ssh/config
```

On doit obtenir les permissions suivantes:

```
-rw------- 1 fdechelle fdechelle 2912 mars  16 09:39 /home/fdechelle/.ssh/config
-rw------- 1 fdechelle fdechelle 1679 mars  15 12:09 /home/fdechelle/.ssh/lab.dechelle.net
-rw-r--r-- 1 fdechelle fdechelle  398 mars  15 12:09 /home/fdechelle/.ssh/lab.dechelle.net.pub
```

SSH refuse en effet qu'une clé privée ait une permission en 0644.


### Lancement du tunnel

```Bash
ssh lab.dechelle.net
```

On voit le message suivant:

```
This login only supports SSH tunneling.
```

On peut ensuite lancer une commande sur une machine du labo:

```Bash
ssh linux1.labo date
```

```
Fri Mar 22 11:37:25 UTC 2019
```


## Prelude

Prelude est un SIEM open source permettant de suivre des incidents de sécurité.

Documentation:
> https://www.prelude-siem.org/projects/prelude/wiki

Installation:
> https://www.prelude-siem.org/projects/prelude/wiki/InstallingPackageUbuntu

Machines à utiliser:

* Prelude serveur et interface web: `prelude.labo`
* Prelude agents: toutes les machines `linux?.labo`


## OSSEC

OSSEC est un HIDS open source.

Documentation d'installation à partir des packages:
> http://www.ossec.net/downloads.html#apt-automated-installation-on-ubuntu-and-debian

L'interface web de OSSED est "deprecated".

Une alternative possible est Wazuh:
> https://wazuh.com/

Machines à utiliser:

* OSSEC serveur et interface web: `ossec.labo`
* Wazuh serveur et interface web: `wazuh.labo`
* OSSEC agents: toutes les machines `linux?.labo`

# Project Big Data
