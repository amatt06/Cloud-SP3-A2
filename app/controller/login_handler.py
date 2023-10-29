import boto3
from flask import render_template, redirect, url_for, request


def handle_login():
    dynamodb = boto3.client('dynamodb')
    email = request.form.get('email')
    password = request.form.get('password')

    # Construct the KeyConditionExpression as a string
    key_condition_expression = "email = :email"

    # Define the expression attribute values
    expression_attribute_values = {
        ":email": {"S": email}
    }

    # Query DynamoDB to check if the user exists with the provided email
    response = dynamodb.query(
        TableName='login',
        KeyConditionExpression=key_condition_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    if response.get('Count', 0) == 1:
        stored_password = response['Items'][0]['password']['S']

        # Check if the stored password matches the provided password
        if password == stored_password:
            # Password matches, redirect to the 'main' page
            return redirect(url_for('main'))

    error_message = 'Invalid Email or Password.'
    return render_template('login.html', message=error_message)
