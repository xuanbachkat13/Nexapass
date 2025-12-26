from detector import detect_resolvers
from utils import normalize_url

class BypassEngine:
    def __init__(self):
        self.resolvers = []

    def register(self, resolver):
        self.resolvers.append(resolver)

    def resolve(self, url, depth=0):
        if depth >= 6:
            return url

        url = normalize_url(url)
        resolver_list = detect_resolvers(url, self.resolvers)

        for r in resolver_list:
            if r.match(url):
                try:
                    new = r.resolve(url)
                    if new and new != url:
                        return self.resolve(new, depth + 1)
                except:
                    pass

        return url
