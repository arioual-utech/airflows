"""
DAG de test pour vérifier le fonctionnement d'Apache Airflow
Ce DAG contient plusieurs tâches simples pour tester l'installation et la configuration
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

# Définition des arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Création du DAG
dag = DAG(
    'test_dag',
    default_args=default_args,
    description='DAG de test pour vérifier le fonctionnement d\'Airflow',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['test', 'verification']
)

# Fonction Python pour la première tâche
def print_hello():
    """Salut IAAS """
    print("Bonjour depuis Airflow!")
    return "Hello task completed"

# Fonction Python pour la deuxième tâche
def print_current_time():
    """Tâche Python qui affiche l'heure actuelle"""
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"L'heure actuelle est: {current_time}")
    return f"Time task completed at {current_time}"

# Fonction Python pour la troisième tâche
def calculate_simple_math():
    """Tâche Python qui effectue un calcul simple"""
    result = 2 + 2
    print(f"2 + 2 = {result}")
    return f"Math result: {result}"

# Définition des tâches
start_task = DummyOperator(
    task_id='start',
    dag=dag
)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag
)

time_task = PythonOperator(
    task_id='time_task',
    python_callable=print_current_time,
    dag=dag
)

math_task = PythonOperator(
    task_id='math_task',
    python_callable=calculate_simple_math,
    dag=dag
)

bash_task = BashOperator(
    task_id='bash_task',
    bash_command='echo "Tâche Bash exécutée avec succès!" && date',
    dag=dag
)

end_task = DummyOperator(
    task_id='end',
    dag=dag
)

# Définition de l'ordre d'exécution des tâches
start_task >> hello_task >> [time_task, math_task] >> bash_task >> end_task 