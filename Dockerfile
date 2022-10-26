FROM python:3
RUN git clone https://github.com/MatiasBoldrini/Cafetera.git
WORKDIR /Cafetera
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]
