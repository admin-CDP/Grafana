# Installation et utilisation de Grafana pour CDP
**Prérequis :** 

 - Avoir installé Grafana en local ou sur un serveur dédié (https://grafana.com/docs/grafana/latest/setup-grafana/installation/)
 - Avoir créé un premier dashboard sur Grafana via l'interface (dans le navigateur http://MONIP:3000 normalement)
 

# Paramétrage de Grafana
Il faut d'abord localiser le fichier de paramétrage Grafana : https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/

Il suffit ensuite de changer les valeurs suivantes : 

 - [security]

		allow_embedding = true
 - [auth.anonymous]

		enabled = true
		org_name = Main Org.
		org_role = Viewer

Il faut ensuire relancer grafana
```bash
sudo systemctl restart grafana-server
```
Reste à récupérer un token de connexion à Grafana, sur l'interface web, *Menu/Administration/Service accounts* et de et de générer un service account token 


# Paramétrage du serveur et de l'interface
Il faut maintenant cloner le git suivant sur le serveur : https://github.com/admin-CDP/Grafana
Il faut ensuite, au début du code python renseigner le token récupéré précédemment et l'IP du serveur sur lequel est hébergé Grafana.

Reste à lancer le code indéfiniment  :

			nohup python3 server_interface_grafana.py 

Reste à accéder à l'interface via  *index.html* en prenant soin de vérifier l'url du serveur Grafana est bien la bonne dans le "< iframe >" du document html.

# Création de visualisation via Grafana
Pour créer des visualisations sous Grafana, il faut tout d'abord connecter la base MySql (rubrique Connection en renseignant l'url et les logins de la base) et on peut ensuite créer un dashboard en choisissant la base MySql comme source.

Reste à écrire la bonne requête, il faut choisir la bonne table, l'id des transactions et sélectionner les bonnes données dans le JSON grâce à la commande JSON_EXTRACT et en se référant aux json extrait depuis la base (voir ce qui est renvoyé pas le code du serveur grafana


# Arrêt du serveur

  

Si pour x ou y raison vous devez arrêter le serveur voici la marche à suivre (sous linux)

		ps -ef |grep nohup

Cette commande retourne l'id du processus en cours (s'il n'y en a qu'un), il suffit alors de le terminer

		kill -9 'process_id'


