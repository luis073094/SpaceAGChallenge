FROM python

RUN pip install --upgrade pip

COPY ./SpaceAGChallenge/SpaceAGChallenge /app/SpaceAGChallenge
COPY ./SpaceAGChallenge/requirements.txt /app
COPY ./SpaceAGChallenge/entrypoint.sh /app/SpaceAGChallenge

WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/SpaceAGChallenge
ENTRYPOINT [ "sh", "entrypoint.sh" ]