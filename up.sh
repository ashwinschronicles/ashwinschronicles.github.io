#!/bin/bash
set -e

read -p "Commit description: " desc
if [ -z "$desc" ]; then
    echo "Aborted: Commit description cannot be empty."
    exit 1
fi

git add -A
git commit -m "$desc"
git push origin HEAD

