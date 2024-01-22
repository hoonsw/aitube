from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

input_str = "日本語しかできないのか"
voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound("Headphones")
data, rate = voicevox_adapter.get_voice(input_str)
play_sound.play_sound(data, rate)