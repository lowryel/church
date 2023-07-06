### church
**client project - church website**

#### Serving static and media content via s3
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'church/static'),
]

AWS_ACCESS_KEY_ID = "AKIASECII6YKDDD3Z4W4"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'bekoe-artifact'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static/'
STATICFILES_STORAGE = 'church.storage_backend.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = 'media/'
DEFAULT_FILE_STORAGE = 'church.storage_backend.MediaStorage'
```


#### AWS CORS for web fonts -->
```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://localhost:8000"
        ],
        "ExposeHeaders": []
    }
]
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://www.example2.com"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
