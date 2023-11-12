import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'open-interpreter'))


import interpreter

# interpreter.system_message  = "あなたは猫の一族の「ねこたろう」です。語尾に必ず「にゃん」をつけて。日本語で会話して"

# file_path = "/root/System/Gilgamesh_system_message.txt"
# file_path = "open-interpreter/interpreter/system_message.txt"
# with open(file_path, 'r', encoding='utf-8') as file:
#     gilgamesh_system_message = file.read().strip()

# print(gilgamesh_system_message)
# raise
# interpreter.system_message  = gilgamesh_system_message

interpreter.auto_run        = True
# interpreter.model           = "tiiuae/falcon-180B"
interpreter.model           = "TheBloke/Llama-2-13B-chat-GGUF"
interpreter.local           = True
interpreter.debug_mode      = True

# msg = interpreter.chat("AAPLとMETAの株価グラフを描いてください") # 一つのコマンドを実行
msg = interpreter.chat("あなたの名前は何？") # 一つのコマンドを実行
print(msg)
interpreter.chat() # インタラクティブなチャットを開始

