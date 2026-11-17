#!/bin/bash

if [ ! -f grades.csv ]; then
    echo "Error: grades.csv was not found."
    exit 1
fi

if [ ! -d archive ]; then
    mkdir archive
fi

timestamp=$(date +%Y%m%d-%H%M%S)
new_name="grades_$timestamp.csv"

if [ -e "archive/$new_name" ]; then
    echo "Error: archive/$new_name already exists. Wait a second and try again."
    exit 1
fi

if ! mv grades.csv "archive/$new_name"; then
    echo "Error: could not move grades.csv."
    exit 1
fi
touch grades.csv

echo "$timestamp: grades.csv -> archive/$new_name" >> organizer.log
echo "Archived grades.csv as archive/$new_name"
