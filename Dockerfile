
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/ ./app/

RUN useradd --system --no-create-home appuser

USER appuser

EXPOSE 8000

CMD ["python", "-m", "app.main"]
