import requests
import time


# --- REQUIRED CONFIGURATION ---
ACCESS_TOKEN = ''  # Replace with your access token
IG_USER_ID = '9067993099967051'  # Replace with your Instagram User ID
IMAGE_URL = 'https://sdmntprwestus.oaiusercontent.com/files/00000000-c540-6230-ba45-19968b448a22/raw?se=2025-06-05T18%3A03%3A49Z&sp=r&sv=2024-08-04&sr=b&scid=5fcd484b-159e-533c-a045-cb384708e303&skoid=7399a3a4-0259-4d43-bcd6-a56ceeb4c28b&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-06-05T16%3A27%3A46Z&ske=2025-06-06T16%3A27%3A46Z&sks=b&skv=2024-08-04&sig=/%2Bfxl%2B6ZhTFxqSuPnTYYajvjDHxBNm91/ToV%2B1BSWBU%3D'
CAPTION = 'Hello from the Instagram Graph API!'
API_VERSION = 'v22.0'  # Can also use 'v19.0' or current latest

# --- STEP 1: Create Media Container ---
create_container_url = f'https://graph.instagram.com/{API_VERSION}/{IG_USER_ID}/media'

payload = {
    'image_url': IMAGE_URL,
    'caption': CAPTION,
    'access_token': ACCESS_TOKEN
}

print("Creating media container...")
res = requests.post(create_container_url, json=payload)
res_json = res.json()

if 'id' not in res_json:
    print("Error creating container:", res_json)
    exit()

container_id = res_json['id']
print("Media container created:", container_id)

# --- OPTIONAL: Wait briefly before publishing ---
time.sleep(2)

# --- STEP 2: Publish Media ---
publish_url = f'https://graph.instagram.com/{API_VERSION}/{IG_USER_ID}/media_publish'
publish_payload = {
    'creation_id': container_id,
    'access_token': ACCESS_TOKEN
}

print("Publishing media...")
publish_res = requests.post(publish_url, data=publish_payload)
publish_json = publish_res.json()

if 'id' in publish_json:
    print("Media published successfully! Post ID:", publish_json['id'])
else:
    print("Error publishing media:", publish_json)
