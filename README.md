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


# Project Steps (Working):
# 1. Create frontend website

The frontend website is built using HTML and CSS and hosted on Amazon S3 as a static website. This serverless approach ensures high availability, scalability, and cost efficiency without managing servers.

# 2. Create S3 Buckets

Three S3 buckets were created:

Frontend Bucket – Hosts frontendimage.html

Input Bucket – Stores uploaded images

Output Bucket – Stores resized and optimized images

