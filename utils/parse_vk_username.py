def parse_vk_username(vk_url: str):
    return vk_url.split("/")[-1]
