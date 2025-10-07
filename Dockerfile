FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY --link . .

RUN uv sync --locked

EXPOSE 8080

CMD [ "uv", "run", "marimo", "edit", "--host", "0.0.0.0", "-p", "8080" ]
