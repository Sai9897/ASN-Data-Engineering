import base64
import json
from google.cloud import pubsub_v1, storage

# Initialize the Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('[YOUR PROJECT ID]', '[YOUR TOPIC]')

def stream_gcs_to_pubsub(data, context):
    """Cloud Function to be triggered by Cloud Storage when a file is uploaded."""

    # Initialize the GCS client
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(data['bucket'])
    blob = bucket.blob(data['name'])

    # Download the content of the uploaded JSON file
    content = blob.download_as_text()

    # Parse the JSON content
    data_json = json.loads(content)
    employees = data_json.get("Employees", [])

    # Publish each employee object as a separate message to Pub/Sub
    for employee in employees:
        message_str = json.dumps(employee)
        message_bytes = message_str.encode('utf-8')
        publisher.publish(topic_path, data=message_bytes)

    print(f"Published {len(employees)} messages to {topic_path}")


