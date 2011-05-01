from fabric.api import *
from fabric.operations import put
import os
#import fabric.contrib.project as project

PROD = 'vhbit.net'
DEST_PATH = '/var/www/vhbit.net/'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde -s . gen')

def regen():
    clean()
    generate()

def serve():
    local('hyde -w -s . -k serve')

def reserve():
    regen()
    serve()

@hosts(PROD)
def publish():
    regen()
    put(os.path.join(DEPLOY_PATH, 'index.html'), os.path.join(DEST_PATH, 'index.temp.html'), use_sudo=True)
    put(os.path.join(DEPLOY_PATH, 'index.ru.html'), os.path.join(DEST_PATH, 'index.temp.ru.html'), use_sudo=True)    
    put(os.path.join(DEPLOY_PATH, 'media'), DEST_PATH, use_sudo=True)
