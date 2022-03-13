from urllib.parse import urlparse


def is_image(resource):
    for attribute in resource.attrs:
        if attribute == 'src':
            p_url = urlparse(resource.get(attribute))
            if len(p_url.path) > 1 and not (p_url.netloc or p_url.scheme):
                return True
    return False


def get_images(html_dom):
    return list(filter(is_image, html_dom.find_all('img')))


def get_res_path(res):
    if res.has_attr('src'):
        return res.attrs['src']


def update_link(res, new_link):
    if res.has_attr('src'):
        res.attrs['src'] = new_link
