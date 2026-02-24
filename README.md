# AWS-Serverless-Image-Optimization-Pipeline
# Project Overview:

This project implements a fully serverless, event-driven image optimization pipeline on AWS. It allows users to upload images through a static web interface hosted on Amazon S3. The uploaded image automatically triggers an AWS Lambda function, which resizes and compresses the image into multiple resolutions. The optimized images are stored securely in an output S3 bucket and can be downloaded directly by users.

The system is built using serverless architecture, making it highly scalable, cost-efficient, fault-tolerant, and production-ready. This project demonstrates real-world cloud engineering skills using AWS services including S3, Lambda, API Gateway, IAM, and CloudWatch.

# File Summary:

-frontendimage.html – Frontend static website upload interface.

-imageresizefunction.py – AWS Lambda function for image resizing and optimization.

-architecture-diagram/ – Architectural diagram explaining the AWS setup.

-image-optimization-working-images/ – Screenshots showing successful project execution.

-README.md – Project documentation.

# Architectural Diagram:

![Image](https://github.com/user-attachments/assets/d5ff0d23-ada4-43da-9018-f5b25dd74831)

# Project Steps (Working):
# 1. Create frontend website

The frontend website is built using HTML and CSS and hosted on Amazon S3 as a static website. This serverless approach ensures high availability, scalability, and cost efficiency without managing servers.

# 2. Create S3 Buckets

Three S3 buckets were created:

Frontend Bucket – Hosts frontendimage.html

Input Bucket – Stores uploaded images

Output Bucket – Stores resized and optimized images



# 3. Enable Static Website Hosting

Static website hosting was enabled on the frontend S3 bucket. This allows the frontendimage.html file to be accessed publicly via browser without any backend servers.

Image

# 4. Create Lambda Execution Role (IAM)

An IAM role was created for the Lambda function with permissions to access S3 and write logs to CloudWatch, following AWS security best practices.

Image

# 5. Create Lambda Function – imageresizefunction

A Python-based AWS Lambda function named imageresizefunction was developed using the Pillow image processing library. 
The function:
-Receives image upload events
-Resizes images into multiple resolutions (1080p, 720p, 480p)
-Compresses images for optimized storage
-Stores processed images in the output S3 bucket

Image

# 6. Add Pillow Library Using Lambda Layers

Since AWS Lambda does not include Pillow by default, a Lambda Layer was created and attached to imageresizefunction, enabling advanced image processing.

Image

# 7. Configure S3 Event Trigger

The input S3 bucket was configured to trigger imageresizefunction automatically whenever a new image is uploaded, enabling fully event-driven processing.

Image

# 8. Setup API Gateway

Amazon API Gateway was used to expose imageresizefunction as a HTTP API endpoint. This allows the frontend interface to securely invoke the backend processing service.

Image

# 9.  Updated Frontend Interface

The frontend code (frontendimage.html) was modified to include the Amazon API Gateway invoke URL for backend integration. A simple HTML and CSS interface enables image uploads and displays download links for resized images returned by the backend.


Image

# 10. End-to-End Testing

The complete pipeline was tested successfully. 
Upon image upload:

-The Lambda function was automatically triggered

-Images were resized into multiple resolutions

-Optimized images were stored in the output bucket

-Users were able to download resized images

AWS Services Used:

-Amazon S3

-AWS Lambda

-Amazon API Gateway

-AWS IAM

-AWS CloudWatch

# Note:

All AWS resources used for this project were deleted after completion to avoid unintended charges, as the project was implemented using the AWS Free Tier.

