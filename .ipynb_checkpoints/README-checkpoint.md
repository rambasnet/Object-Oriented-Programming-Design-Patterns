# Object Oriented Programming & Design Patterns

![Test](https://github.com/rambasnet/Python-Object-Oriented-Programming/actions/workflows/ci-test.yml/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rambasnet/Python-Object-Oriented-Programming/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rambasnet/Python-Object-Oriented-Programming)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

- Jupyter notebooks for Object Oriented Programming and Design Patterns using Python

## Text: Python Object Oriented Programming

- Fourth Edition by Steven F. Lott and Dusty Phillips

## How to use the notebooks

### Important

In order to learn coding, it's very important to actually type code on your own from scratch and NOT copy paste! You can run provided cells to see the output, follow along and learn from it. However, it's very important that you either start a new notebook or add cells and write your own code from scratch to practice the concepts covered with many similar examples and solve the exercises provided for self assessment.

### Online services

You can launch an interactive session of this project using online Binder service:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/badge_logo.svg) or Google Colab. Each chapter, where applicable, provides [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com) to simply click and run the notebook in Google's Colab environment.

### On a local system

To run these notebooks interactively and save your work locally, you need [Python 3](https://www.python.org/) and [Jupyter Notebook](http://jupyter.org/) -- an interactive web-based editor that allows you to create and share documents that contain live code and data. [Anaconda or Miniconda](https://www.anaconda.com/products/distribution) is the recommended way to install Python and other packages on all modern platforms.

#### Using Docker

- Install Docker on your system: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

- Dockerfile is provided to build a container image with all the necessary packages and dependencies to run the notebooks. You can build the image and run the container using the provided bash scripts.

- Clone this repo and run the following command from the root of the repo
- Use git-bash Terminal on Windows to run bash scripts

```bash
    git clone https://github.com/rambasnet/Python-Object-Oriented-Programming.git
    curl -o setup.sh https://raw.githubusercontent.com/rambasnet/course-container/main/setup.sh
    bash setup.sh
    bash run.sh # run interactive Debian Shell in the container
    bash run-jupyter.sh # run jupyter notebook server in the container
```

- jupyter notebooks are inside the notebooks folder
- start from the OO-Table-of-Contents.ipynb

#### Installing via Anaconda or Miniconda

Anaconda or Miniconda has Python 3 and many other packages that you can easily install on any platform (Windows, Linux, and Mac). First, install Anaconda: [http://docs.continuum.io/anaconda/install/](http://docs.continuum.io/anaconda/install/) or Miniconda [https://conda.io/docs/user-guide/install/index.html](https://conda.io/docs/user-guide/install/index.html) for Python 3.

After installing anaconda or miniconda, open a terminal or cmd prompt and run the following commands:

```bash
    conda update conda
    conda env list # list current environments
    conda env remove -n <environment_name> # remove existing environment
    conda create -n oop python=3.10 # create a new virtual environment named py
    conda activate oop
    conda install notebook # or
    conda install -c conda-forge retrolab # uses notebook
    conda install mypy # type checker
    python -m pip install hypothesis # test data generator
```

#### Running the notebooks in VS Code

- Python notebooks can be run natively in VS Code. Simply open the notebook file with extension .ipynb in VS Code and run each cell; add new cell, etc. right from VS Code.

#### Running the notebooks using jupyter notebook server

Once Python 3 and Jupyter Notebook are installed, open a terminal change working directory using cd command to go into the folder where this repo is cloned and run the notebook from there. Use notebook or retro.

```bash
    cd <directory where this repo is cloned>
    jupyter notebook # or
    jupyter retro
```

This will start a Jupyter session in your browser. Open any chapter and start coding...
