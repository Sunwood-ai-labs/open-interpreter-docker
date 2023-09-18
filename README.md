# open-interpreter-docker

```
docker-compose exec open-interpreter /bin/bash
```

```
interpreter
```


## Q1

`from sklearn.datasets import fetch_california_housing`これを用いてカリフォルニア住宅価格のデータセットを用いて住宅価格の回帰予測を行って

### A1

```

C:\Prj\open-interpreter-docker>docker-compose up -d
[+] Running 1/1
 ✔ Container open-interpreter-docker-open-interpreter-1  Started   0.0s

C:\Prj\open-interpreter-docker>docker-compose exec open-interpreter /bin/bash
root@465aaa3eb215:~# interpreter

●

Welcome to Open Interpreter.

────────────────────────────────────────────────────────────────────────

▌ OpenAI API key not found

To use GPT-4 (recommended) please provide an OpenAI API key.

To use Code-Llama (free but less capable) press enter.

────────────────────────────────────────────────────────────────────────

OpenAI API key:

▌ Switching to Code-Llama...

Tip: Run interpreter --local to automatically use Code-Llama.

────────────────────────────────────────────────────────────────────────

Open Interpreter will use Code Llama for local execution. Use your arrowkeys to set up the model.

[?] Parameter count (smaller is faster, larger is more capable): 7B
 > 7B
   13B
   34B

[?] Quality (smaller is faster, larger is more capable): Small | Size: 2[?] Quality (smaller is faster, larger is more capable): Medium | Size: [?] Quality (smaller is faster, larger is more capable): Large | Size: 6.7 GB, Estimated RAM usage: 9.2 GB RAM usage: 5.1 GB
   Small | Size: 2.6 GB, Estimated RAM usage: 5.1 GB
   Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
 > Large | Size: 6.7 GB, Estimated RAM usage: 9.2 GB
   See More

[?] Use GPU? (Large models might crash on GPU, but will run more qu...: n

Model found at /root/.local/share/Open
Interpreter/models/codellama-7b-instruct.Q8_0.gguf

▌ Model set to TheBloke/CodeLlama-7B-Instruct-GGUF

Open Interpreter will require approval before running code. Use
interpreter -y to bypass this.

Press CTRL-C to exit.

> `from sklearn.datasets import fetch_california_housing`これを用いてカ
リフォルニア住宅価格のデータセットを用いて住宅価格の回帰予測を行って




  from sklearn.datasets import fetch_california_housing


  Would you like to run this code? (y/n)

  y


  from sklearn.datasets import fetch_california_housing



  I will now proceed to run the next line of code.



  from sklearn.model_selection import train_test_split


  Would you like to run this code? (y/n)

  y


  from sklearn.model_selection import train_test_split

```