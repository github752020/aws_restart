"""
Name of the file - s3blist.py
Author name - Quinn Chan
Student ID - Quinn Chan
Brief description of code purpose - get AWS region and print list of S3 buckets within the to a text file
Date written - 9/2/2023
Revisions including Date; Description of Change; Author of the change - N/A

"""
import boto3

def printBucketListToFile(my_region):
    s3client = boto3.client("s3", region_name=my_region)
    f = open("myfile.txt", "w")
    for bucket in s3client.list_buckets()["Buckets"]:
        if s3client.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint'] == my_region:
            print(bucket["Name"])
            f.write(bucket["Name"] + "\n")
    f.close()
    
    
my_session = boto3.session.Session()
my_region = my_session.region_name
print("Your current region is " + my_region)
result = input("Set "+ my_region +" as default region? (Y/N) ")

if result =="Y" or result =="y":
    try:
        printBucketListToFile(my_region)
        print("Bucket list written to file.")
    except:
        print("Failed to write.")
elif result =="N" or result =="n":
    print("Program terminated.")
else:
    print("Invalid response.")