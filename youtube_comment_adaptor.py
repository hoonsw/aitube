import pytchat
import json

class YoutubeCommentAdapter:
  def __init__(self,video_id) -> None:
    self.chat = pytchat.create(video_id=video_id.interruptable=False)
  
  def get_comments(self):
    # コメントを取得
    comments = self.__get_comments()
    if(comments==None):
      return None
    comments = comments[-1] # 最新のコメントを取得
    #　コメント情報の中からコメントのみを取得
    message = comments.get("message")
    return message
  
  def __get_comments(self): 
    if(self.chat.is_alive()==False):
      print("開始してません")
      return None
    comments = json.loads(self.chat.get().json())
    if(comments==[]):
      print("コメント取得失敗")
      return None
    return comments
  
if __name__ == "__main__":
  import time
  video_id = ""
  chat = YoutubeCommentAdapter(video_id)
  time.sleep(1) #少し持つ
  print(chat.get_comments()) 