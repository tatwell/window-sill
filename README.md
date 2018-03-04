# Window Sill

A project to test building simple Python desktop applications for Ubuntu and Mac.


## Environment
- Python >= `3.6.4`


## Setup
- Install the Tkinter system package. This must be installed before installing Python with pyenv as recommended below. On Ubuntu:

      sudo apt-get install tk-dev

    See this StackOverflow post for more information: https://stackoverflow.com/q/26357567/1093087

- [Install Pyenv](https://wiki.formulafolios.com/view/Best_Practices:Python#Pyenv) and version of Python set in `.python-version`:

      pyenv install 3.6.4

- Clone repository:

      git clone https://github.com/tatwell/window-sill.git

- Install dependencies:

      cd window-sill
      pyenv virtualenv 3.6.4 window-sill
      pyenv local window-sill
      pip install -r requirements.txt


## Usage

To run the app:

    cd window-sill/window-sill
    python app.py

For more usage details:

    python app.py -h


## Testing

To run tests:

    cd window-sill/window-sill
    nosetests -c nose.cfg

Verbosely:

    nosetests -c nose.cfg -v

To run a single test:

    nosetests -c nose.cfg tests/test_example.py
