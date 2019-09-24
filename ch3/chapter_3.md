# Chapitre 3: Booléens et conditionnelles

## 4. Tirage au sort

### 1. Dans le programme suivant, quelle devrait être la valeur de la variable `seuil` pour que la probabilité d'avoir `pile` soit la même que pour celle d'avoir `face`?

```python
import random
if random.random() < seuil:
    print("pile")
else:
    print("face")
```

La variable `seuil` doit avoir la valeur `0.5` pour que la probabilité d'avoir `pile` est la même que pour avoir `face`.

### 2. Quelle devrait être la valeur de `seuil` pour que la probabilité d'avoir `pile` soit 10% (et celle d'avoir `face` soit de 90%)?

La valeur de `seuil` devrait être de `0.10`.

### 3. Le programme suivant construit une chaîne de caractères composée de 40 caractères `*`.

```python
ligne = ""
for i in range(40):
    ligne += "*"
```

Modifier ce programme pour que la chaîne produite contienne des `*` et des `O` distribués de façon aléatoire et que la probabilité d'avoir `*` soit de 80%.


Réponse:

```python
import random
ligne = ""
for i in range(40):
    if random.random() < 0.20:
        ligne += "O"
    else:
        ligne += "*"
```

## 5. Les boucles `while`

### 1. Soit le programme suivant:

```python
for i in range(9):
    print(2*i)
```

Écrire le même programme avec une boucle `while`.

Réponse:

```python
i = 0
while i < 9
    print(2*i)
    i += 1
```

### 2. Écrire une fonctione `deux_somme_paire` qui n'a besoin d'aucun argument et ne retourne aucune valeur, mais affiche deux entiers dont la somme doit être paire.

```python
import random


def deux_somme_pair():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    while (a + b) % 2 != 0:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
    print(a)
    print(b)
```

## 6. Pour aller plus loin: les nombres premiers

### 1. Écrire une fonction `est_premier` qui, à partir d'un nombre `n` retourne `True` si `n` est premier et `False` s'il ne l'est pas.

Note: On suppose que 1 n'est pas premier.

```python
def est_premier(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### 2. Écrire une fonction `nombres_premiers` qui, à partir d'un nombre `n`, affiche à l'écran tous les nombres premiers strictement inférieurs à `n`.

```python
def nombres_premiers(n):
    for i in range(n):
        if est_premier(i):
            print(i)
```

## 7. Pour aller plus loin: Calcul de l'impôt sur le revenu

### 1. Le *revenu net imposable* est obtenu en diminuant de 10% le montant de revenu imposable.

`rev_net_imp = rev_imp - (rev_imp * 0.1)`

### 2. Le *quotient familial* (ou `qf`) obtenu en divisant le *revenu net imposable* par le nombre de parts fiscaux.

`qf = rev_net_imp / nb_parts`

### 3. Écrire une focntion `impots_brut` dont les arguments sont toujours `rev_imp` et `nb_parts`. Cette fonction devrait retourner le montant de l'impôt brut, si le motant est négatif alors l'impôt à payer est nul.

```python
def impots_brut(rev_imp, nb_parts):
    rev_net_imp = rev_imp - (rev_imp * 0.1)
    qf = rev_net_imp / nb_parts
    montant = 0
    if qf <= 9807:
        montant = 0
    elif qf > 9807 and qf <= 27086:
        montant = rev_net_imp * 0.14 - 1372.98 * nb_parts
    elif qf > 27086 and qf <= 72617:
        montant = rev_net_imp * 0.3 - 5706.74 * nb_parts
    elif qf > 72617 and qf <= 153783:
        montant = rev_net_imp * 0.41 - 13694.61 * nb_parts
    else:
        montant = rev_net_imp * 0.45 - 19845.93 * nb_parts
    if montant < 0:
        montant = 0
    return montant
```

