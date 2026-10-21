# Exercice Python 10/06

Ce dépôt contient une série d'exercices Python centrés sur les structures conditionnelles (`if`, `elif`, `else`) et les expressions booléennes.

## Objectif

Pratiquer la logique conditionnelle en Python à travers plusieurs situations concrètes :
- validation d'âge,
- choix d'activité selon la température,
- test de divisibilité,
- calcul du nombre de racines d'un polynôme du second degré.

## Contenu du projet

- `Exo1.py` : vérifie si un âge est compris entre 18 et 55 et affiche une réponse selon le résultat.
- `Exo2.py` : choisit une activité selon une température donnée.
- `Exo3.py` : détermine si un nombre est divisible par 2, par 3, ou par les deux.
- `Exo4.py` : calcule le discriminant et indique le nombre de racines réelles d'une équation du second degré.

## Comment exécuter les exercices

Depuis le dossier du projet, lancez un fichier Python avec la commande :

```bash
python Exo1.py
```

Vous pouvez remplacer `Exo1.py` par n'importe quel autre fichier du dépôt :

```bash
python Exo2.py
python Exo3.py
python Exo4.py
```

## Prérequis

- Python 3 installé sur votre machine.

## Exemple

```python
age = int(input("Entrer l'age que vous souhaitez évaluer: "))
if 18 <= age <= 55:
    print("Transaction acceptée!")
else:
    print("Transaction refusée")
```

## Auteur

Projet réalisé dans le cadre de la pratique de Python sur les conditions et la logique booléenne.
