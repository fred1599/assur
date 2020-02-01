# assur

Web Services concernant la création d'un contrat d'assurance
------------------------------------------------------------

Pour tester dans votre environnement
-

1) Créer votre environnement
$ python3 -m venv env_assur

2) Activer votre environnement
$ source env_assur/bin/activate

3) Aller dans le dossier contenant le projet
$ cd assur
$ ./manage.py migrate
$ ./manage.py runserver

Le script de test concernant le WS se nomme *scripts/test_api_contract.py*
--------------------------------------------------------------------------

1) Mettre le serveur en fonctionnement

$ ./manage.py runserver

2) Dans une autre fenêtre, exécuter le script

$ python3 assur/scripts/test_api_contract.py

3) Visualiser le retour de type JSON

Tests unitaires sur la création de contrats
-------------------------------------------

$ ./manage.py test contract.tests

Participer au projet
------

1) Pour Fixer une erreur, créer un ticket et un Merge Request nommé Fix-erreur (remplacer erreur par l'erreur détectée)

Utilisation de *pre-commit* obligatoire
