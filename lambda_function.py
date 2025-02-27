import awsSDK as wr
import pandas as pd
import urllib.parse
import os

os_input_s3_cleansed = os.environ['s3_cleansed']
os_input_glue_catalog_db = os.environ['glue_catalog_db']
os_input_glue_catalog_table = os.environ['glue_catalog_table']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:

        # Creating DF from content
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Extract required columns:
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write to S3
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed,
            dataset=True,
            database=os_input_glue_catalog_db,
            table=os_input_glue_catalog_table,
            mode=os_input_write_data_operation
        )

        return wr_response
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
