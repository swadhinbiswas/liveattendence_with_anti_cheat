import os


filepath=os.listdir("/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures")
ids=[]
for file in filepath:
  
  id=file.split(".")[0]
  ids.append(id)
  

print(ids)
  