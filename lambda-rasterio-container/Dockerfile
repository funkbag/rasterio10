FROM public.ecr.aws/lambda/python:3.9

# System dependencies for rasterio
RUN yum install -y gcc gdal gdal-devel python3-devel libcurl-devel zip

# Install rasterio + numpy
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy your function code
COPY app.py .

# Set the command to your handler
CMD ["app.lambda_handler"]
