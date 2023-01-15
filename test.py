import pandas
from googleapiclient.discovery import build

import warnings # 경고창 무시
warnings.filterwarnings('ignore')

api_key = "AIzaSyCWZkgnvRZ2dIl0N_DOZZcutUTKY63n8-A"
youtube_link = input("input youtube link : ")
print()
print()
print()
vedio_id = youtube_link.replace("https://www.youtube.com/watch?v=", "")

comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=vedio_id, maxResults=10).execute()

while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                print(reply_item)
                print()
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId='sWC-pp6CXpA', pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break
