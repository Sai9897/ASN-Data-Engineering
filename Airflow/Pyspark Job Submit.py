from airflow.operators.bash_operator import BashOperator

submit_spark_job_task = BashOperator(
task_id='submit_pyspark_job',
bash_command=f"gcloud dataproc jobs submit pyspark --cluster={CLUSTER_NAME} --region={GCP_REGION} gs://python_codes/my_spark_job.py",
dag=dag,
)

# Set the task dependencies as required