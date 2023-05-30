# EL331 teamL Final Project
s1280160_Yusei Ichikawa (Reader)  
s1280124_Toshiki Ogata  
s1260247_Shouya Hurukawa  

Original Repository: https://github.com/gkhayes/author_attribution  
We using a datasets by original repository.  

## How to use
### Step1. Refactoring Datasets
We need refactoring Original Repository's datasets. Remove not needed line breaks to make a one sentence.  
Running ` refactoring.py ` will refactor the ` .txt ` in `./before_refactoring `
```
$ python refactoring.py

Before: (./before_refactoring/Anne_of_Avonlea.txt)
A tall, slim girl, “half-past sixteen,” with serious gray eyes and hair
which her friends called auburn, had sat down on the broad red sandstone
doorstep of a Prince Edward Island farmhouse one ripe afternoon in
August, firmly resolved to construe so many lines of Virgil.

After: (./after_refactoring/Anne_of_Avonlea.txt)
A tall, slim girl, “half-past sixteen,” with serious gray eyes and hair which her friends called auburn, had sat down on the broad red sandstone doorstep of a Prince Edward Island farmhouse one ripe afternoon in August, firmly resolved to construe so many lines of Virgil.
```

### Step2. Create author characteristics
First, You need install nltk.
```
$ pip install -U nltk
```

Second, You create author datasets. Create author's name folder in ` ./datasets/ ` and author's sentence in author's name folder. e.g. ` ./datasets/s1280124/report.txt `
If you put on some files in author's namefolder, when analysis all files.

Finally, Runnning ` create_characteristics.py `  
The result of characteristics is save to ` ./datasets/characteristics.json `  

### Step3. Authorship analysis
First, You want to analyze sentences are put on ` ./input/ `  

Second, Runnning ` authorship_analysis.py `

### Trouble shooting
If caunse error when you need check files put on correct folder, has not exist not-needed file (.DS_Store etc.).  
```
find . -name ".DS_Store" -delete
```

## Markers for authorship analysis
### Number of all upper words per number of all words (1/10)
` number of upper words / word-count `  
Reason to use:  
I thought it is idiosyncratic language expression.  
> DECEMBER

### Number of proper nouns per number of first char is upper (2/10)
` number of correct spelling / number of proper noun `  
Reason to use:  
The author using correct grammar?  
> London

### adverbials of place vs. adverbials of time (3/10)
` Target of preposition "on" / number of "on" (Unit6.1) `  
Reason to use:  
It was created in class Unit6.1  
> Put them on the table, and bring her in and see her open the bundles.

### perfect aspect/tense vs. and non-perfect aspect/tense  (4/10)
` perfect aspect or non-perfect aspect (Unit6.2) `  
Reason to use:  
It was created in class Unit6.2  
> Methods have changed since your schooldays, Mr. Harrison.

### Number of "," per total number of tokens (5/10)
` number of "," / token `  
Reason to use :  
Because we thought there are differences in frequency of use of comma among  persons. Someone may write a long document with many commas.  
> Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition, seemed to unite some of the best blessings of existence; and had lived nearly twenty-one years in the world with very little to distress or vex her.  

### Number of ";" per total number of tokens (6/10)
` number of ";" / token `  
Reason to use :  
Because we thought there are differences in frequency of use of semicolon among  persons. We can write sentences without semicolons.  
> Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition, seemed to unite some of the best blessings of existence; and had lived nearly twenty-one years in the world with very little to distress or vex her.

### Number of "!" per total number of tokens (7/10)
` number of "!" / token `　　
Reason to use：  
Because we thought that exclamation marks would make differences in frequency of use among persons. Children may use it more. It may be used more in chat-style conversations.
> Ah! poor Miss Taylor! 'Tis a sad business.

### Number of slang per total number of tokens (8/10)
` number of slangs / word-token `
Reason to use :
Because we thought there are differences in frequency of use of slang among  persons. This marker tells you whether the author prefers a casual style of writing.
> A couple of squirrels set on a limb and jabbered at me very friendly. (jabbered)

### Number of types per total number of tokens (9/10)
` types / word-count `
This means the variety of words that are used.
Reason to use：
Because the number of words that people know is different. Smart people may know many words. Children may not know many words.
> If the machinery of the Law could be depended on to fathom every case of suspicion, and to conduct every process of inquiry, with moderate assistance only from the lubricating influences of oil of gold, the events which fill these pages might have claimed their share of the public attention in a Court of Justice. (43/55 = 78.18182%)

### Median number of words that make up one sentence (10/10)
` Sentence length(Median) `
Reason to use：
We expected that the length of a sentence shows a person's writing style. Someone who has good writing skills may be longer. Someone who writes easily might make it shorter.
> All at once Mr. Harrison found his voice. (8-words)
