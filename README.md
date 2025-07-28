# 📊 Test DAG Airflow - Démo IAAS

Ceci est un exemple de README mis à jour automatiquement par n8n et GPT, cet encard ne devrait pas bouger d'un pouce et seul la partie en dessous est modifée par l'IA.

## 🧑‍💻 Auteur & Contact

- Auteur : Équipe IAAS
- Contact : iaas-team@example.com

# Doc by AI

Ce dépôt contient un exemple de DAG (Directed Acyclic Graph) pour Apache Airflow. Le but est de tester le fonctionnement d'une installation Airflow via un workflow simple comportant différentes tâches Python, Bash et des opérateurs de contrôle.

## 🚀 Description du projet

Ce DAG nommé `test_dag` est exécuté quotidiennement (`schedule_interval=timedelta(days=1)`) et comprend les étapes suivantes :

- Tâche de démarrage via un `DummyOperator`
- Tâche Python affichant un message (`hello_task`)
- Tâche Python affichant l'heure actuelle (`time_task`)
- Tâche Python effectuant un calcul mathématique simple (`math_task`)
- Tâche Bash exécutant une commande système (`bash_task`)
- Tâche de fin via un `DummyOperator`

L’objectif principal est de :
- Vérifier que l’environnement Airflow est opérationnel
- Illustrer l’utilisation de différents types d’opérateurs
- Fournir un point de départ pour des workflows plus complexes

## 🧩 Structure du DAG

```mermaid
graph TD;
    start --> hello_task;
    hello_task --> time_task;
    hello_task --> math_task;
    time_task --> bash_task;
    math_task --> bash_task;
    bash_task --> end;
```

## ⚙️ Dépendances

Ce DAG utilise uniquement les opérateurs standards d'Airflow (Dummy, Python et Bash), donc aucune dépendance supplémentaire n’est nécessaire si votre environnement Airflow est installé correctement.

## 🧠 IA - Intelligence Artificielle (Section à venir)

Cette section est dédiée aux futures intégrations avec des composants d'intelligence artificielle. L'objectif est d'utiliser Airflow comme orchestrateur de processus IA dans le cadre d'une IAAS (Intelligence-Artificial-as-a-Service).

🔧 À venir :
- Intégration de modèles d'IA via des tâches Python (ex : prédictions, traitements NLP)
- Appels à des APIs de modèles pré-entraînés (OpenAI, HuggingFace, etc.)
- Suivi des métriques d'exécution et journaux intelligents

➡️ Cette section sera mise à jour dans les prochaines versions du DAG.

## 📁 Fichier principal

- `test_dag.py` : Contient la définition complète du DAG avec toutes les tâches.

## 📅 Saisie d'historique

- `catchup=False` : Les exécutions passées ne seront pas rattrapées.
- `start_date=datetime(2024, 1, 1)` : Date à partir de laquelle le DAG peut s'exécuter.

---

Ce DAG est un excellent point de départ pour construire des workflows data et IA complexes à l’aide d’Apache Airflow 💡