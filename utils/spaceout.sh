# !/bin/bash

# Loop through all filenames
for file in *; do
  # Check if it's a regular file (avoid directories and hidden files)
  if [[ -f "$file" ]]; then
    # New name with underscores replacing spaces
    new_name=${file// /_}

    # Print a message (optional)
    echo "Renaming '$file' to '$new_name'"

    # Rename the file using mv command
    mv "$file" "$new_name"
  fi
done

echo "Renaming completed!"
