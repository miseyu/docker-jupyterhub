# jupyterhub_config.py
c = get_config()

c.JupyterHub.log_file = '/var/log/jupyterhub.log'

# create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True

# specify users and admin
c.Authenticator.admin_users = {'admin'}

