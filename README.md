# Discourse Custom Emoji Icons
This project allows you to upload custom emoji icons to your Discourse forum.

## Setup
1. Copy `lib/example.env` to `lib/somename.env` and fill in your Discourse credentials.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the batch upload script:
```
python run_batch_upload.py
```
This will read the emoji files from the `emoji` directory in batches and upload them to your Discourse forum.