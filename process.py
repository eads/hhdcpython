import os

HHDC_ROOT = os.path.dirname(os.path.realpath(__file__))
HHDC_DATA_FILE = os.path.join(HHDC_ROOT, 'data/data.csv')
HHDC_OUTPUT_DIRECTORY = os.path.join(HHDC_ROOT, 'output')

def process_data():
    """
    Process data.

    You must modify this function to shape the data the way you need.
    """

    # Make an empty list to hold the processed data.
    output_list = list()

    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()

    # Loop over each line of the data file. Each time the loop runs, the current
    # line is assigned to a variable called `line` which is a string like
    # "x,y,z".
    for line in data:

        # Turn line into a list by "splitting" on the comma.
        processed_line = line.split(',')

        # Add the processed line to the `output_list` variable.
        output_list.append(processed_line)

    # Return the processed data
    return output_list

"""
This cryptic thing calls our process data function when the file is run
from the command line or from PythonAnywhere using the ">>>" icon.
"""
if __name__ == '__main__':
    # Print start message.
    print('Running `process_data()`')

    # Assign return values of `process_data()` function to `output` variable.
    output = process_data()

    # Print the `output` variable.
    print('Value of `output` variable:')
    print(output)

    # Print that we're done.
    print('Done.')