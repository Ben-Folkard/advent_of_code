#!/bin/bash

TIMEFORMAT='Successfully ran in %R s'
#chmod +x run_fortran.sh (Need to run in terminal before you can run the bash file)

# Clears the Commandline for a cleaner output from the code
clear

# Check if at least one argument is provided (source file)
if [ $# -lt 1 ]; then
    echo "Usage: $0 <source_file> [optional_libraries]"
    exit 1
fi

# Set variables for readability
source_file=$1
output_name="${source_file%.f90}"  # Removes the .f90 extension for the output name
optional_libraries=$2

# Compile the Fortran code with optional libraries
if [ -z "$optional_libraries" ]; then
    # Compile without additional libraries
    gfortran -o "$output_name" -g -Wall -O0 -fcheck=all -fmax-errors=1 -std=f2008 "$source_file"
else
    # Compile with additional libraries
    gfortran -o "$output_name" -g -Wall -O0 -fcheck=all -fmax-errors=1 -std=f2008 "$source_file" $optional_libraries
fi

# Run the compiled Fortran program
time {
    echo "Running $1..."
    ./"$output_name"
}
