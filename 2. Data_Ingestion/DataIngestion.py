# Databricks notebook source
import requests
import boto3
import json
import time
from datetime import datetime, timedelta

TWELVEDATA_API_KEY = 'api_key_here'  
aws_access_key_id = 's3_access_key'
aws_secret_access_key = 's3_secret_key'
region_name = 'region-name'
bucket_name = 'your_bucket_name'


# Initialize boto3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Test S3 connection
try:
    s3.put_object(Bucket=bucket_name, Key='upload.txt', Body='S3 connection successful!')
    print("Test upload succeeded! Check S3 for 'test_upload.txt'.")
except Exception as e:
    print("S3 upload failed:", e)

# COMMAND ----------

def get_ohlcv_twelvedata(symbol, interval="1day", days=30):
    """
    Fetch OHLCV data from TwelveData for the past `days` days.
    """
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": days,
        "apikey": TWELVEDATA_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "values" in data:
            values = reversed(data["values"])  # Reverse to get oldest first
            return [
                {
                    "date": v["datetime"],
                    "open": float(v["open"]),
                    "high": float(v["high"]),
                    "low": float(v["low"]),
                    "close": float(v["close"]),
                    "volume": float(v["volume"])
                }
                for v in values
            ]
        else:
            print(f"No data for {symbol}: {data.get('message')}")
    else:
        print(f"Failed to fetch OHLCV for {symbol}: {response.status_code}")
    return []


# COMMAND ----------

import pandas as pd 
symbols = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "NVDA"]


for symbol in symbols:
    print(f"Processing {symbol}...")
    ohlcv_data = get_ohlcv_twelvedata(symbol, days=30)

    if ohlcv_data:
        try:
            df = pd.DataFrame(ohlcv_data)
            csv_buffer = df.to_csv(index=False)
            file_key = f"ohlcv/{symbol}.csv"

            s3.put_object(
                Bucket=bucket_name,
                Key=file_key,
                Body=csv_buffer,
                ContentType="text/csv"
            )
            print(f" Uploaded {symbol}.csv successfully.")
        except Exception as e:
            print(f" Failed to upload {symbol}: {e}")
    time.sleep(7.5)

print("All symbols uploaded individually to S3 as CSV files!")
