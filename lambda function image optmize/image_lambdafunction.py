import json
import boto3
from PIL import Image
import io
import base64
import uuid

s3 = boto3.client('s3')

INPUT_BUCKET = "imageoptimize-input-ms"
OUTPUT_BUCKET = "imageoptimize-output-ms"

sizes = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "480p": (854, 480)
}

def lambda_handler(event, context):
    try:
        body = event['body']

        # HTTP API sends base64 encoded body
        if event.get("isBase64Encoded"):
            file_content = base64.b64decode(body)
        else:
            file_content = body.encode()

        # Unique filename
        filename = f"{uuid.uuid4()}.jpg"

        # Upload original image
        s3.put_object(
            Bucket=INPUT_BUCKET,
            Key=filename,
            Body=file_content,
            ContentType="image/jpeg"
        )

        img = Image.open(io.BytesIO(file_content))

        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        urls = {}

        for label, size in sizes.items():
            resized = img.copy()
            resized.thumbnail(size)

            buffer = io.BytesIO()
            resized.save(buffer, "JPEG", quality=85)
            buffer.seek(0)

            key = f"{label}-{filename}"

            s3.put_object(
                Bucket=OUTPUT_BUCKET,
                Key=key,
                Body=buffer,
                ContentType="image/jpeg"
            )

            presigned_url = s3.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': OUTPUT_BUCKET,
                    'Key': key
                },
                ExpiresIn=3600
            )

            urls[label] = presigned_url

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "images": urls
            })
        }

    except Exception as e:
        print(str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }