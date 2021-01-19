import vk
import time

session = vk.Session(access_token='token')
api = vk.API(session,v='5.35')
wallget=api.video.get(owner_id=id)
post = wallget['items']
for post1 in post:
    api.video.delete(owner_id=post1['owner_id'],video_id=post1['id'],target_id=id)
  
