import boto3
from flask import request, redirect, url_for, session

s3 = boto3.client('s3')


def get_image_url(artist_name):
    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': 'artist-images-bucket',
                                                     'Key': f'artist_images/{artist_name}.jpg'},
                                             ExpiresIn=3600)
        return response
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return None


def handle_query():
    title = request.form.get('title')
    year = request.form.get('year')
    artist = request.form.get('artist')

    session.pop('query_results', None)

    dynamodb = boto3.client('dynamodb')

    filter_expression = []
    expression_attribute_values = {}
    expression_attribute_names = {}

    if title:
        filter_expression.append("begins_with(title, :title)")
        expression_attribute_values[":title"] = {"S": title}

    if year:
        filter_expression.append("#yr = :year")
        expression_attribute_values[":year"] = {"S": year}
        expression_attribute_names["#yr"] = "year"

    if artist:
        filter_expression.append("begins_with(artist, :artist)")
        expression_attribute_values[":artist"] = {"S": artist}

    if expression_attribute_values:
        filter_expression_str = " AND ".join(filter_expression)

        if expression_attribute_names:
            response = dynamodb.scan(
                TableName='music',
                FilterExpression=filter_expression_str,
                ExpressionAttributeValues=expression_attribute_values,
                ExpressionAttributeNames=expression_attribute_names
            )
        else:
            response = dynamodb.scan(
                TableName='music',
                FilterExpression=filter_expression_str,
                ExpressionAttributeValues=expression_attribute_values)

        items = response.get('Items', [])

        if not items:
            return redirect(url_for('main', message='No result is retrieved. Please query again'))

        for item in items:
            artist_name = item['artist']['S']
            img_url = get_image_url(artist_name)
            item['img_url'] = img_url

        print(items)
        session['query_results'] = items
        return redirect(url_for('main', music_items=items))
    else:
        return redirect(url_for('main', message='No result is retrieved. Please query again'))
