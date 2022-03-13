from urllib.parse import urlunparse
from bs4 import BeautifulSoup
from page_loader.path_resolve import get_page_name, get_path, get_resource_dir_name, get_res_full_path
from page_loader.save import save, mkdir
from page_loader.download import load
from page_loader.res import get_images, get_res_path, update_link
import os
from urllib.parse import urlparse, urlunsplit

def download(url, path=''):
    download_path = get_path(path)

    html_dom = BeautifulSoup(load(url), 'html.parser')

    parse = urlparse(url)
    scheme = parse.scheme
    netloc = parse.netloc

    images = get_images(html_dom)
    print(images)
    if images:
        res_path = get_resource_dir_name(url)
        mkdir(os.path.join(download_path, res_path))

        to_download = []

        for image in images:
            online_path = get_res_path(image)
            local_path = os.path.join(res_path, get_res_full_path(online_path))
            update_link(image, local_path)
            to_download.append(online_path)
        
        for res_url in to_download:
            download_url = urlunsplit([scheme, netloc, res_url, None, None])
            save(load(download_url), os.path.join(download_path, res_path), get_res_full_path(res_url))

    html_dom.prettify()
    filename = get_page_name(url) + '.html'
    save(html_dom.encode(), download_path, filename)
