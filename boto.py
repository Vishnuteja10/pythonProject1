# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3
aws_mg_con = boto3.session.Session(profile_name='demo_user2')
iam_con=aws_mg_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)

