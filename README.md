## Setup Environment

- [install uv](https://docs.astral.sh/uv/getting-started/installation/)

- [install marimo](https://docs.astral.sh/uv/guides/integration/marimo/)

## Edit in Docker

```sh
docker run -p 8080:8080 -it ghcr.io/tbytes404/pymath
open http://localhost:8080
```
  
## Export Wasm

```sh
make index calculator
python -m http.server -d public
open http://localhost:8000
```
