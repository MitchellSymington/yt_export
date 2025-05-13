
README - YouTube Video Metadata Export Tool (OAuth Ready)
==========================================================

This tool allows you to export all public videos from any YouTube channel into a CSV file, including:
- Title
- Description
- Published date
- Video ID
- View count
- Like count
- Comment count

You can use the ready-to-go credentials included, or migrate to your own Google account.

-------------------------------------------------------
📦 What's Included
-------------------------------------------------------

✅ Python script (`yt_export.py`)  
✅ OAuth credentials file (`client_secret.json`)  
✅ Automatically saved token after first login (`token.pkl`)  
✅ Fully configured Google Cloud project  
✅ Dedicated Google account created just for this project:
    - Email: ytclientproj@gmail.com
    - Password: ytclientproj123

You can run the tool immediately using this account.  
No setup on Google Cloud is needed unless you want to migrate.

-------------------------------------------------------
💻 Requirements
-------------------------------------------------------

1. Python 3 installed on your system
2. Internet connection
3. A terminal (Command Prompt on Windows or Terminal app on macOS/Linux)

-------------------------------------------------------
🔧 One-Time Setup
-------------------------------------------------------

### 1. Install Python

Download it from:
https://www.python.org/downloads

✔ On Windows: check “Add Python to PATH” during install.

---

### 2. Install Required Python Packages

Open your terminal and run:

**On Windows:**
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```

**On macOS/Linux:**
```
pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```

---

### 3. Extract Files

Place all files in the same folder:
- `yt_export.py`
- `client_secret.json`

-------------------------------------------------------
🚀 Running the Script
-------------------------------------------------------

Open the terminal in the project folder:

**On Windows:**
```
cd path\to\your\folder
python yt_export.py
```

**On macOS/Linux:**
```
cd /path/to/your/folder
python3 yt_export.py
```

The script will:

1. Show a green authorization link in the terminal
2. You copy or click the link, log in with:
   - Email: xxxxxxx@gmail.com
   - Password: xxxxxxxx
3. Authorize the app
4. Paste the returned code into the terminal

✔ Login is now saved. No need to repeat this next time.

-------------------------------------------------------
📁 Output
-------------------------------------------------------

The script creates a file:

```
youtube_video_data.csv
```

Which contains:
- Title
- Description
- Published At
- Video ID
- Views
- Likes
- Comments

You can open it with Excel, Google Sheets, or any text editor.

-------------------------------------------------------
🔁 OPTIONAL: Migrate to Your Own Google Account
-------------------------------------------------------

If you prefer to use your own Google account and project, follow these steps:

1. Go to https://console.cloud.google.com
2. Create a new project
3. Go to “APIs & Services > Library” and enable “YouTube Data API v3”
4. Go to “APIs & Services > Credentials”
5. Click “+ Create Credentials” > “OAuth Client ID”
6. Choose “Desktop App” and give it a name
7. Download the `client_secret.json` file
8. Replace the existing `client_secret.json` in your script folder with your new file
9. Run the script again and authorize with your own Google account

✔ Once authorized, your new token will be saved and used automatically from then on.

-------------------------------------------------------
🔐 Notes
-------------------------------------------------------

- The included Google account is for demo/testing purposes
- For commercial or production use, you should create and use your own OAuth credentials
- The login step only happens once; a token is saved afterward

Enjoy exporting your YouTube channel data! 🎉
