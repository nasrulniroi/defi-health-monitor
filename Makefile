.PHONY: setup build test run deploy clean

setup:
	pip install fastapi uvicorn aiohttp numpy scipy pyyaml
	cd src/scanner && go mod tidy
	cd src/web && npm install

build:
	cd src/web && npm run build
	cd src/scanner && go build -o ../../bin/scanner .

test:
	python -m pytest tests/engine/ -v
	python -m pytest tests/integration/ -v
	cd src/scanner && go test -v ./...
	cd src/web && npx vitest run

run-engine:
	cd src/engine && python main.py

run-scanner:
	cd src/scanner && go run main.go serve

run-web:
	cd src/web && npm run dev

deploy:
	bash src/scripts/deploy.sh

clean:
	rm -rf bin/ __pycache__ .pytest_cache
	find . -name "*.pyc" -delete
