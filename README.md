# Breaking-Language-Barriers-Pipeline




## Codelabs

https://codelabs-preview.appspot.com/?file_id=1dXKHuohRDgSZ0ZNEV1IM7HvMwl88bMCi3bkk1zInp8Y#0


## Overview

Natural Language Processing based Big Data Pipeline system to convert product information, blogs or news podcasts published in any language to other multiple languages based on user's choice using state of the art machine learning models powered by AWS architecture. 

- Language Translation 
- NER Audio Masking 
- Summarization

## Architecture

![img](https://lh6.googleusercontent.com/VBfMTC3kYuEUvnUNagpADibEgBd0EemN8-QVroz6EyaQ30R7AuliHwz37_5-mWqyAj8Glo2ZiH6Pa5FkYtBBaWXY0yKSMPtn7unXrSvqKQbaVMW-KTpD08BzbkQNVlebiqc5AxFcFaY_Mosu8XubecTrFwiWtlx6CKPOZJCVpaGac79v)

## Step Function Workflow

For our application we have developed a specific design pattern for our step functions which is parent and child processes or also known as Nested Workflows.
The parent Step function spawns multiple Child Step functions to process multiple input Audio links/files parallelly.

## Parent workflow:

![img](https://lh4.googleusercontent.com/ny9MIWyx8_XegbHN-HmBmFvPZ4_YuWdjcv1J4gJtvNcYhPelzrKKwdaKg9zwA8lOz7qBrMWVhD0GbhyejRSAF6SmgxS8FCN9_cvmeA_dMVIhJJOtU35MTzz0XRg_YXYdspT73_f3EEJjUBXjp9BxAr-4HgXXNGsD0FI8_QwuSMg5LX4X)

## Child Workflow:

![img](https://lh4.googleusercontent.com/zZ9i_XjrgJhY-MbBNTCgcy2cirerr0VS98u9jrdSP58Pm3JO33gAYxMLvKLb2CxD9Xv_u22sk9-rGKPl7I4IJ-Rng5hYezNR8dUXv7D3ZquLDb88ApN5P5BM7M_tB0BHhiGJNwnI4k4JotQOrziKRBoTwXnqAjHo2hjYxktchelLzoJO)

### Language Translation Step function Execution 
![img](https://lh5.googleusercontent.com/1zDx0cYpFi8ADi0TdWWMD8t-YRJX_kqF3KU6KT_YzHQJVVzPOovNP-6DfFd14YxyvVfWYyFOg8LH4pTzRyuBqRjWSO3FrZDqZBPiNQKsLXZc50JNxpX50zN6xFUSVrRXCXQ4imt909-i7hLkFpg4E4EM8i1W4PzMZY62E_xtux2bRb1l)

### NER Masking Step function Execution  
![img](https://lh4.googleusercontent.com/qjAbqVjjW2AuBGVvY597U7sRzQWVekHuG0OtEkR0Fb8MVnyfsJt1FU26eTXtJQQZEeDuRdVlm3s6sURB8wYSBJnVIgLiLv5qqQ2KP_GQWulxgfVq2jI6VEY668Xythp6C-7hWHI_DnJFR3Y0CWx3BVCenq8edRDlHFQX_dyh7BnDUDTn)

## X-Ray Service Graph

We are using AWS X-Ray to debug and monitor our application. By enabling X-Ray functionality mainly for step functions in our application. It generates service graph to display the execution of different processes and highlight them as shown above.

![img](https://lh3.googleusercontent.com/e214oE0aZumT1OZymdizWFLS7beuxLISTH02ub5GaaO3GE8P5-D_beEoSXkMSKeNd_CKe5lb3zhzlSINcAMFLixQLP24kXCnJAz6UxI-15Bon-EBQMH40xe6_XjqPVoS_rza3pLPHVJHhXIn3XM72bv03ebM_wMHGiVr5E5f-yu2Pv75)


## Application Screenshots 

Login/Signup
![img](https://lh3.googleusercontent.com/_UJgDQ3ziSbB61hLtIhj5dBXsrYsLNNC2kJ0wLDYQnqG5w8t2wiOp-62UTFp28gG9wKSYvo08SBT7K1CFxWzHSSnsmy_IevzX3LkrfG_SPKwAxVTdvhllNHxwKNATf2euQOqGOXFYEVX0glox65CkyG8uujDUVJ4n3uEvw30BX8-RwVF)

Services

![img](https://lh6.googleusercontent.com/O-sD4SLHimjwoVRvnK9EXMt7ubq8xFjH-b7ka9VH0cUbG39xLpYz0yzNSDY4R4JK2ShdA6Y0LWGNjH3bvf7UJ6DLEcyNMKKw1wVAmPFL_4VnLUuDiJuVUqlMPq0s_ChAdTPR4mxDzYXioy1LsXrhJUl8bzIrGeHBonaLayhNUAAoLsnu)
![img](https://lh6.googleusercontent.com/oKHVepMKHbKwL5o6NOJAH1OAOU2CWtKcRnauxJUSO4WNkTbzPUfCkSGsqOSmgemE1mGPDxzs-0fi5OX5F8rNGfto4F_jeP_mP6cdvH2YHkXQUR1Dq1jsN80jCb1b3HGa04ukYZZV8hAh69gqO7ZgX8HKjm161C-cY3y8dUQ0Z-V0k0IF)


NER Masking Output 

![img](https://lh3.googleusercontent.com/1Fomzwz7HuyFXOs8zgZtBXxMwZ2Kc-v1T9VYZpCsFihilGkegXGqDGnMVFlXlOlIpnUvQm-zFWfnS-pQQ0eyN_I0y5GduQ5ObkuP2SoNkIb8TtwsVmT0JwhLvG6UOYPLfVSjvfp_PX-1lgLjmXKARUy64XOcEsUJX1E0B3u0Vkgt4A0T)

Language Translation Output 
![img](https://lh6.googleusercontent.com/zo2KkiyJVaEx-atuVHBJ8crsbW7iY6RRKydxj4GC2FOQ4gYPD2Lc6VR5eCFeZ_2s1BumlbIOoxL3_5BSbJ6d4d2m4Lj1KoD06WDor7a_Ys-VY0NbZmZz5pxqkLeDgjjX9X9640v_blQP4vhrDkDkvQqCAJAOgKSE_l3QNBVb3g1LXq6k)


## Quick Sight Integration

For our application we have integrated our meta database tables located in DynamoDB with AWS Quick Sight service to generate various analyses/dashboards to visualize different aspects of our application.

![img](https://lh3.googleusercontent.com/OvAz9TQeo6HhAxvm5-3eMTuRmWKvchQv-654xs6Z2Bx93JA9isuXjU4OTXn7qmM5EIQJin21bmIaGK3gxw5sK6eJjkHACxz3BSoRak7OqH_awIAIIWLtLHBQeYhSUGi_syC8yiScO2tmBJ0KPP4xeZJpduFB2dPvn5f8NbZlAXPMyQOb)



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
