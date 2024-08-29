import hashlib
import base64
from datetime import datetime
import time

def generate_license_key(expiry_date_time):
    """Generates a license key with an expiry date and time and a secure hash."""
    # Create a simple hash from the expiry date and time
    hash_object = hashlib.sha256(expiry_date_time.encode())
    hash_digest = hash_object.hexdigest()

    # Combine the expiry date and time and hash
    combined = expiry_date_time + '|' + hash_digest

    # Encode the combined string for simplicity
    encoded_key = base64.b64encode(combined.encode()).decode()
    return encoded_key

# Usage with user input
if __name__ == '__main__':
    user_input = input("Enter expiry date and time (YYYY-MM-DD HH:MM): ")
    try:
        # Validate the input format by attempting to parse it
        datetime.strptime(user_input, '%Y-%m-%d %H:%M')
        key = generate_license_key(user_input)
        print("Generated License Key:", key)
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD HH:MM")
    time.sleep(30)
