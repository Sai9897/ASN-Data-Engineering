from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateClusterOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Replace these values with your own configurations
GCP_PROJECT_ID = 'airflow123'
GCP_REGION = 'us-central1'
CLUSTER_NAME = 'dpcluster'
NUM_WORKERS = 2
MASTER_MACHINE_TYPE = 'n2-standard-2'
WORKER_MACHINE_TYPE = 'n2-standard-2'
MASTER_DISK_SIZE_GB = 50  # Set the desired disk size for the master node (in GB)
WORKER_DISK_SIZE_GB = 50  # Set the desired disk size for the worker nodes (in GB)
IMAGE_VERSION = '2.1-debian11'


default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': days_ago(1),
'email_on_failure': False,
'email_on_retry': False,
'retries': 0,
#'retry_delay': timedelta(minutes=5),
}

dag = DAG(
'create_dataproc_cluster_and_submit_sparkjob_delete_cluster',
default_args=default_args,
description='Create a Dataproc cluster, submit spark job and delete the cluster',
schedule_interval=timedelta(days=1),
)

create_cluster_task = DataprocCreateClusterOperator(
task_id='create_dataproc_cluster',
project_id=GCP_PROJECT_ID,
cluster_name=CLUSTER_NAME,
num_workers=NUM_WORKERS,
master_machine_type=MASTER_MACHINE_TYPE,
worker_machine_type=WORKER_MACHINE_TYPE,
master_disk_size=MASTER_DISK_SIZE_GB,
worker_disk_size=WORKER_DISK_SIZE_GB,
region=GCP_REGION,
image_version=IMAGE_VERSION,
dag=dag,
)

# Set the task dependencies as required