# Modèle SASRI 

## Description du modèle SASRI

Le modèle SASRI intègre deux sous modèles : un modèle de mobilité et un modèle à compartiment d'épidémiologiques.
Le **modèle de mobilité** décrire un mouvement brownien des agents dans un espace à deux dimensions. Le **modèle à compartiment d'épidémiologiques** (cf. ci-dessous) définie les probabilités de transition entre les différents état de l'agent. Un agent peut prendre les états suivant : sain, asymptomatique, symptomatique, rétablie, mort, immuniser. 

<p align="center">
  <img width="60%" height="60%" src="./schéma/Model SASRI.png">
</p>


## Politique publique : l'efficacité de la quarantaine

**Question** : La quarantaine de la population symptomatique est-elle une mesure efficace pour contrôler une épidémie ? Nous faisions hypothèse que seules les personnes symptomatiques peuvent être identifié pour être mise en quarantaine. Cela correspondant au stade 2 du plan de réaction français face à la pandémie de coronavirus.

Nous analysons deux hypothèses : un virus produisant une population asymptomatique et sans une population asymptomatique.
