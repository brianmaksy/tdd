import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run
# import paramiko, os
# paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG) 
# env.use_ssh_config = True
# env.key_filename = '/Users/bmak/.ssh/id_rsa_do.pub'


REPO_URL = 'https://github.com/brianmaksy/tdd.git'  
HOST = 'noslackmak.com'

def deploy():
    site_folder = f'/home/{env.user}/sites/{HOST}'  
    run(f'mkdir -p {site_folder}')  
    with cd(site_folder):  
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    '''The equivalent of the git pull we used when we did it manually, but with the reset --hard to force overwriting any local changes.'''
    if exists('.git'):  
        run('git fetch')  
    else:
        run(f'git clone {REPO_URL} .')  
    current_commit = local("git log -n 1 --format=%H", capture=True)  
    run(f'git reset --hard {current_commit}')  

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):  
        run(f'python3 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')  

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')  
    append('.env', f'SITENAME={HOST}')
    current_contents = run('cat .env')  
    if 'DJANGO_SECRET_KEY' not in current_contents:  
        new_secret = ''.join(random.SystemRandom().choices(  
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')  

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')  