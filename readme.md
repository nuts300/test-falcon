# Test falcon

## tutorial

  http://falcon.readthedocs.io/en/stable/user/tutorial.html

## Api document

  http://falcon.readthedocs.io/en/stable/api/index.html

## Environment

### Install pyenv pyenv-virtualenv

```
  brew install pyenv pyenv-virtualenv
  echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bash_profile
  echo 'export PATH="${PYENV_ROOT}/bin:$PATH"' >> ~/.bash_profile
  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
  source ~/.bash_profile
```

### Making python env

```
  pyenv install 3.6.3
  pyenv virtualenv 3.6.3 {{env_name}}
  
  cd {{project_dir}}
  pyenv local {{env_name}}
```

## Install dependencies

### Install dependencies

  pip install -r requirements.txt -c constraints.txt

## Start server

```
  gunicorn --reload look.app
  gunicorn 'look.app:get_app()'
  gunicorn --reload 'look.app:get_app()'

  gunicorn --reload 'thing.app:get_app()'
  
  gunicorn --reload 'sample.app:get_app()'
```

## Testing

```
  pytest tests
  pytest tests -k test_saving_image
  pytest tests -k test_posted_image_gets_saved
```

### Testing with Using http

#### look

```
  http localhost:8000/images/voltron.png
  http localhost:8000/images/db79e518-c8d3-4a87-93fe-38b620f9d410.png
  http POST localhost:8000/images Content-Type:image/png < test.png
```

#### thing

```
  http localhost:8000/1/things authorization:custom-token
```

### sample

```
  python -m unittest sample_tests/*.py
```