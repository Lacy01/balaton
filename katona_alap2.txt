class balaton:
    def __init__(self, település, fekvés,lakos,elotag):
        self. település = település
        self. fekvés = fekvés
        def elotag(self):
            if elotag=="é":
                return "északi"
            else:
                return "déli"
        def lakos(self):
            if lakos<5000:
                return "falu"
            elif lakos>5000:
                return "nagyközség"
            else:
                return "város"