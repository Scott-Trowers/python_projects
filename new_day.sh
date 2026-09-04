#!/bin/bash
# creates a new dayN project with uv and a src/main.py layout

# Detect if the script is being sourced in bash or zsh
if [[ -n "$ZSH_VERSION" ]]; then
    if [[ "$ZSH_EVAL_CONTEXT" =~ :file$ ]]; then
        is_sourced=true
    else
        is_sourced=false
    fi
elif [[ -n "$BASH_VERSION" ]]; then
    if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
        is_sourced=true
    else
        is_sourced=false
    fi
else
    is_sourced=false
fi

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "usage: ./new_day.sh <day_number> <title>"
    echo "or to automatically navigate your terminal:"
    echo "  source ./new_day.sh <day_number> <title>"
    if [ "$is_sourced" = true ]; then
        return 1
    else
        exit 1
    fi
fi

DIR="projects/day${1}_${2}"

if [ -d "$DIR" ]; then
    echo "error: $DIR already exists"
    if [ "$is_sourced" = true ]; then
        return 1
    else
        exit 1
    fi
fi

# Run the setup steps checking for errors. We don't use 'set -e'
# so that a sourced terminal session is not terminated on failure.
if ! mkdir -p "$DIR"; then
    echo "error: failed to create directory $DIR"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

if ! cd "$DIR"; then
    echo "error: failed to enter directory $DIR"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

if ! uv init --no-workspace; then
    echo "error: uv init failed"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

# Overwrite the generic README with the standardized template
cat <<EOF > README.md
# day $1 - ${2//_/ }

<brief description>

## how to run

\`\`\`bash
uv run src/main.py
\`\`\`

## skills

- <skills>

## features

- <features>
EOF

if ! mkdir src; then
    echo "error: failed to create src directory"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

if ! mv main.py src/main.py; then
    echo "error: failed to move main.py to src/"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

if ! uv sync; then
    echo "error: uv sync failed"
    if [ "$is_sourced" = true ]; then return 1; else exit 1; fi
fi

echo "Successfully created and initialized $DIR"

if [ "$is_sourced" = false ]; then
    echo ""
    echo "Note: To automatically navigate your terminal into the new directory next time, use:"
    echo "  source ./new_day.sh $1 $2"
    echo ""
    echo "For now, please run: cd $DIR"
fi\
