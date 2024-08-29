import hashlib
import base64
from datetime import datetime
import time
import sys

license_key = "MjAyNC0wOC0yOCAyMzoxMXw4OTAzMTBjNTFmYjI3YTZkOGVjMWVlZGZlODE2Yzg3MGRhNzYxOWFlNTJmZmZlZTJjZmVjZTg1YTk3OTVlZmYx"

def validate_license(key):
    """Validates the license key from the config."""
    try:
        decoded_bytes = base64.b64decode(key.encode())
        decoded_string = decoded_bytes.decode()
        expiry_date_str, provided_hash = decoded_string.split('|')
        hash_object = hashlib.sha256(expiry_date_str.encode())
        valid_hash = hash_object.hexdigest()
        if provided_hash != valid_hash:
            raise ValueError("Invalid license key.")
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d %H:%M')  # Updated to include time
        if datetime.now() > expiry_date:
            raise ValueError("License has expired.")
        return expiry_date
    except Exception as e:
        print("Error validating license:", str(e))
        sys.exit(1)

expiry_date = validate_license(license_key)

def countdown():
    while datetime.now() < expiry_date:
        remaining_time = expiry_date - datetime.now()
        print(remaining_time)
        time.sleep(1)
    print("License has expired.")
    sys.exit(1)

validate_license(license_key)
countdown()
