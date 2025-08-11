# Homework 5: The immune response

We will learn about the basics of gene expression data analysis. Biologists have found a way to measure how much each gene is *expressed* in each cell in an experiment. We do this by counting the number of mRNA molecules in each cell. Remember, DNA holds instructions for building proteins but can't be turned into proteins directly. Translation of DNA creates mRNA molecules which ribosomes read to synthesize proteins.
If we measure the amount of mRNA in a cell, we can tell what proteins the cell is making and, indirectly, what the cell is doing as a whole.

Open `homework-5.ipynb` to get started.

## Submission and Grading
There are three types of exercises/answers within each homework:

1. *Coding exercises* require you to implement an algorithm. We will always include Python stubs for the functions you need to implement in a separate file (most often `helper_functions.py`). Please read the function docstrings for expected parameter and return types. Coding problems will be automatically graded with unit tests.

2. *Image answers* require you to generate an image and save the plot to a corresponding file in `<img>.png`. Please ensure that your images have the exact same name as specified in the instructions and are stored in the root folder of the repository (the same folder as the README.md file).

3. *Variable answers* require you to write down your answers into variables. Please be careful that the variables have the exact same name as in the instructions. We will always provide a stub in the notebook. We don't actually run your entire notebooks, we evaluate only the variable we are grading. This means that your variables should be set explicitly. For instance

    ```python
    x = 5 / 3
    answer_var = x
    ```

    will not work and will receive zero points. All answer variables should be set explicitly e.g. `answer_var = 1.6666` in for this simple example. Please ensure there are no syntax errors in your notebook.


## Environment instructions

You will need Python 3.10 or higher. You will need to install `biopython` for accessing NCBI and `matplotlib` for plotting. You will also need `jupyterlab` to open and run the notebook. You will also need `numpy`, `scipy`, `pandas`, `scanpy`, `statsmodels` and `seaborn`. You can install everything necessary by running
```
pip install biopython matplotlib jupyterlab pandas scanpy statsmodels scipy
```
Please do not use any other libraries, because they will not be installed in the automatic grader environment and will fail, resulting in zero points. If you think some other library absolutely needs to be included, please reach out on Slack and we will discuss it there.

You can start the notebook by running
```
jupyter lab
```
and a browser window should pop open, or you can manually navigate to http://localhost:8888/ in your browser.

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
