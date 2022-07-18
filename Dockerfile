FROM python:3.10.5-slim-bullseye
EXPOSE  5000
WORKDIR /app
COPY .  /app
RUN pip install -U pip && pip install -r requirements.txt
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:5000/ping || exit 1
CMD ["flask", "run", "--host=0.0.0.0"]
