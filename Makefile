start:
	poetry shell
	poetry install
	poetry build
	python3 -m pip install --user dist/altlinux_branch_diff-0.1.0-py3-none-any.whl