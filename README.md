# PDF Table Extractor

This project is usefull for those who need use PDF files with tables and always need to manually copy the entire table from the PDF file. In addition to the code we have a website with this application using a friendly interface!

Acess the application in: https://pdftableextractor.herokuapp.com/

This aplication needs java on background, make sure he's in your machine!


### How to run localy
```
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

streamlit run interface.py
```

### How to run with docker
```
docker-compose build .
docker-compose up -d

```
