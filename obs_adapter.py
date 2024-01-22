import obsws_python as obs 
import os
from dotenv import load_dotenv

class OBSAdapter:
  def __init__(self) -> None:
    load_dotenv()
    password = os.environ.get("OBS_WS_PASSWORD")
    host = os.environ.get("OBS_WS_HOST")
    port = os.environ.get("OBS_WS_PORT")
    # エラー処理
    if(password == None or host == None  or port == None):
      raise Exception("OBSの設定が環境変数に設定されていません")
    self.ws = obs.ReqClient(host=host, port=port, password=password)

  def set_question(self, text:str):
    self.ws.set_input_settings(name = "Question", settings = {"text": text}, overlay=True)

  def set_answer(self, text:str):
    self.ws.set_input_settings(name = "Answer", settings = {"text": text}, overlay=True)
  
# fileを直接指定したとき(text, debugging)
if __name__ == "__main__":
  obsAdapter = OBSAdapter()
  import random
  text = "Questionの番号は" + str(random.randint(0, 100))
  obsAdapter.set_question(text)

  answer_text = "Answerの番号は" + str(random.randint(0, 100))
  obsAdapter.set_answer(answer_text)
