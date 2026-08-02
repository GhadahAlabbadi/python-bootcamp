Write-Host "Welcome to the startup project"
mkdir src
mkdir tests
ni src\README.md
ni src\main.py
python -m venv venv 
pip install requests
git init
Write-Host "All complete!!"
