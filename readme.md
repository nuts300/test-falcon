# Test falcon

## tutorial

  http://falcon.readthedocs.io/en/stable/user/tutorial.html

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

### Make dependencies.txt

  pip-compile requirements/dependencies.in

### Install dependencies

  pip-sync requirements/*.txt

## Start server

```
  gunicorn --reload look.app
  gunicorn 'look.app:get_app()'
```

## Testing

```
  pytest tests
  pytest tests -k test_saving_image
  pytest tests -k test_posted_image_gets_saved
```
