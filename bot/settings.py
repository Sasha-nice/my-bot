import envparse

env = envparse.Env()
env.read_envfile()


class Config:
    TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
    VK_API_TOKEN = env.str("VK_API_TOKEN")
    VK_API_VERSION = env.str("VK_API_VERSION")
    VK_API_BASE_URL = env.str("VK_API_BASE_URL")
