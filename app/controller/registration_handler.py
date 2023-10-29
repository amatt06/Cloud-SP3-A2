import boto3
from flask import request, redirect, url_for, render_template


def handle_registration():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('user_name')
        password = request.form.get('password')

        dynamodb = boto3.client('dynamodb')

        response = dynamodb.query(
            TableName='login',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={':email': {'S': email}}
        )

        if response.get('Count', 0) > 0:
            return render_template('register.html', message='The Email Already Exists.')

        dynamodb.put_item(
            TableName='login',
            Item={
                'email': {'S': email},
                'user_name': {'S': username},
                'password': {'S': password}
            }
        )

        return redirect(url_for('login'))

    return render_template('register.html')
