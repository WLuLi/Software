# TODO: add autopep8 here.
autopep8 -i -r .

# TODO: add autoflake here.
autoflake -i -r --exclude=.git,__pycache__,venv .

# TODO: add isort here.
isort --skip=.git,__pycache__,venv .

# TODO: add flake8 here.
flake8 .