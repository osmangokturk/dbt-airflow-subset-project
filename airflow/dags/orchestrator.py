
import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount
from airflow.operators.python import PythonOperator 

# Appending path to find your custom modules
sys.path.append('/opt/airflow/api-requests')
from insert_records import main


default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 4, 30),
    'catchup': False,
}

dag = DAG(
    dag_id='bweather-dbt-orchestrator2',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )

# Task 2: dbt Transformation via Docker
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(#lowercase
                source='/home/osman/reposProjects/weather-data-prj/dbt/my_prj', # full path on our side. 
                target='/usr/app', # on the container side, use the d-c.yaml file 
                type='bind'
            ),
            Mount(
                source='/home/osman/reposProjects/weather-data-prj/dbt/profiles.yml', 
                target='/root/.dbt/profiles.yml', 
                type='bind'
            ),
        ],
        network_mode='weather-data-prj_my-network',
        docker_url='unix://var/run/docker.sock', 
        auto_remove='success'
    )

task1  >> task2 