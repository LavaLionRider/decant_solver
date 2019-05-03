import decant
class DEC_Token(decant.DECANT):
    def token(self, node):
        return tuple(node)
