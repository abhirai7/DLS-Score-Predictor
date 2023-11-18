# DLS Score Predictor with Machine Learning

This project is a DLS (Duckworth Lewis Stern) Score Predictor which uses the the original DLS method/algorithm to predict the DLS score for given set of inputs and displays the predicted score on the python gui.

The Duckworth–Lewis method (often written as D/L method) is a mathematical formulation designed to calculate the target score for the team batting second in a limited-overs cricket match interrupted by weather or other circumstances.

## Project Structure

The project consists of the following files and directories:

- `_main.py_`: The file contains the regression model which predicts the DLS score.
    
- `dls_resources.csv`: This is the dataset on which the regression model is trained. this consists on percentage of remaining reesources for the remaining overs and wickets fallen. 
- `tkinter_.py`: This contains the tkinter gui program that takes the required inputs.
- `_run.py`: This contains the output gui class.this file extracts the data from all the above files and outputs the main result on tkinter gui

Note: This Program works only for One-day/50-over format game.


## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python _run.py
```

1. Fill in all the parameters in the gui dialog box and submit.
2. Close the dialog box

3. The application will provide an another gui dialog box displaying the prediction of DLS score. 



## Dependencies

The project relies on the following Python libraries:

- `tkinter`:The standard Python interface to the Tk gui toolkit.
- `pandas`: For data manipulation.
- `scikit-learn`: For machine learning model training and prediction.
You can install these dependencies using the requirements.txt file.

## Contributing

Feel free to contribute to this project by opening issues, suggesting improvements, or creating pull requests.
