from environs import Env

env = Env()
env.read_env()

# general
# --------------------------------------------------------------------------
OPENAI_API_KEY = env.str("OPENAI_API_KEY", None)
