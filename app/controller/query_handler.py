import boto3
from flask import request, redirect, url_for


def handle_query():
    title = request.form.get('title')
    year = request.form.get('year')
    artist = request.form.get('artist')

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

        print(items)
        return redirect(url_for('main', music_items=items))
    else:
        return redirect(url_for('main', message='No result is retrieved. Please query again'))
