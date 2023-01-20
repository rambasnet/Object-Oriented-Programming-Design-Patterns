# Python-Object-Oriented-Programming
Class Notes for Object Oriented Programming - Python

## Text: Python Object Oriented Programming
- Fourth Edition by Steven F. Lott and Dusty Phillips

## How to use the notebooks

### Important

In order to learn coding, it's very important to actually type code on your own from scratch and NOT copy paste! You can run provided cells to see the output, follow along and learn from it. However, it's very important that you either start a new notebook or add cells and write your own code from scratch to practice the concepts covered with many similar examples and solve the exercises provided.

### Online services

You can launch an interactive session of this project using online Binder service:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/badge_logo.svg) or Google Colab. Each chapter, where applicable, provides [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com) to simply click and run the notebook in Google's Colab environment.

### On a local system

To run these notebooks interactively and save your work locally, you need [Python 3][https://www.python.org/] and [Jupyter Notebook](http://jupyter.org/) -- an interactive web-based editor that allows you to create and share documents that contain live code and data. [Anaconda or Miniconda](https://www.anaconda.com/products/distribution) is the recommended way to install Python and other packages on all modern platforms.

#### Installing via Anaconda or Miniconda

Anaconda or Miniconda has Python 3 and many other packages that you can easily install on any platform (Windows, Linux, and Mac). First, install Anaconda: [http://docs.continuum.io/anaconda/install/](http://docs.continuum.io/anaconda/install/) or Miniconda [https://conda.io/docs/user-guide/install/index.html](https://conda.io/docs/user-guide/install/index.html) for Python 3.

After installing anaconda or miniconda, open a terminal or cmd prompt and run the following commands:

```bash
    conda update conda
    conda env list # list current environments
    conda env remove -n <environment_name> # remove existing environment
    conda create -n py python=3.10 # create a new virtual environment named py
    conda install notebook # or
    conda install -c conda-forge retrolab # uses notebook
    conda install mypy
    python -m pip install hypothesis
```

### Manually create evn and install packages

```bash
    conda create -n ml python=3.10 # create new ml environment
    conda env list # list all the avialable virtual environments
    conda activate ml #activate ml environment
    conda install <SomePackage> #install packages
    conda deactivate # exit out the current environment
```

#### Running the notebooks in VS Code

- Python notebooks can be run natively in VS Code. Simply open the notebook file with extension ipynb in VS Code and run each cell; add new cell, etc. right from VS Code.

#### Running the notebooks using jupyter notebook server

Once Python 3 and Jupyter Notebook are installed, open a terminal change working directory using cd command to go into the folder where this repo is cloned and run the notebook from there:

```bash
    cd <directory where this repo is cloned>
    jupyter notebook # or
    jupyter retro
```

This will start a Jupyter session in your browser. Open any chapter and start coding...

## Contributing

Contributions are accepted via pull requests. You can also open issues on bugs, typos or any corrections and suggest improvements on the notebooks.
- 