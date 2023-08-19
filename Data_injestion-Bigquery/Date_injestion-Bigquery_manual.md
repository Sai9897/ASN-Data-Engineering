PRE TASKS:

1.	Create a GCP New Project.
2.	Create a Dataproc cluster.
3.	Create a GCS  Bucket and load the csv file.
4.	Create a Temporary GCS Bucket and don’t load any file.
5.	Create a Dataset in BigQuery.
6.	Create an empty table in the above Dataset.
------------------------------------------------------------------------------------------------------------------------
In Dataproc: Start the cluster and open Juptyer Notebook web interface.

In Juptyer Notebook:
1.	Check whether GCS connection is established or not:
      !pip install gcsfs
      import gcsfs

## Create a GCS file system object
fs = gcsfs.GCSFileSystem()

## List the contents of a GCS bucket
bucket_name = 'inventy_bucket1'
contents = fs.ls(f'gs://inventy_bucket1')
print(contents)

2.	Now Check whether BigQuery connection is established or not:
      !pip install google-cloud-bigquery
      from google.cloud import bigquery

## Create a BigQuery client
client = bigquery.Client()

## List the datasets in your default project
datasets = list(client.list_datasets())
print("Datasets:")
for dataset in datasets:
print(dataset.dataset_id)

-------------------------------------------------------------------------------------------------------------------

## READ THE CSV FILE USING SPARK:

#Define your GCS and BigQuery configurations
gcs_bucket_name = 'inventy_bucket1'
gcs_file_path = 'gs://inventy_bucket1/Inventy_Metadata.csv'
bigquery_project_id = 'inventy'
bigquery_dataset_id = 'inventy_metadata'
bigquery_table_name = 'metadata_table'

#Read CSV from GCS
gcs_uri = f'gs://inventy_bucket1/Inventy_Metadata.csv'
df = spark.read.csv(gcs_uri).toDF("c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10")

df.show()

WRITE THAT DATAFRAME TO BIGQUERY:

#Replace "<dataset_id>" and "<table_id>" with your actual dataset and table IDs
project_id = "inventy"
dataset_id = "inventy_metadata"
table_id = "metadata_table"

df.write \
.format("bigquery") \
.option("table", f"{project_id}.{dataset_id}.{table_id}") \
.option("temporaryGcsBucket", "temp_data123") \
.mode("overwrite") \
.save()

NOW OPEN BIGQUERY AND DO YOUR QUERYING
