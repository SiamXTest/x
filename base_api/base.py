class BaseCore:
    def __init__(self, config=None):
        pass

    def initialize_session(self, headers=None):
        pass

    def fetch(self, url):
        import httpx
        r = httpx.get(url)
        return r.text

    def get_segments(self, quality, m3u8_url_master):
        return []

    def download(self, video, quality, path, callback, downloader, remux, callback_remux):
        pass

    def legacy_download(self, path, callback, url):
        pass

    def str_to_bool(self, value: str) -> bool:
        return value.lower() in ('true', '1', 'yes')

def setup_logger(name, log_file=None, level=None, http_ip=None, http_port=None):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
