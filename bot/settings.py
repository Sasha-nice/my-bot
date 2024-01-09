import envparse

env = envparse.Env()
env.read_envfile()


class Config:
    TOKEN = env.str("TOKEN")
