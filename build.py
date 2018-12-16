import shutil
import os
import subprocess

# npm run build
# copy /dist/index.html & /dist/static to /
os.chdir("blog")
subprocess.Popen("npm run build", shell=True)
os.chdir("..")
shutil.copy("blog/dist/index.html","index.html")
shutil.copytree("blog/dist/static","static")