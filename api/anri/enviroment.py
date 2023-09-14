import os
import warnings

import environ


env = environ.Env()

current_path = environ.Path(__file__) - 1
site_root = current_path - 1
env_file = site_root(".env")


# If exists file local.env we load dev.env and this file.
# This is necessary so that the new variables for the local environment are automatically applied
local_env_file = site_root("local.env")
dev_env_file = site_root("dev.env")
if os.path.exists(local_env_file):
    # Creating fake classes so as not to overwrite os.environ
    # and be able to get the loaded variables from different files.
    class DevEnv(environ.Env):
        ENVIRON = {}

    class LocalEnv(environ.Env):
        ENVIRON = {}

    dev_env = DevEnv()
    dev_env.read_env(env_file=dev_env_file)

    local_env = LocalEnv()
    local_env.read_env(env_file=local_env_file)

    SAME_SETTINGS = {}
    for env_name, env_value in local_env.ENVIRON.items():
        if env_name in dev_env.ENVIRON and dev_env.ENVIRON[env_name] == env_value:
            SAME_SETTINGS[env_name] = env_value

    if SAME_SETTINGS:
        warning_massage = (
            "You can delete these settings (in local.env) "
            "since the same settings are specified in the dev.env file:\n"
        )
        for env_name, env_value in SAME_SETTINGS.items():
            warning_massage += f"{env_name}={env_value}\n"

        warnings.warn(warning_massage)

    # The first should be the configuration file of which are a priority
    # because django-environ use the setdefault (for os.environ)
    # for set it and the re-setting of the value will be ignored
    environ.Env.read_env(env_file=local_env_file)
    environ.Env.read_env(env_file=dev_env_file)
else:
    environ.Env.read_env(env_file=env_file)
