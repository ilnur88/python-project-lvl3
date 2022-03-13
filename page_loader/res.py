from urllib.parse import urlparse

RES_TYPES = ('img', 'link', 'script')
RES_REFS = {'src', 'href'}

def is_image(resource):
    for attribute in resource.attrs:
        if attribute in RES_REFS:
            p_url = urlparse(resource.get(attribute))
            if len(p_url.path) > 1 and not (p_url.netloc or p_url.scheme):
                return True
    return False


def get_images(html_dom):
    return list(filter(is_image, html_dom.find_all(RES_TYPES)))


def get_res_path(res):
    for ref in RES_REFS:
        if res.has_attr(ref):
            return res.attrs[ref]


def update_link(res, new_link):
    for ref in RES_REFS:
        if res.has_attr(ref):
            res.attrs[ref] = new_link
