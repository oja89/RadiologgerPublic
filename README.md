# RadiologgerNLP

Sign up to UMLS...
Download the UMLS database.


### Set up

### Installing dependencies

0. (Install virtualenv)
(virtualenv is not in requirements)
(in case with problems on Windows, try first installing with)
```shell
python -m pip install virtualenv --user
```

1. Activate python virtual environment in command line
```shell
virtualenv nlp
```

2. Activate virtual environment
```shell
nlp/Scripts/activate.bat
```
3. install dependencies
```shell
pip install -r requirements.txt
```

4. When running first time, we need to download nltk databases used:
```shell
python conf/downloadnltk.py
```
5. Put your API key to UMLS in conf/Config.py.
All folders and output-files are also named there, but keep the defaults.

6. We need reports to parse, these can be in pdf too (but columns break stuff up!):
If pdfs: Put them in ./pdfs folder and run
```shell
python pdfread.py
```
Those are output by the function to ./reports
If they are in .txt format, just put them into ./reports

7. start the main function
```shell
python main.py
```
This takes sentences from your reports, and checks each word against UMLS database.
Checked words are cached to prevent need to check words agains (API is slow).

Found words are output as a summary to ./logs with ending _summary.txt.
