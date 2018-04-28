#!/bin/sh
# Execute this script on project root folder as: source setpythonpath.sh

# Include in PYTHONPATH
PYTHONPATH=${PYTHONPATH}:$(pwd)

export PYTHONPATH

# Echo the result
echo "PYTHONPATH: ${PYTHONPATH}"

