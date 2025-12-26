from urllib.parse import urlparse

def detect_resolvers(url, resolvers):
    domain = urlparse(url).netloc.lower()
    matched = []

    for r in resolvers:
        for d in r.domains:
            if d in domain:
                matched.append(r)

    return matched if matched else resolvers
