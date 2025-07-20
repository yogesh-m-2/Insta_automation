import requests
import time


# --- REQUIRED CONFIGURATION ---
ACCESS_TOKEN = 'IGAARQi67MLB1BZAFBkNjF4N2ZAieEVuanp2RzYxTWZASM3YzN1doVFNhUDZAycFZAGNk5HV25OZAXU0VUJ3dGJUbHdHYnRkdjBtNlZAPcTZA2WWJKWEJDbk1LQkRhczJXTUxoZAVJCTVhjWFBseUtvYmJ0bTBGcGVTT2IzTFdycnBDejRnbwZDZD'  # Replace with your access token
IG_USER_ID = '17841475573024879' #'9067993099967051'  # Replace with your Instagram User ID
IMAGE_URL = 'https://www.skywaytour.com/media/gallery/2023-01-23-12-01-30-9HistoricalPlacesYouShouldVisitInKarnataka1.jpg'
CAPTION = 'Hello from the Instagram Graph API!'

def upload_to_instagram(IMAGE_URL,CAPTION=""):
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