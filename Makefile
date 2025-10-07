%: %.py
	uv run marimo export html-wasm $< -o public/$@.html --show-code
