import envparse

env = envparse.Env()


class Config:
    TOKEN = env.str("TOKEN")