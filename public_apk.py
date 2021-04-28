import http.client
import os
import requests
import pprint

repositoty = os.environ["REPOSITORY"]
tag = os.environ["GITHUB_REF"].split('/')[2]
body = os.environ["BODY"].split(" ")
assets = os.environ["ASSETS"]
uploadUrl = ""
releaseId = ""
token = os.environ["GITHUB_TOKEN"]

create_url = "https://api.github.com/repos/anantasak-pcru/wsm-release/releases"

body = {
    "accept": "application/vnd.github.v3+json",
    "owner": "anantasak-pcru",
    "repo": "wsm-release",
    "tag_name": tag,
    "name": tag,
    "body": body
}

header = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Accept": "application/vnd.github.v3+json"
}

print("🚀🚀 Create relase...")

res = requests.post(url=create_url,headers=header, json=body)


# if(res.status_code == 200):
print("🎉🎉 Created relase success at " + repositoty)
uploadUrl = str(res.json()['upload_url']).replace("{?name,label}", "")
releaseId = str(res.json()['id'])
# else: exit(0)

print("🚀🚀 Uploading assets...")

for asset in assets:
    fileName = asset.split('/')[-1]
    url = uploadUrl + "?name=" + fileName
    files = {"file": (fileName, open(assets, 'rb'), 'multipart/form-data')}
    res = requests.post(url, files=files, headers=header)
    # if(res.status_code == 200):
    print("🎉🎉 Uploading success " + fileName)