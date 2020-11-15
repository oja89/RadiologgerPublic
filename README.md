# RadiologgerNLP

Sign up to UMLS...
Get your API key from UMLS profile page ( uts.nlm.nih.gov//uts.html#profile )


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
All folders and output-files are also named there, but we suggest keep the defaults.

6. Run the GUI:
```shell
python gui.py
```
This will let you summarize reports one at the time.
Checked words are cached to prevent need to check words agains (API is slow).
Gives prints in the GUI and also saves summary in ./summaries

-------------------

7. If you need to parse pdf, that can be done with module pdfread.py (but columns break stuff up!):
Put them in ./pdfs folder and run
```shell
python pdfread.py
```
Those are output by the function to ./reports
If they are in .txt format, just put them into ./reports

8. If you want to do whole ./reports folder:
start the main function
```shell
python main.py
```
This takes sentences from your ./reports, and checks each word against UMLS database.
Checked words are cached to prevent need to check words agains (API is slow).

Found words are output as a summary to ./summaries with ending _summary.txt.
