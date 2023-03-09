# zipcode = []
# country_codes = ['us', 'ca', 'mx', 'fr', 'ru']
# zipcodes = {90003: 'Los Angeles', 90802: 'Long Beach',\
#     91501: 'Burbank', 92101: 'San Diego',92139:'San Diego',\
#     90071:'Los Angeles'}
# for code in zipcodes.keys():
#     zipcode.append(code)
# print(f'ZipCodes-> {zipcode}')

# mapped_countries = map(country_codes, zipcodes.keys())
# print((mapped_countries))

# generator_zipcode = (zc for zc in zipcodes.keys())
# print(generator_zipcode)
# for code in generator_zipcode:
#     print(code)

# import json
# import boto3
# import sys
# import time
# s3 = boto3.resource("s3")
# querying buckets by their name
# bucket = s3.buckets.all()
# for i in bucket:
#     print(i.name)

# data = open("templates/index.html", 'rb')
# s3.Bucket("boto3-buck").put_object(Key="templates/index.html", Body=data)

# sqs = boto3.resource("sqs")
# sqs.create_queue(QueueName="test", Attributes={"DelaySeconds": '5'})
# time.sleep(5)
# existing_queue = sqs.get_queue_by_name(QueueName="test")
# print(existing_queue)
# for queue in sqs.queues.all():
#     print(queue.url)

# EC2 Instance_ID querying

# ec2 = boto3.client("ec2")
# response = ec2.describe_instances()
# Instance_Id = response["Reservations"][0]["Instances"][0]["InstanceId"]
# print(Instance_Id)


'''Setting up cloudwatch alarm'''
# cloudwatch =boto3.client("cloudwatch")

# paginator = cloudwatch.get_paginator("describe_alarms")
# for response in paginator.paginate(StateValue="INSUFFICIENT_DATA"):
#     res = response["MetricAlarms"]
#     print(res)



# cloudwatch.put_metric_alarm(
#     AlarmName='Web_server_CPU_Utilization',
#     ComparisonOperator='GreaterThanThreshold',
#     EvaluationPeriods=1,
#     MetricName='CPUUtilization',
#     Namespace='AWS/EC2',
#     Period=60,
#     Statistic='Average',
#     Threshold=70.0,
#     ActionsEnabled=False,
'''to enable AlarmActions, set ActionsEnabled to True'''
#     AlarmActions=[
#         f'arn:aws:swf:us-east-1:1461-8047-0292:action/actions/AWS_EC2.InstanceId.Reboot/1.0'
#     ],
#     AlarmDescription='Alarm when server CPU exceeds 70%',
#     Dimensions=[
#         {
#             'Name': 'InstanceId',
#             'Value': f'{Instance_Id}',
#         },
#     ],
#     Unit='Seconds',

# )

'''Disabling alarms'''
# cloudwatch.disable_alarm_actions(
#     AlarmNames=['Web_server_CPU_Utilization'],
# )

'''Apparrently, disabling alarm is different from deleting it'''
''' delete alarms '''
# cloudwatch.delete_alarms(AlarmNames=['Web_server_CPU_Utilization'])
# print(dir(boto3.client('ec2')))



# print(time.sleep(10))
# '''Terminating an instance using the instance ID'''
# terminate_instance = ec2.terminate_instances(InstanceIds=[Instance_Id])
# print(terminate_instance)




