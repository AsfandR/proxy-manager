def get_proxy_path():
    import os
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'proxies.txt')
    return filepath

def test_load_proxies():
    