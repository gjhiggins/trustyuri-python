#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../src && pwd )"
export PYTHONPATH=$PYTHONPATH:$DIR
python $DIR/hashuri/CheckFile.py $*
