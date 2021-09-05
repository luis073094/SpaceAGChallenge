FROM python

RUN pip install --upgrade pip

COPY ./SpaceAGChallenge/SpaceAGChallenge /app/SpaceAGChallenge
COPY ./SpaceAGChallenge/requirements.txt /app
COPY ./SpaceAGChallenge/entrypoint.sh /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh", "entrypoint.sh" ]