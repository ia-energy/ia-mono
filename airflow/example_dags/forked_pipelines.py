# Example dag that shows forking and joining task 
import datetime as dt
 
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
 
# define functions to run 
def root_fn():
    return 'root'
 
def one_a():
    return '1a'
 
def one_b():
    return '1b'

def two():
    return '2' 
 
# arguments for dag
default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2018, 10, 1, 10, 00, 00),
    'concurrency': 1,
    'retries': 0
}
 
# create and run DAG
with DAG('forked_pipelines',
         catchup=False,
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         # schedule_interval=None,
         ) as dag:
    root = PythonOperator(task_id='root',
         python_callable=root_fn)
 
    one_a = PythonOperator(task_id='1a',
                                        python_callable=one_a)
    one_b = PythonOperator(task_id='1b',
                                        python_callable=one_b)
    two = PythonOperator(task_id='2',
                                        python_callable=two)

# bitwise operators are used to set run order
root >> one_a
root >> one_b
one_a >> two 
one_b >> two 
 
