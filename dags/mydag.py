from airflow import DAG
from airflow.operators.bash import BashOperator  # type: ignore
from datetime import datetime, timedelta
import os

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 10),  # Change as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the path to your dbt project
DBT_PROJECT_DIR = "/usr/local/airflow/include/snowflake_dbt_myproject"
# ^ Better to mount your dbt project inside the Astro container (Windows paths won’t work inside Linux containers)

# Define the DAG
with DAG(
    dag_id="dbt_snowflake_pipeline",
    default_args=default_args,
    description="Run dbt models using dbt Core",
    schedule="@daily",   
    catchup=False,
    tags=["dbt", "snowflake"],
) as dag:

    # Task 1: Run dbt models
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run",
    )

    # Task 2: Run dbt tests after models are built
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test",
    )

    # Define task dependencies
    dbt_run >> dbt_test
