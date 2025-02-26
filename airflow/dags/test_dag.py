from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 0,
}

def print_test():
    print("__________ceci est un test_______________")

dag = DAG(
    'test_dag',
    default_args=default_args,
    description='Test DAG qui imprime un message toutes les 60 secondes',
    schedule=timedelta(seconds=60),
    catchup=False,
    is_paused_upon_creation=True  # Le DAG sera inactif dès sa création
)

task_print = PythonOperator(
    task_id='print_test_message',
    python_callable=print_test,
    dag=dag
)