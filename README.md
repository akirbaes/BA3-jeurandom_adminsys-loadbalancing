# jeurandom_adminsys
Jeu random pour tester les connexions pour le projet d'amin sys
##Utilisation:
###Serveur:
python3 server_jeu.py IPADDRESS &

•Attache l'application à l'ip IPADDRESS sur le port 10000 (dix-mille) 

•Lancer l'application en tâche de fond (car "connect" bloque l'appli et empêche de l'arrêter avec ctrl+c)

•Stopper l'appli avec kill (killall python3)

###Client:
python3 jeu.py IPADDRESS

python3 triche.py IPADDRESS

•Envoie une partie au serveur d'ip IPADDRESS

•En cas de load-balancing, donner l'addresse du Directeur

##Effet:
La partie envoyée au serveur est analysée, puis après un temps de calcul le serveur renvoie une réponse:
Partie validée ou Partie rejettée.

###TODO: 
Client qui envoie 100 requêtes à la seconde.
