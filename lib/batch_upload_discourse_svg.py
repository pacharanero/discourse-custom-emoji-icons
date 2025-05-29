#!/usr/bin/env python

import os
import sys
import requests
from time import sleep
from dotenv import load_dotenv

def usage():
    print(f"Usage: {sys.argv[0]} [path/to/.env]")
    print("If no .env file is specified, defaults to './.env' in the current directory.")
    sys.exit(1)

def main():
    env_path = sys.argv[1] if len(sys.argv) > 1 else './.env'
    if not os.path.isfile(env_path):
        print(f".env file not found: {env_path}")
        usage()
    load_dotenv(env_path)

    DISCOURSE_BASE_URL = os.getenv('DISCOURSE_BASE_URL')
    API_USERNAME = os.getenv('DISCOURSE_API_USERNAME')
    API_KEY = os.getenv('DISCOURSE_API_KEY')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '../custom')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 5))
    WAIT_SECONDS = int(os.getenv('WAIT_SECONDS', 3))

    def upload_svg(filepath):
        with open(filepath, 'rb') as f:
            files = {'file': (os.path.basename(filepath), f, 'image/svg+xml')}
            payload = {
                'type': 'composer',
                'synchronous': 'true',
                'user_api_key': API_KEY,
                'api_username': API_USERNAME,
            }
            response = requests.post(
                f'{DISCOURSE_BASE_URL}/uploads.json',
                files=files,
                data=payload
            )
            if response.status_code == 200:
                return response.json()['url']
            else:
                print(f"Failed to upload {filepath}: {response.text}")
                return None

    def batch_upload():
        files = [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.svg')]
        for i in range(0, len(files), BATCH_SIZE):
            batch = files[i:i + BATCH_SIZE]
            for filepath in batch:
                print(f'Uploading {filepath}...')
                url = upload_svg(filepath)
                if url:
                    print(f'Uploaded: {url}')
            print(f'Batch {i // BATCH_SIZE + 1} done. Waiting {WAIT_SECONDS}s...')
            sleep(WAIT_SECONDS)

    batch_upload()

if __name__ == '__main__':
    main()

def upload_svg(filepath):
    with open(filepath, 'rb') as f:
        files = {'file': (os.path.basename(filepath), f, 'image/svg+xml')}
        payload = {
            'type': 'composer',
            'synchronous': 'true',
            'user_api_key': API_KEY,
            'api_username': API_USERNAME,
        }
        response = requests.post(
            f'{DISCOURSE_BASE_URL}/uploads.json',
            files=files,
            data=payload
        )
        if response.status_code == 200:
            return response.json()['url']
        else:
            print(f"Failed to upload {filepath}: {response.text}")
            return None

def batch_upload():
    files = [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.svg')]
    for i in range(0, len(files), BATCH_SIZE):
        batch = files[i:i + BATCH_SIZE]
        for filepath in batch:
            print(f'Uploading {filepath}...')
            url = upload_svg(filepath)
            if url:
                print(f'Uploaded: {url}')
        print(f'Batch {i // BATCH_SIZE + 1} done. Waiting {WAIT_SECONDS}s...')
        sleep(WAIT_SECONDS)
