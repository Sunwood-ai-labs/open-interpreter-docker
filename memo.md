interpreter --model Xwin-LM/Xwin-LM-7B-V0.1 --local
interpreter --model TheBloke/Llama-2-13B-chat-GGUF --local --auto_run
interpreter --model TheBloke/TigerBot-70B-Chat-GGUF


interpreter --model TheBloke/Airoboros-L2-13B-3.1.1-GGUF --local --auto_run
interpreter --model mistralai/Mistral-7B-v0.1 --local
interpreter --model huggingface/mistralai/Mistral-7B-v0.1
docker-compose exec open-interpreter /bin/bash

interpreter --model huggingface/WizardLM/WizardCoder-Python-34B-V1.0

interpreter --model huggingface/TheBloke/Mistral-7B-Instruct-v0.1-GGUF --local --auto_run
interpreter --model TheBloke/Mistral-7B-Instruct-v0.1-GGUF --local --auto_run
interpreter --model TheBloke/Mistral-7B-Instruct-v0.1-GGUF --local --auto_run

interpreter --model huggingface/TheBloke/Mistral-7B-Instruct-v0.1-GGUF --local -y --api_base http://host.docker.internal:1234/v1/chat/completions
interpreter --model huggingface/TheBloke/Mistral-7B-Instruct-v0.1-GGUF --local -y --api_base http://localhost:1234/v1
interpreter --local -y --api_base http://host.docker.internal:1234/v1/chat/completions
interpreter --local -y --api_base http://host.docker.internal:1234/v1

http://host.docker.internal:1234/v1/chat/completions
host.docker.internal 
http://host.docker.internal:1234/v1

curl http://host.docker.internal:1234/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{ 
  "messages": [ 
    { "role": "system", "content": "Always answer in rhymes." },
    { "role": "user", "content": "Introduce yourself." }
  ], 
  "temperature": 0.7, 
  "max_tokens": -1,
  "stream": false
}'