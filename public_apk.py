import http.client
import os
import requests
import pprint
from dotenv import load_dotenv

load_dotenv()

repository = os.environ["REPOSITORY"]
tag = os.environ["GITHUB_REF"].split('/')[2]
body = os.environ.get("BODY", "Changelog")
assets = os.environ["ASSETS"].split(" ")
uploadUrl = ""
releaseId = ""
token = os.environ["GITHUB_TOKEN"]

create_url = "https://api.github.com/repos/{}/releases".format(repository)

# print(create_url)
# print("tag " + tag)

body = {
    "accept": "application/vnd.github.v3+json",
    "owner": repository.split('/')[0],
    "repo": repository.split('/')[1],
    "tag_name": tag,
    "name": tag
}

header = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Accept": "application/vnd.github.v3+json"
}

print("🚀🚀 Create release...")

res = requests.post(url=create_url,headers=header, json=body)


if(res.status_code == 201):
    print("🎉🎉 Created release success at " + repository)
    uploadUrl = str(res.json()['upload_url']).replace("{?name,label}", "")
    releaseId = str(res.json()['id'])
else: 
    print("🛑🛑 Can't create release " + tag)
    print(res.json()['message'])
    raise Exception("Can't create release " + tag)

print("🚀🚀 Uploading assets...")

for asset in assets:
    fileName = asset.split('/')[-1]
    url = uploadUrl + "?name=" + fileName
    files = {"file": (fileName, open(asset, 'rb'), 'multipart/form-data')}
    res = requests.post(url, files=files, headers=header)
    if(res.status_code == 201):
        print("🎉🎉 Uploading success " + fileName)
    else:
        print("🛑 Upload " + fileName + " error")