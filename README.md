# Python3 : Agenda

Créer le <a href="https://fr.wikipedia.org/wiki/Agenda">jeu Simon</a> en utilisant python3.

# Déroulement 

Développeur freelance, vous avez été contacté par Madame Derieux, médecin généraliste qui a 
besoin de vos services. Madame Derieux est très occupée entre son métier et ses nombreuses 
activités. Elle a souvent des difficultés à gérer son agenda et son emploi du temps. Comme tous les 
scientifiques, elle est tournée vers les nouvelles technologies et voudrait quelque chose de plus 
performant qu'un agenda papier. Elle voudrait utiliser cette dernière technologie dont tout le monde 
parle : l'ordinateur ! Votre mission sera donc de lui développer une application pour son terminal qui
fonctionnera comme un agenda et lui permettra d'organiser son emploi du temps.
  
Spécifications fonctionnelles :
- La page d'accueil affiche la date du jour et le calendrier du mois en cours
- L'utilisateur peut voir le calendrier du mois suivant et du mois précédent
- L'utilisateur peut voir tous les événements d'une date précise
- L'utilisateur peut annuler (supprimer) un événement enregistré dans l'agenda
- L'utilisateur peut ajouter un événement dans l'agenda
- L'utilisateur peut modifier les caractéristiques d'un événement déjà enregistré dans l'agenda
- Deux événements ne peuvent pas avoir lieu le même jour à la même heure
- Un événement est composé obligatoirement d'un titre, d'une date, d'une heure et éventuellement 
  d'une description


# Critères de qualité

Votre agenda devra :
- Langage Python 3
- Organisation du code selon le principe MVC
- Usage de la programmation orientée objet
- Respect du principe DRY
- Essayer de respecter certains des principes SOLID
- Programme exécutable par le lancement d'un fichier main.py
- Intégration d'une base de données PostgreSQL via la librairie Psycopg2
- Utilisation du module Calendar

# Bonus

Vous pouvez, si vous le souhaitez, rajouter des fonctionnalités à votre application comme par 
exemple :
- Une vérification stricte des données rentrées par l'utilisateur dans les inputs (validité du format des
  dates, heures, absence de caractères spéciaux...)
- Une gestion plus fine de l'expérience utilisateur. Par exemple que se passe-t-il l'utilisateur cherche 
  à modifier un événement non-existant ?
- Transformer votre application en agenda partagé pour plusieurs personnes avec la possibilité de 
  créer des comptes personnels

# Ressources 

- https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/
