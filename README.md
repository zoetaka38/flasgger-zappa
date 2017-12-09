# flasgger-zappa

## Prerequisitions

- python

## deploy

```
pyenv virtualenv 3.6.2 flasgger-zappa
source activate flasgger-zappa
pip install -r requirements.txt
pip install zappa awscli
aws configure
zappa deploy dev
```