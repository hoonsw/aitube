import random
from obs_adapter import OBSAdapter
from voicevox_adapter import VoiceVoxAdapter
from openap_adapter import OpenAPAdapter
from youtube_comment_adaptor import YoutubeCommentAdapter
from play_sound import PlaySound
from dotenv import load_dotenv
import os

class AITuberSystem:
  def __init__(self) -> None:
    video_id = os.getenv("YOUTUBE_VIDEO_ID")
    self.youtube_comment_adaptor = YoutubeCommentAdapter(video_id)
    self.openai_adapter = OpenAPAdapter()
    self.voice_adapter = VoiceVoxAdapter()
    self.obs_adapter = OBSAdapter()
    self.play_sound = PlaySound(output_device_name="CABLE Input (VB-Audio Virtual Cable)")

    pass

  def talk_with_comment(self) -> bool:
    print("コメントを読み込みます")
    comment = self.youtube_comment_adaptor.get_comment()

    if comment==None:
      print("コメントがありません")
      return False
    response_text = self.openai_adapter.create_chat(comment)
    data, rate = self.voice_adapter.get_voice(response_text)
    self.obs_adapter.set_question(comment)
    self.obs_adapter.set_answer(response_text)
    self.play_sound.play_sound(data, rate)
    return True
