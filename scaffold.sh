#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

# =============================================================================
# WORKTREE SCAFFOLD HOOK FOR ANOTACIONES (PELICAN BLOG)
#
# This script is executed automatically by 'gw create' or 'gw review'.
# It sets up a new worktree to be ready for development.
#
# Arguments from gw.sh:
#   $1: The worktree's name (e.g., "feature-x").
#   $2: The absolute path to the worktree's root directory.
# =============================================================================


# =============================================================================
# --- FUNCTIONS ---
# =============================================================================

# Task 1: Initialize git submodules (Flex theme and plugins)
init_submodules() {
    local worktree_path="$1"

    echo "[+] Task 1: Initializing git submodules (Flex theme and plugins)..."

    cd "$worktree_path"

    if [ -f ".gitmodules" ]; then
        echo "   -> Found .gitmodules, initializing submodules..."
        git submodule update --init --recursive
        echo "   -> Submodules initialized successfully."
    else
        echo "   -> No .gitmodules found. Skipping submodule initialization."
    fi
}

# Task 2: Clone pelican-plugins if not present (legacy setup)
clone_pelican_plugins() {
    local worktree_path="$1"

    echo "[+] Task 2: Checking pelican-plugins..."

    cd "$worktree_path"

    if [ -d "plugins" ]; then
        echo "   -> Plugins directory already exists."
    else
        echo "   -> Cloning pelican-plugins repository..."
        git clone https://github.com/getpelican/pelican-plugins.git plugins
        echo "   -> Plugins cloned successfully."
    fi
}

# Task 3: Sync uv dependencies
copy_untracked_files() {
    local worktree_path="$1"

    echo "[+] Task 3: Copying untracked configuration files..."

    local repo_root
    repo_root=$(git -C "$worktree_path" rev-parse --show-toplevel)
    if [ -z "$repo_root" ]; then
        echo "   -> Error: Could not determine git repository root. Skipping file copy." >&2
        return
    fi

    local files_to_copy
    files_to_copy=($(git -C "$repo_root" config --get-all worktree.untrackedfiles 2>/dev/null || true))
    if [ ${#files_to_copy[@]} -eq 0 ]; then
        echo "   -> No custom files configured in 'worktree.untrackedfiles'. Using defaults."
        files_to_copy=( ".env" ".envrc" ".env.local" ".tool-versions" "mise.toml" ".python-version"
        )
    else
        echo "   -> Using custom files from 'worktree.untrackedfiles' git config."
    fi

    # Change to repo root to correctly check for untracked files.
    pushd "$repo_root" > /dev/null

    local copied_count=0
    for file in "${files_to_copy[@]}"; do
        # Check if the file/dir exists and is untracked by git.
        # Use git ls-files --others --exclude-standard to check if it's untracked.
        if [ -e "$file" ] && [ -n "$(git ls-files --others --exclude-standard "$file")" ]; then
            local dest_path="$worktree_path/$file"

            # Ensure parent directory of the destination exists.
            mkdir -p "$(dirname "$dest_path")"

            if [ -d "$file" ]; then
                echo "   -> Copying untracked directory: '$file' to '$worktree_path/$file'..."
                cp -rT "$file" "$dest_path"
            else
                echo "   -> Copying untracked file: '$file' to '$worktree_path/$file'..."
                cp "$file" "$dest_path"
            fi
            ((copied_count++))
        fi
    done

    popd > /dev/null # Return to original directory

    if [ "$copied_count" -eq 0 ]; then
        echo "   -> No relevant untracked files found to copy."
    else
        echo "   -> Finished copying $copied_count untracked item(s)."
    fi
}

# Task 4: Sync uv dependencies
sync_uv_deps() {
    local worktree_path="$1"

    echo "[+] Task 4: Syncing uv dependencies..."

    cd "$worktree_path"

    if ! command -v uv &> /dev/null; then
        echo "   -> Warning: 'uv' command not found. Cannot sync dependencies." >&2
        echo "   -> Please install uv: https://docs.astral.sh/uv/"
        return
    fi

    if [ -f "pyproject.toml" ] || [ -f "uv.lock" ]; then
        echo "   -> Running 'uv sync'..."
        uv sync
        echo "   -> Dependencies synced successfully."
    else
        echo "   -> No pyproject.toml or uv.lock found. Skipping uv sync."
    fi
}


# =============================================================================
# --- MAIN FUNCTION ---
# =============================================================================

main() {
    local worktree_name="$1"
    local worktree_path="$2"

    echo "--- Running scaffold for worktree: '$worktree_name' ---"
    echo "Worktree path: $worktree_path"
    echo

    if [ -z "$worktree_path" ] || [ ! -d "$worktree_path" ]; then
        echo "Error: Worktree path '$worktree_path' is not a valid directory." >&2
        exit 1
    fi

    init_submodules "$worktree_path"
    echo
    clone_pelican_plugins "$worktree_path"
    echo
    copy_untracked_files "$worktree_path"
    echo
    sync_uv_deps "$worktree_path"

    echo
    echo "--- ✅ Scaffold for '$worktree_name' finished successfully. ---"
}


# =============================================================================
# --- EXECUTION ---
# =============================================================================

main "$@"
