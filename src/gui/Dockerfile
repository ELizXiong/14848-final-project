FROM python:latest
WORKDIR /usr/src/gui
COPY . /usr/src/gui
RUN pip install tk
ENV DISPLAY :0
CMD ["User_Interface_GUI.py"]
ENTRYPOINT ["python"]