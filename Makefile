.ONESHELL:

init:
	cd api && make init

pre-commit:
	echo "Running pre-commit hooks"
	pre-commit run --all-files
