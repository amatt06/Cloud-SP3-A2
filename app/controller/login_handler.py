import boto3
from flask import render_template, redirect, url_for, request, session


def handle_login():
    dynamodb = boto3.client('dynamodb')
    email = request.form.get('email')
    password = request.form.get('password')

    key_condition_expression = "email = :email"

    expression_attribute_values = {
        ":email": {"S": email}
    }

    response = dynamodb.query(
        TableName='login',
        KeyConditionExpression=key_condition_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    if response.get('Count', 0) == 1:
        stored_password = response['Items'][0]['password']['S']

        if password == stored_password:
            user_name = response['Items'][0]['user_name']['S']
            session['user_name'] = user_name
            return redirect(url_for('main'))

    error_message = 'Invalid Email or Password.'
    return render_template('login.html', message=error_message)
