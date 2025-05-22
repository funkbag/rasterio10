import rasterio
import numpy as np

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Rasterio and Numpy loaded successfully!"
    }
