from airflow.providers.google.cloud.operators.dataproc import DataprocDeleteClusterOperator

delete_cluster_task = DataprocDeleteClusterOperator(
task_id='delete_cluster_task',
project_id=GCP_PROJECT_ID,
cluster_name=CLUSTER_NAME,
region=GCP_REGION,
dag=dag,
)

# Set the task dependencies as required