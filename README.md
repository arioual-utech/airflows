# 📊 Test DAG Airflow - Démo IAAS

Ceci est un exemple de README mis à jour automatiquement par n8n et GPT, cet encard ne devrait pas bouger d'un pouce et seul la partie "Doc by AI" est modifée par l'IA. Cordialement, la direction.

## 🧑‍💻 Auteur & Contact

- Auteur : Équipe IAAS
- Contact : iaas-team@example.com

# Doc by AI

Ce dépôt contient un DAG Apache Airflow nommé test_dag qui a pour objectif de tester et valider l'installation et la configuration de base d'Airflow.

## Description générale
Le DAG `test_dag` est programmé pour s'exécuter une fois par jour. Il inclut plusieurs tâches simples implémentées en Python et Bash, permettant de vérifier la bonne exécution des opérateurs dans un environnement Airflow.

## Structure du DAG
- `start_task` : une tâche DummyOperator servant de point de départ.
- `hello_task` : une tâche Python qui affiche "Bonjour depuis Airflow!".
- `time_task` : une tâche Python qui affiche l'heure actuelle.
- `math_task` : une tâche Python qui calcule l'opération simple 2 + 2.
- `bash_task` : une tâche BashOperator qui exécute une commande shell pour afficher un message et la date.
- `end_task` : une tâche DummyOperator servant de point final.

## Dépendances entre les tâches
```
start_task
   │
hello_task
   │
 ┌────────────┬────────────┐
 │            │            │
time_task   math_task
   │            │
   └────────────┘
       │
bash_task
   │
end_task
```

## Objectif
Ce DAG constitue un modèle de test rapide pour valider que les différents types d'opérateurs fonctionnent correctement dans un pipeline Airflow (PythonOperator, BashOperator, DummyOperator). Idéal pour des tests de bon fonctionnement ou de démonstration d'installation d'Airflow.

## Paramètres par défaut
- `owner`: airflow
- `start_date`: 1er janvier 2024
- `retries`: 1
- `retry_delay`: 5 minutes
- `schedule_interval`: tous les jours

## Tags
- `test`, `verification`