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
        dictMovies = dict()
        for movie in data:
            oscarNominee = movie.split(',')
            if oscarNominee[1] not in dictMovies.keys():
                dictMovies[oscarNominee[1]] = [1, []]
                dictMovies[oscarNominee[1]][1].append(oscarNominee[0])
            else:
                dictMovies[oscarNominee[1]][0] += 1
                dictMovies[oscarNominee[1]][1].append(oscarNominee[0])

        finalDataSet = []
        cnt = 0
        for movie in dictMovies.items():
            string = '; '.join(movie[1][1])
            final_string = ','.join([str(cnt), movie[0], str(movie[1][0]), string])
            cnt += 1
            finalDataSet.append(final_string)

        for movie in finalDataSet:
            movie = movie.split(',')
            table.put_item(
                Item={
                    'id': movie[0],
                    'movie': movie[1],
                    'nominations': movie[2],
                    'awards': movie[3]
                }
            )
    except Exception as err:
        print(err)

    return {
        'statusCode': 200,
        'body': json.dumps('Our shining data are loaded to DynamoDB table!')
    }
