import vk
import time

session = vk.Session(access_token='c6d34f3d6f7f9ae98a1e9eb5270f5b9c569da5f7f8625883c7fb69a5f76f30a7bc2579850dbd0dc68fe9e')
api = vk.API(session,v='5.35')
wallget=api.video.get(owner_id=53065529)
post = wallget['items']
for post1 in post:
    api.video.delete(owner_id=post1['owner_id'],video_id=post1['id'],target_id=53065529)
  