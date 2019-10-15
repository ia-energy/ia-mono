from flask_sqlalchemy import SQLAlchemy
from app.config import ia_config as config
import boto3
db = SQLAlchemy()
s3 = boto3.client('s3',
    aws_access_key_id=config['boto3']['aws_access_key_id'],
    aws_secret_access_key=config['boto3']['aws_secret_access_key'])
