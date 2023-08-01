FROM python:3.11-alpine

RUN pip install -r requirements.txt

CMD streamlit run app.py