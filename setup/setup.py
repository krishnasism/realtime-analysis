import os
cwd= os.getcwd()
print("Installing.....")
print("Please disable antivirus shield if Access is denied")
os.system('pip install -r requirements.txt')
os.system('pip install '+cwd+'/libs/tweet-preprocessor-0.4.0.zip')
os.system('pip install -U numpy')
print("Successfully installed...")

