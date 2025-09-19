# RepoCloner App

A Windows desktop application that simplifies the process of cloning Git repositories with a clean, user-friendly interface. The app allows you to clone any Git repository, remove its version control history, and create convenient shortcuts for easy access.

## Features

### 🎯 **Easy Repository Cloning**
- Clone any Git repository from popular platforms (GitHub, GitLab, Bitbucket)
- Support for both HTTPS and SSH URLs
- Automatic URL validation to ensure proper Git repository format

### 📁 **Flexible Directory Selection**
- Interactive directory picker dialog
- Choose any location on your system to clone the repository
- No need to navigate to specific folders via command line

### 🏷️ **Custom Repository Naming**
- Provide your own custom name for the cloned repository
- Automatic sanitization of invalid filename characters
- No more dealing with complex repository names from URLs

### 🧹 **Clean Repository Output**
- Automatically removes the `.git` folder after cloning
- Creates a clean copy without version control history
- Perfect for creating project templates or clean codebases

### 🔗 **Automatic Shortcut Creation**
- Creates desktop shortcuts in `C:\Development\Apps`
- Shortcuts are named after your custom repository name
- Direct access to your cloned projects

### 🖥️ **User-Friendly Interface**
- Modern GUI dialogs instead of command-line prompts
- Clear error messages and success notifications
- Graceful handling of user cancellations and errors

## How to Use

1. **Run the Application**
   - Double-click `RepoCloner.exe` to launch the application

2. **Select Destination Directory**
   - A directory picker dialog will appear
   - Choose where you want the repository to be cloned
   - Click "Select Folder" to confirm

3. **Enter Repository URL**
   - Input the Git repository URL (HTTPS or SSH)
   - The app will validate the URL format automatically
   - Click "OK" to proceed

4. **Provide Custom Name**
   - Enter a custom name for your cloned repository
   - Invalid characters will be automatically replaced
   - Click "OK" to continue

5. **Automatic Processing**
   - The app will clone the repository
   - Remove the `.git` folder
   - Create a shortcut in `C:\Development\Apps`
   - Display a success message when complete

## Supported Repository URLs

The application supports all standard Git repository formats:

- **GitHub**: `https://github.com/username/repository` or `git@github.com:username/repository.git`
- **GitLab**: `https://gitlab.com/username/repository` or `git@gitlab.com:username/repository.git`
- **Bitbucket**: `https://bitbucket.org/username/repository` or `git@bitbucket.org:username/repository.git`
- **Custom Git Servers**: Any standard Git URL format

## Requirements

- **Windows 10/11** (64-bit)
- **Git** installed and available in system PATH
- **Python 3.7+** (for development/build)

## Installation

1. Download the `RepoCloner.exe` file
2. Place it in your desired location
3. Ensure Git is installed on your system
4. Run the executable

## Development

### Building from Source

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build Executable**
   ```bash
   pyinstaller RepoCloner.spec
   ```

### Dependencies

- **Core**: Python standard library modules
- **GUI**: tkinter (included with Python)
- **Shortcut Creation**: pywin32, winshell
- **Build Tool**: PyInstaller

## Use Cases

### 🎨 **Design Templates**
- Clone design system repositories
- Remove version history for clean templates
- Create shortcuts for quick access

### 📚 **Learning Projects**
- Clone tutorial repositories
- Create clean copies for practice
- Organize learning materials with custom names

### 🏗️ **Project Templates**
- Clone boilerplate projects
- Remove Git history for clean templates
- Create project starters with custom naming

### 🔄 **Code Migration**
- Clone repositories for migration projects
- Create clean copies without version history
- Organize migrated code with descriptive names

## Error Handling

The application includes comprehensive error handling:

- **Git Not Installed**: Clear error message with installation instructions
- **Invalid URLs**: Validation with helpful examples
- **Directory Access Issues**: Graceful handling of permission problems
- **Network Issues**: Clear error messages for connection problems
- **File Conflicts**: Option to overwrite existing directories

## Technical Details

- **Language**: Python 3.7+
- **GUI Framework**: tkinter
- **Git Integration**: subprocess calls to Git CLI
- **File Operations**: pathlib and shutil for file management
- **Windows Integration**: pywin32 for shortcut creation
- **Build System**: PyInstaller for executable creation

## File Structure

```
RepoCloner/
├── repo_cloner.py          # Main application code
├── requirements.txt        # Python dependencies
├── RepoCloner.spec        # PyInstaller configuration
├── build_exe.bat          # Windows build script
├── build_exe.sh           # Linux build script
├── dist/
│   └── RepoCloner.exe     # Built executable
└── README.md              # This documentation
```

## Troubleshooting

### Common Issues

1. **"Git is not installed" Error**
   - Install Git from https://git-scm.com/
   - Ensure Git is added to your system PATH

2. **Shortcut Creation Fails**
   - Ensure you have write permissions to `C:\Development\Apps`
   - The directory will be created automatically if it doesn't exist

3. **Repository Clone Fails**
   - Check your internet connection
   - Verify the repository URL is correct
   - Ensure you have access to the repository

4. **Permission Denied Errors**
   - Run the application as administrator if needed
   - Check that the target directory is writable

## License

This project is developed for internal use at CECO Environmental Corp.

## Support

For technical support or feature requests, please contact the development team.

---

**Version**: 2.0  
**Last Updated**: December 2024  
**Compatibility**: Windows 10/11 (64-bit)# RepoCloner
