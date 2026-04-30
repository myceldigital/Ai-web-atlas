.PHONY: validate render

validate:
	python3 scripts/validate-data.py

render:
	bash scripts/render-maps.sh
