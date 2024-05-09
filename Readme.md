## Intro:


## Deploy


# 1 - on windows server

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install --yes python3

python3.exe -m venv venv3
.\venv3\Script\activate

pip install Flask
```