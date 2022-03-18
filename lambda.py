import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pet-project-dynamodb')

def lambda_handler(event, context):
    try:
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        csv_file = event["Records"][0]["s3"]["object"]["key"]

        response = s3_client.get_object(Bucket=bucket, Key=csv_file)
        data = response['Body'].read().decode('utf-8').split('\n')
        del data[0]
        for disease in data:
            disease = disease.split(',')
            table.put_item(
                Item = {
                    'id': disease[0],
                    'cancer_site': disease[1],
                    'year': disease[2],
                    'sex': disease[3],
                    'total': disease[4],
                    'first_year_costs': disease[5],
                    'last_year_costs': disease[6]
                }
                )
    except Exception as err:
        print(err)

    return {
        'statusCode': 200,
        'body': json.dumps('Our shining data are loaded to DynamoDB table!')
    }
