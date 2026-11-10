# TP_DEVOPS_M2_MIAGE_DOCKER_AB
TP Docker Alexia B

Axes d'optimisation :

- Alléger l'image : Ne pas prendre la dernière version existante de Node (node:latest) qui pèse 1.88GB (tpdockeropti:origin) mais une version beaucoup plus légère pour se délester des outils inutiles.

Correction : FROM node:20-alpine

Taille obtenue : 216MB (tpdockeropti:20alpine)

- Structurer l'installation des dépendances : Mauvaise pratique de copier tout le dossier node_modules de la machine hôte ou d'utiliser un npm install classique qui alourdit l'image à 226MB (tpdockeropti:node).

Correction : Copier d'abord les package*.json puis faire un RUN npm ci --only=production

- Gérer le contexte de build : Utiliser un .dockerignore pour exclure le dossier node_modules et les fichiers superflus.

Correction : Ajout du .dockerignore

Taille obtenue : 209MB (tpdockeropti:dockerignore)

- Nettoyer la liste des ports : Le code montre qu'il n'utilise que le port 3000, il n'y a donc pas besoin d'embarquer d'autres ports.

Correction : EXPOSE 3000

- Ne pas utiliser l'user en root par défaut dans le conteneur en ajoutant un utilisateur dédié.

Correction : USER node

Taille finale obtenue : 209MB (tpdockeropti:versiondefinitive)
