# Breaking-Language-Barriers-Pipeline



## Web Application

http://3.85.147.6:8501/


## Codelabs

https://codelabs-preview.appspot.com/?file_id=1dXKHuohRDgSZ0ZNEV1IM7HvMwl88bMCi3bkk1zInp8Y#0


## Overview

Natural Language Processing based Big Data Pipeline system to convert product information, blogs or news podcasts published in any language to other multiple languages based on user's choice using state of the art machine learning models powered by AWS architecture. 

- Language Translation 
- NER Audio Masking 
- Summarization


## Architecture

![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/aws_architecture.png)

## Step Function Workflow

For our application we have developed a specific design pattern for our step functions which is parent and child processes or also known as Nested Workflows.
The parent Step function spawns multiple Child Step functions to process multiple input Audio links/files parallelly.

## Parent workflow:

![img](https://lh4.googleusercontent.com/ny9MIWyx8_XegbHN-HmBmFvPZ4_YuWdjcv1J4gJtvNcYhPelzrKKwdaKg9zwA8lOz7qBrMWVhD0GbhyejRSAF6SmgxS8FCN9_cvmeA_dMVIhJJOtU35MTzz0XRg_YXYdspT73_f3EEJjUBXjp9BxAr-4HgXXNGsD0FI8_QwuSMg5LX4X)

## Child Workflow:

![img](https://lh4.googleusercontent.com/zZ9i_XjrgJhY-MbBNTCgcy2cirerr0VS98u9jrdSP58Pm3JO33gAYxMLvKLb2CxD9Xv_u22sk9-rGKPl7I4IJ-Rng5hYezNR8dUXv7D3ZquLDb88ApN5P5BM7M_tB0BHhiGJNwnI4k4JotQOrziKRBoTwXnqAjHo2hjYxktchelLzoJO)

### Language Translation Step function Execution 
![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/Translation%20sf.png)

### NER Masking Step function Execution  
![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/NER%20sf.PNG)

## X-Ray Service Graph

We are using AWS X-Ray to debug and monitor our application. By enabling X-Ray functionality mainly for step functions in our application. It generates service graph to display the execution of different processes and highlight them as shown above.

![img](https://lh3.googleusercontent.com/e214oE0aZumT1OZymdizWFLS7beuxLISTH02ub5GaaO3GE8P5-D_beEoSXkMSKeNd_CKe5lb3zhzlSINcAMFLixQLP24kXCnJAz6UxI-15Bon-EBQMH40xe6_XjqPVoS_rza3pLPHVJHhXIn3XM72bv03ebM_wMHGiVr5E5f-yu2Pv75)


## Application Screenshots 

Login/Signup
![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/Grid%20layout.PNG)

Services

![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/services1.PNG)
![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/Masking.PNG)


NER Masking Output 

![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/NER%20Output.PNG)

Language Translation Output 
![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/Translation%20Output.PNG)


## Quick Sight Integration

For our application we have integrated our meta database tables located in DynamoDB with AWS Quick Sight service to generate various analyses/dashboards to visualize different aspects of our application.

![img](https://github.com/Nikhilkohli1/Breaking-Language-Barriers-Serverless-Pipeline/blob/main/application-screenshots/dash.PNG)



## Install instructions

### Create an Amazon Web Services (AWS) account

If you already have an account, skip this step.

Go to this [link](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fportal.aws.amazon.com%2Fbilling%2Fsignup%2Fresume&client_id=signup) and follow the instructions. You will need a valid debit or credit card. You will not be charged, it is only to validate your ID.

### Install AWS Command Line Interface (AWSCLI)

Install the AWS CLI Version 1 for your operating system. Please follow the appropriate link below based on your operating system.

- [macOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)
- [Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows)

** Please make sure you add the AWS CLI version 2 executable to your command line Path. Verify that AWS CLI is installed correctly by running `aws --version`.

- You should see something similar to `aws-cli/1.18.197 Python/3.6.0 Windows/10 botocore/1.19.37`.

#### Configuring the AWS CLI

You need to retrieve AWS credentials that allow your AWS CLI to access AWS resources.

1. Sign into the AWS console. This simply requires that you sign in with the email and password you used to create your account. If you already have an AWS account, be sure to log in as the root user.
2. Choose your account name in the navigation bar at the top right, and then choose My Security Credentials.
3. Expand the Access keys (access key ID and secret access key) section.
4. Press Create New Access Key.
5. Press Download Key File to download a CSV file that contains your new Access Key Id and Secret Key. Keep this file somewhere where you can find it easily.

Now, you can configure your AWS CLI with the credentials you just created and downloaded.

1. In your Terminal, run `aws configure`.

   i. Enter your AWS Access Key ID from the file you downloaded.
   ii. Enter the AWS Secret Access Key from the file.
   iii. For Default region name, enter `us-east-1`.
   iv. For Default output format, enter `json`.

2. Run `aws s3 ls` in your Terminal. If your AWS CLI is configured correctly, you should see nothing (because you do not have any existing AWS S3 buckets) or if you have created AWS S3 buckets before, they will be listed in your Terminal window.

** If you get an error, then please try to configure your AWS CLI again.



## Run Sequence

Run requirements.txt

```python
pip install -r requirements.txt
```

Run Streamlit application

```python
streamlit run app.py

```

## Built With

- [AWS Transcribe](https://aws.amazon.com/transcribe/) : Service that adds speech to text capabilities in applications.
- [AWS Translate](https://aws.amazon.com/translate/) : Machine translation service for fast, high-quality, & affordable language translation. 
- [AWS Polly](https://aws.amazon.com/polly/) : Service that turns text into lifelike speech.
- [AWS Comprehend](https://aws.amazon.com/comprehend/) : NLP service that uses machine learning to find insights and relationships in text.
- [AWS Polly](https://aws.amazon.com/polly/) : Service that turns text into lifelike speech.
- [AWS X-Ray](https://aws.amazon.com/xray/): Service which helps to analyze and debug production, distributed applications
- [AWS Cognito](https://aws.amazon.com/cognito/) :Service for authentication, authorization, and user management for web & mobile apps.
- [Streamlit](https://www.streamlit.io/) :The fastest way to build and share data apps
