
UPLOAD IMAGE PROJECT

DESCRIPTION
------------
This project enables users to upload images that are stored on Google Drive, and the URLs of the uploaded images displayed for the users so that they can directly view the images on the browser .

INSTALLATION PROCESS
---------------------
1. Clone the repository:
   ```
   git clone https://github.com/janhavi-naik14/upload_image.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install Django:
   ```
   pip install django
   ```

4. Navigate to the `imageuploader` directory:
   ```
   cd imageuploader
   ```

GOOGLE DRIVE INTEGRATION
-------------------------
1. Install the required Google Drive libraries:
   ```
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. Google Drive API activation:
   1. Go to the Google Cloud Console: https://console.cloud.google.com/
   2. Navigate to the IAM & Admin section and select Service accounts.
   3. Find the service account you’re using and click on the Actions (three dots) menu, then select Create key.
   4. Choose JSON as the key type and download the new key file.
   5. Put the JSON file in the `credentials.json` file in the `imageuploader/imageuploader` directory.

RUNNING MIGRATIONS
-------------------
1. Run migrations to apply the changes:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

RUNNING THE SERVER
-------------------
1. Start the Django development server:
   ```
   python manage.py runserver
   ```

DEMO VIDEO
-----------
The demo video of the whole webpage is in the project directory "demo_image_upload.mp4".

