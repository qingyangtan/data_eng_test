from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

import os

DIR = os.getcwd() + '/Section_1'

dag = DAG(
    "de-pipeline-1",
    description="Process pipeline 1",
    schedule_interval="0 1 * * *",
    start_date=datetime(2020, 5, 30)
)

process_pipeline = BashOperator(
    task_id="process_file",
    bash_command=f"python3 {DIR}/de_pipeline/scripts/pipeline_1.py",
    env={'cwd': DIR},
    dag=dag
)
