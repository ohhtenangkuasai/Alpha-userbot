# KING USERBOT
FROM biansepang/weebproject:buster

# Dockerfile
# KING
# Dockerfile
RUN git clone -b Alpha-userbot https://github.com/zeeoneofc/Alpha-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/zeeoneofc/Alpha-userbot/Alpha-userbot/requirements.txt

CMD ["python3","-m","userbot"]
