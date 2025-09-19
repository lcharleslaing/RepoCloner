#!/usr/bin/env python3
"""
Repository Cloner Script

This script prompts the user for a repository URL, clones it to the current directory,
and removes the .git folder to create a clean copy without version control history.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import re
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


def select_directory():
    """Open a directory picker dialog to select where to clone the repository."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    directory = filedialog.askdirectory(
        title="Select directory where the repository will be cloned"
    )
    
    root.destroy()
    return directory


def get_custom_repo_name():
    """Prompt user for a custom repository name."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    repo_name = simpledialog.askstring(
        "Repository Name",
        "Enter the name for the cloned repository:",
        initialvalue=""
    )
    
    root.destroy()
    return repo_name


def get_repo_url():
    """Prompt user for repository URL and validate it."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    while True:
        url = simpledialog.askstring(
            "Repository URL",
            "Enter the repository URL:",
            initialvalue=""
        )
        
        if not url:
            messagebox.showerror("Error", "Please enter a valid repository URL.")
            continue
            
        # Basic validation for common git URL patterns
        git_patterns = [
            r'^https://github\.com/[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^https://gitlab\.com/[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^https://bitbucket\.org/[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^git@github\.com:[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^git@gitlab\.com:[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^git@bitbucket\.org:[\w\-\.]+/[\w\-\.]+(?:\.git)?$',
            r'^https://.*\.git$',
            r'^git@.*:.*\.git$'
        ]
        
        if any(re.match(pattern, url) for pattern in git_patterns):
            root.destroy()
            return url
        else:
            messagebox.showerror(
                "Invalid URL",
                "Invalid repository URL format. Please enter a valid Git repository URL.\n\nExamples:\n  https://github.com/username/repository\n  https://github.com/username/repository.git\n  git@github.com:username/repository.git"
            )
    
    root.destroy()
    return None


def get_repo_name(url):
    """Extract repository name from URL."""
    # Remove .git suffix if present
    url = url.rstrip('.git')
    
    # Extract name from URL
    if '/' in url:
        return url.split('/')[-1]
    elif ':' in url:
        return url.split(':')[-1]
    else:
        return "cloned_repo"


def check_git_installed():
    """Check if git is installed on the system."""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def clone_repository(url, target_dir):
    """Clone the repository to the target directory."""
    try:
        print(f"Cloning repository from {url}...")
        result = subprocess.run(
            ['git', 'clone', url, target_dir],
            capture_output=True,
            text=True,
            check=True
        )
        print("Repository cloned successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Git is not installed or not found in PATH.")
        return False


def remove_git_folder(repo_path):
    """Remove the .git folder from the cloned repository."""
    git_path = Path(repo_path) / '.git'
    
    if git_path.exists():
        try:
            print("Removing .git folder...")
            shutil.rmtree(git_path)
            print(".git folder removed successfully!")
            return True
        except Exception as e:
            print(f"Error removing .git folder: {e}")
            return False
    else:
        print("No .git folder found to remove.")
        return True


def create_shortcut(repo_name, target_path):
    """Create a shortcut to the cloned repository in C:\\Development\\Apps."""
    try:
        import winshell
        from win32com.client import Dispatch
        
        # Create the target directory if it doesn't exist
        shortcut_dir = Path("C:/Development/Apps")
        shortcut_dir.mkdir(parents=True, exist_ok=True)
        
        # Create shortcut path
        shortcut_path = shortcut_dir / f"{repo_name}.lnk"
        
        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.Targetpath = str(target_path)
        shortcut.WorkingDirectory = str(target_path)
        shortcut.Description = f"Shortcut to {repo_name} repository"
        shortcut.save()
        
        print(f"Shortcut created: {shortcut_path}")
        return True
        
    except ImportError:
        print("Warning: Required modules for shortcut creation not available.")
        print("Install pywin32 and winshell to enable shortcut creation:")
        print("pip install pywin32 winshell")
        return False
    except Exception as e:
        print(f"Error creating shortcut: {e}")
        return False


def main():
    """Main function to orchestrate the cloning process."""
    print("=" * 50)
    print("Repository Cloner")
    print("This script will clone a repository and remove the .git folder")
    print("=" * 50)
    
    # Check if git is installed
    if not check_git_installed():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "Git is not installed or not found in PATH.\nPlease install Git and try again.")
        root.destroy()
        sys.exit(1)
    
    # Get target directory from user
    target_dir = select_directory()
    if not target_dir:
        print("No directory selected. Operation cancelled.")
        sys.exit(0)
    
    # Get repository URL from user
    repo_url = get_repo_url()
    if not repo_url:
        print("No repository URL provided. Operation cancelled.")
        sys.exit(0)
    
    # Get custom repository name from user
    custom_name = get_custom_repo_name()
    if not custom_name:
        print("No repository name provided. Operation cancelled.")
        sys.exit(0)
    
    # Clean the repository name (remove invalid characters)
    repo_name = re.sub(r'[<>:"/\\|?*]', '_', custom_name.strip())
    
    # Create target path
    target_path = Path(target_dir) / repo_name
    
    # Check if directory already exists
    if target_path.exists():
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askyesno(
            "Directory Exists",
            f"Directory '{repo_name}' already exists in the selected location.\nDo you want to remove it and continue?"
        )
        root.destroy()
        
        if response:
            try:
                shutil.rmtree(target_path)
                print(f"Removed existing directory '{repo_name}'")
            except Exception as e:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror("Error", f"Error removing existing directory: {e}")
                root.destroy()
                sys.exit(1)
        else:
            print("Operation cancelled.")
            sys.exit(0)
    
    # Clone the repository
    if not clone_repository(repo_url, str(target_path)):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "Failed to clone repository. Check the console for details.")
        root.destroy()
        sys.exit(1)
    
    # Remove .git folder
    if not remove_git_folder(target_path):
        print("Warning: Repository was cloned but .git folder could not be removed.")
    
    # Create shortcut
    create_shortcut(repo_name, target_path)
    
    print("\n" + "=" * 50)
    print("Operation completed successfully!")
    print(f"Repository cloned to: {target_path}")
    print("The .git folder has been removed.")
    print("=" * 50)
    
    # Show success message
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
        "Success",
        f"Repository '{repo_name}' has been cloned successfully!\n\nLocation: {target_path}\n\nShortcut created in C:\\Development\\Apps"
    )
    root.destroy()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
