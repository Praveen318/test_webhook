import hmac
import hashlib

# Replace with your actual secret
secret = b'your_secret_here'

# Replace with your actual payload
payload = b'{"key":"value"}'

# Create the HMAC SHA-256 signature
signature = 'sha256=' + hmac.new(secret, payload, hashlib.sha256).hexdigest()

print(signature
