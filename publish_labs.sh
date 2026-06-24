#!/bin/bash
set -e

# Loop over all report directories
for d in LAB*/report; do
  if [ -d "$d" ]; then
    echo "Processing $d"
    # Create .gitignore to ignore everything except directories, pdf files, and itself
    printf "*\n!*/\n!*.pdf\n!.gitignore\n" > "$d/.gitignore"
    
    # Untrack everything in the report directory
    git rm -r --cached "$d" || true
  fi
done

# Add everything, which will respect the new .gitignore files
git add .

# Commit changes
git commit -m "Add .gitignore in reports to only track pdfs, and add all labs"

# Push to origin
git push origin HEAD
