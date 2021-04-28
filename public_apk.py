import http.client
import os
import requests
import pprint

# repositoty = os.environ["repository"]

tag = os.environ["GITHUB_REF"]

print("current tag" + tag)

# print("repository: " + repositoty)

# create_url = "https://api.github.com/repos/anantasak-pcru/wsm-release/releases"

# body = {
#     "accept": "application/vnd.github.v3+json",
#     "owner": "anantasak-pcru",
#     "repo": "wsm-release",
#     "tag_name": "1.0.1",
#     "name": "1.0.1",
#     "body": "1.0.1"
# }

# header = {
#     "Authorization": "Bearer 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",
#     "Content-Type": "application/json",
#     "Accept": "application/vnd.github.v3+json"
# }

# res = requests.post(url=create_url,headers=header, json=body)

# pprint.pprint(res.content)
# print("status: " + str(res.status_code))

# pyhton3 public_apk.py $repository=anantasak-pcru/wsm-release