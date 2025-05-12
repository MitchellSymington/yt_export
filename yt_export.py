import pandas as pd
import os
import pickle
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scope of access — read-only access to YouTube data
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# Replace with the filename of your downloaded OAuth credentials JSON
CREDENTIALS_FILE = "client_secret_640199845672-gm2im8ekeg12v1adb0kkmdkmllv8kfk3.apps.googleusercontent.com.json"
#"client_secret_XXXXX.json"

# Replace with the target YouTube channel ID (starts with 'UC...')
CHANNEL_ID = "UCQrbqsVHRljAsoi0SnOKhpQ"
#"YOUR_CHANNEL_ID" #exemple UCQrbqsVHRljAsoi0SnOKhpQ

# Defina estes valores no seu script
# SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
# CREDENTIALS_FILE = "client_secret_XXXX.json"

def authenticate():
    creds = None

    # Load saved token if available
    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as token_file:
            creds = pickle.load(token_file)

    # If no valid token, go through manual auth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(
                CREDENTIALS_FILE,
                scopes=SCOPES,
                redirect_uri='urn:ietf:wg:oauth:2.0:oob'
            )

            auth_url, _ = flow.authorization_url(prompt='consent')

            # Highlight the link in green and keep it visible
            print(f"\n\033[92m[Authorize this app by visiting the link below:]\033[0m\n{auth_url}\n")

            code = input("Paste the authorization code here: ").strip()
            flow.fetch_token(code=code)
            creds = flow.credentials

            # Save token for future runs
            with open("token.pkl", "wb") as token_file:
                pickle.dump(creds, token_file)

    return creds

def get_all_video_ids(youtube, channel_id):
    """
    Retrieves all video IDs from the specified YouTube channel.
    Handles pagination to fetch more than 50 results.
    """
    video_ids = []
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,
        type="video"
    )

    while request:
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['id']['videoId'])

        request = youtube.search().list_next(request, response)

    return video_ids

def get_video_details(youtube, video_ids):
    """
    Fetches detailed information (title, description, stats) for a list of video IDs.
    """
    video_data = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        request = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(batch)
        )
        response = request.execute()

        for item in response["items"]:
            snippet = item["snippet"]
            stats = item.get("statistics", {})
            video_data.append({
                "Title": snippet.get("title", ""),
                "Description": snippet.get("description", ""),
                "Published At": snippet.get("publishedAt", ""),
                "Video ID": item["id"],
                "Views": stats.get("viewCount", "0"),
                "Likes": stats.get("likeCount", "0"),
                "Comments": stats.get("commentCount", "0")
            })
    return video_data

def main():
    print("Authenticating...")
    credentials = authenticate()
    youtube = build("youtube", "v3", credentials=credentials)

    print("Fetching video IDs...")
    video_ids = get_all_video_ids(youtube, CHANNEL_ID)
    print(f"Total videos found: {len(video_ids)}")

    print("Fetching video details...")
    video_data = get_video_details(youtube, video_ids)

    df = pd.DataFrame(video_data)
    df.to_csv("youtube_video_data.csv", index=False, encoding='utf-8-sig')
    print("Data successfully exported to youtube_video_data.csv")

if __name__ == "__main__":
    main()