class Codec:
    mapper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    idx = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        r = self._encode(len(self.idx))
        self.idx.append(longUrl)
        return 'http://tinyurl.com/'+r

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str

        """
        code = shortUrl.replace('http://tinyurl.com/','')
        n = self._decode(code)
        return self.idx[n]

    def _encode(self, n):
        result = []
        while n > 0: result, n = [self.mapper[n % 62]] + result, n // 62
        return ''.join(result) #['a']*max(0,6-len(result))+

    def _decode(self, short_url):
        result = 0
        for idx, c in enumerate(short_url):
            oc = ord(c)
            if ord('a') <= oc and oc <= ord('z'): result = result * 62 + (oc - ord('a'))
            elif ord('A') <= oc and oc <= ord('Z'): result = result * 62 + (oc - ord('A') + 26)
            elif ord('0') <= oc and oc <= ord('9'): result = result * 62 + (oc - ord('0') + 52)
            else: raise Exception('Wrong URL')
        return result

c = Codec()
r = c.encode('abc')
print(r)
print(c.decode(r))