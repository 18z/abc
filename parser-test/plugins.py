def load_modules():

    from print_url import print_url
    plugins = dict()

    urltp = print_url()

    plugins['print_url'] = urltp

    return plugins

__modules__ = load_modules()
