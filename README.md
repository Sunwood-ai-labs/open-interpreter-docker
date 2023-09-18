# open-interpreter-docker

解説ブログはこちら

https://hamaruki.com/can-open-interpreters-be-installed-on-office-pcs/



```
docker-compose exec open-interpreter /bin/bash
```

```
interpreter
```


## Q1

`from sklearn.datasets import fetch_california_housing`これを用いてカリフォルニア住宅価格のデータセットを用いて住宅価格の回帰予測をstep-by-stepで行って


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



```

Microsoft Windows [Version 10.0.22621.2283]
(c) Microsoft Corporation. All rights reserved.

C:\Users\solar>cd C:\Prj\open-interpreter-docker

C:\Prj\open-interpreter-docker>docker-compose up -d
[+] Running 1/1
 ✔ Container open-interpreter-docker-open-interpreter-1  Started                                                                    0.0s

C:\Prj\open-interpreter-docker>docker-compose exec open-interpreter /bin/bash
root@465aaa3eb215:~# ls
Dockerfile  README.md  docker-compose.yml  scikit_learn_data
root@465aaa3eb215:~# interpreter

●

Welcome to Open Interpreter.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

▌ OpenAI API key not found

To use GPT-4 (recommended) please provide an OpenAI API key.

To use Code-Llama (free but less capable) press enter.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
OpenAI API key:

▌ Switching to Code-Llama...

Tip: Run interpreter --local to automatically use Code-Llama.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Open Interpreter will use Code Llama for local execution. Use your arrow keys to set up the model.

[?] Parameter count (smaller is faster, larger is more capable): 7B
 > 7B
   13B
   34B

[?] Quality (smaller is faster, larger is more capable): Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
   Small | Size: 2.6 GB, Estimated RAM usage: 5.1 GB
 > Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
   Large | Size: 6.7 GB, Estimated RAM usage: 9.2 GB
   See More

[?] Use GPU? (Large models might crash on GPU, but will run more quickly) (Y/n): n

Model found at /root/.local/share/Open Interpreter/models/codellama-7b-instruct.Q4_K_M.gguf

▌ Model set to TheBloke/CodeLlama-7B-Instruct-GGUF

Open Interpreter will require approval before running code. Use interpreter -y to bypass this.

Press CTRL-C to exit.

> `from sklearn.datasets import fetch_california_housing`これを用いてカリフォルニア住宅価格のデータセットを用いて住宅価格の回帰予測を行って




  from sklearn.datasets import fetch_california_housing


  Would you like to run this code? (y/n)

  y


  from sklearn.datasets import fetch_california_housing



  I'll ask you what you would like to do next. Would you like me to run another piece of code or provide more information about the
  California Housing dataset?

>
Exception in thread Thread-2 (save_and_display_stream):
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
root@465aaa3eb215:~# interpreter

●

Welcome to Open Interpreter.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
▌ OpenAI API key not found

To use GPT-4 (recommended) please provide an OpenAI API key.

To use Code-Llama (free but less capable) press enter.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
OpenAI API key:

▌ Switching to Code-Llama...

Tip: Run interpreter --local to automatically use Code-Llama.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Open Interpreter will use Code Llama for local execution. Use your arrow keys to set up the model.

[?] Parameter count (smaller is faster, larger is more capable): 7B
 > 7B
   13B
   34B

[?] Quality (smaller is faster, larger is more capable): Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
   Small | Size: 2.6 GB, Estimated RAM usage: 5.1 GB
 > Medium | Size: 3.8 GB, Estimated RAM usage: 6.3 GB
   Large | Size: 6.7 GB, Estimated RAM usage: 9.2 GB
   See More

[?] Use GPU? (Large models might crash on GPU, but will run more quickly) (Y/n): Y

Model found at /root/.local/share/Open Interpreter/models/codellama-7b-instruct.Q4_K_M.gguf

▌ Model set to TheBloke/CodeLlama-7B-Instruct-GGUF

Open Interpreter will require approval before running code. Use interpreter -y to bypass this.

Press CTRL-C to exit.

> `from sklearn.datasets import fetch_california_housing`これを用いてカリフォルニア住宅価格のデータセットを用いて住宅価格の回帰予測をstep-by-stepで行って




  from sklearn.datasets import fetch_california_housing


  Would you like to run this code? (y/n)

  y


  from sklearn.datasets import fetch_california_housing



  I will now proceed to load the California Housing dataset using the fetch_california_housing function from scikit-learn.



  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()


  Would you like to run this code? (y/n)

  y


  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()



  I will now proceed to explore the California Housing dataset.



  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)


  Would you like to run this code? (y/n)

  y



  from sklearn.datasets import fetch_california_housing

  from sklearn.datasets import fetch_california_housing

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█



  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█



  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group
  - HouseAge      median house age in block group

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group
  - HouseAge      median house age in block group

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)█


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group
  - HouseAge      median house age in block group

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group
  - HouseAge      median house age in block group

  from sklearn.datasets import fetch_california_housing
  housing = fetch_california_housing()
  print(housing.DESCR)


  .. _california_housing_dataset:
  California Housing dataset
  --------------------------
  **Data Set Characteristics:**
  :Number of Instances: 20640
  :Number of Attributes: 8 numeric, predictive attributes and the target
  :Attribute Information:
  - MedInc        median income in block group
  - HouseAge      median house age in block group
  - AveRooms      average number of rooms per household
  - AveBedrms     average number of bedrooms per household
  - Population    block group population
  - AveOccup      average number of household members
  - Latitude      block group latitude
  - Longitude     block group longitude
  :Missing Attribute Values: None
  This dataset was obtained from the StatLib repository.
  https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html
  The target variable is the median house value for California districts,
  expressed in hundreds of thousands of dollars ($100,000).
  This dataset was derived from the 1990 U.S. census, using one row per census
  block group. A block group is the smallest geographical unit for which the U.S.
  Census Bureau publishes sample data (a block group typically has a population
  of 600 to 3,000 people).
  A household is a group of people residing within a home. Since the average
  number of rooms and bedrooms in this dataset are provided per household, these
  columns may take surprisingly large values for block groups with few households
  and many empty houses, such as vacation resorts.
  It can be downloaded/loaded using the
  :func:`sklearn.datasets.fetch_california_housing` function.
  .. topic:: References
  - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
  Statistics and Probability Letters, 33 (1997) 291-297



  it appears that the California Housing dataset is a collection of features and target variable for predicting median house value in
  California districts. The dataset contains 8 numeric attributes and one target variable, which is the median house value expressed in
  hundreds of thousands of dollars ($100,000).

  I will now proceed to explore the California Housing dataset further by visualizing the distribution of the target variable.



  import matplotlib.pyplot as plt
  plt.hist(housing.target)
  plt.xlabel('Median House Value')
  plt.ylabel('Frequency')
  plt.title('Distribution of Median House Value')
  plt.show()


  Would you like to run this code? (y/n)



> y




  import matplotlib.pyplot as plt
  plt.hist(housing.target)
  plt.xlabel('Median House Value')
  plt.ylabel('Frequency')
  plt.title('Distribution of Median House Value')
  plt.show()


  Would you like to run this code? (y/n)

  y


  import matplotlib.pyplot as plt
  plt.hist(housing.target)
  plt.xlabel('Median House Value')
  plt.ylabel('Frequency')
  plt.title('Distribution of Median House Value')
  plt.show()


  (array([ 877., 3612., 4099., 3771., 2799., 1769., 1239.,  752.,  479.,
  1243.]), array([0.14999 , 0.634992, 1.119994, 1.604996, 2.089998, 2.575   ,
  3.060002, 3.545004, 4.030006, 4.515008, 5.00001 ]), <BarContainer object of 10 artists>)
  Text(0.5, 0, 'Median House Value')
  Text(0, 0.5, 'Frequency')
  Text(0.5, 1.0, 'Distribution of Median House Value')


  it appears that the median house value in California districts is distributed as follows:

   • The lowest value is $877
   • The highest value is $5000
   • There are approximately 1243 values between these two extremes

  I will now proceed to explore the distribution of the other attributes in the dataset.



  import matplotlib.pyplot as plt
  plt.hist(housing.data[:, 1:])
  plt.xlabel('Attribute')
  plt.ylabel('Frequency')
  plt.title('Distribution of Attributes')
  plt.show()


  Would you like to run this code? (y/n)

  y


  import matplotlib.pyplot as plt
  plt.hist(housing.data[:, 1:])
  plt.xlabel('Attribute')
  plt.ylabel('Frequency')
  plt.title('Distribution of Attributes')
  plt.show()


  (array([[2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
  [2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
  [2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
  [1.9726e+04, 7.9600e+02, 1.0000e+02, 1.2000e+01, 4.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00, 1.0000e+00],
  [2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
  [2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
  [2.0640e+04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
  0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), array([ -124.35 ,  3456.285,  7036.92 , 10617.555, 14198.19 ,
  17778.825,
  21359.46 , 24940.095, 28520.73 , 32101.365, 35682.   ]), <a list of 7 BarContainer objects>)
  Text(0.5, 0, 'Attribute')
  Text(0, 0.5, 'Frequency')
  Text(0.5, 1.0, 'Distribution of Attributes')


  it appears that there are 7 attributes in the dataset and their frequencies are distributed as follows:

   • The lowest value is -124.35
   • The highest value is 35682.0
   • There are approximately 1243 values between these two extremes

  I will now proceed to explore the distribution of the other attributes in the dataset.



  import matplotlib.pyplot as plt
  plt.hist(housing.data[:, 2:])
  plt.xlabel('Attribute')
  plt.ylabel('Frequency')
  plt.title('Distribution of Attributes')
  plt.show()


  Would you like to run this code? (y/n)

```