import os
from libs.configobj import ConfigObj

config_file = os.path.join(os.getenv('HOME'), ".Slx7hS3ns3onLinux.cfg")
config = ConfigObj(config_file)


print config['PARSER']['timestamp']['enable']
