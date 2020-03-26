from storages.backends.s3boto3 import S3Boto3Storage

class PPStaticStorage(S3Boto3Storage):
    """ Store static files under S3 static directory """
    location = 'static'

class PPMediaStorage(S3Boto3Storage):
    """ Store media files (advert images) under S3 adverts directory """
    location = 'adverts'