#!/bin/bash
git add .
echo "Enter commit message:"
read commitm
git commit -m "$commitm"
git push
