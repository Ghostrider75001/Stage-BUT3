# 📄 Pourquoi on n’utilise pas le filtrage MAC & pourquoi on reste en WPA3-Personal (temporairement)

## 🔐 1. **Le filtrage MAC : une fausse sécurité**

### ❌ C’est facilement contournable

- Les adresses MAC sont **visibles en clair** sur le réseau.
- Il suffit à un attaquant d’écouter le trafic, récupérer une MAC autorisée, et la **spoof** (changer l’adresse de son appareil).

Résultat : **aucune vraie protection**.

<br>

### ⛔ Maintenance lourde

À chaque nouvel appareil, il faut :

- Demander l’adresse MAC.
- L’ajouter manuellement sur le contrôleur ou les APs.
- Risquer une erreur (typo, doublon, oubli).

Pas viable dès qu’on dépasse une poignée d’utilisateurs (ce qui est notre cas).

<br>

###  ⚠️ Pas compatible avec la mobilité moderne

- Certains appareils *(notamment Apple/Android/MacOS et même certains PCs Windows)* utilisent des **MAC aléatoires** pour renforcer la vie privée.

Résultat : ça bloque les connexions ou fait sauter les règles.

<br>

## 🛡️ 2. Pourquoi on reste (temporairement) en WPA3-Personal

### ✅ Chiffrement fort

- WPA3-Personal utilise **SAE** *(Simultaneous Authentication of Equals)* au lieu du vieux PSK WPA2.
- Résiste mieux aux attaques par dictionnaire.
- Chaque session est chiffrée **individuellement**, donc même si quelqu’un a le mot de passe, il ne peut pas sniffer les autres.

<br>

### ⚙️ Facile à déployer
- Pas besoin de serveur RADIUS ni d’infra supplémentaire.
- On peut le mettre en place **immédiatement** *(c'est déjà le cas)*, le temps de finaliser la configuration du FreeRADIUS + Entra ID.

<br>

### 🔒 Meilleure sécurité que WPA2-Personal
- Si on doit rester sur un PSK, autant prendre la version la plus robuste.
- En plus, **la plupart des devices récents** supportent WPA3.

<br>

## ✅ Ce qu’on mettra ensuite : WPA2/3-Enterprise
Une fois le serveur RADIUS en place, on passera en **authentification entreprise** :

- Chaque utilisateur aura son propre login (via Entra ID).
- Il n'y aura plus de mot de passe partagé.
- Contrôle d’accès plus fin + logs d’audit.
- Compatible avec l’auth multi-facteur si besoin (Il faut un serveur qui prends en charge l'extension NPS de windows dans ce cas).

## 🧠 En résumé

| Option             | Avantages	                 | Inconvénients                | Verdict          |
| :---------------   |:----------------------------- | :----------------------------| :------------    |
| Filtrage MAC       | Simple à comprendre           | Contournable, relou à gérer  |❌À éviter       |
| WPA3-Personal      | Sûr, simple, dispo maintenant | Un mot de passe partagé      |✅Temporaire OK  |
| WPA2/3-Enterprise  | Sécurisé, individuel, pro     | Mise en place + infra RADIUS |🚀Objectif final |

