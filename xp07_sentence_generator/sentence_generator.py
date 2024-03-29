"""Sentence generator."""


def helper(lis):
    """Helper."""
    while True:
        for i in lis:
            yield i


rules = """
noun = koer | porgand | madis | kurk | tomat
target = koera | porgandit | madist | kurki | tomatit
verb = sööb | lööb | jagab | tahab | ei taha
adjective = ilus | kole | pahane | magus | sinu
targetadjective = ilusat | koledat | pahast | magusat | sinu
sentence = noun verb target .
beautifulsentence = adjective noun verb targetadjective target .
twosentences = sentence sentence
"""


class SentenceGenerator:
    """Class."""

    def __init__(self, rules_string):
        """Constructor."""
        rules_dict = {}
        rules_rows = rules_string.split('\n')
        for x in rules_rows:
            rule_name, x = x.split(' = ')
            x = [i for i in x.split() if i != '|']
            rules_dict[rule_name.strip()] = helper(x)
        self.rules = rules_dict
        print(self.rules)

    def sentence_generator(self, syntax):
        """Main function."""
        syntax = syntax.split()
        if len(syntax) != 0:
            while True:
                gen = ''
                for x in syntax:
                    if x in self.rules:
                        gen += str(next(self.rules[x])) + ' '
                yield gen
        else:
            while True:
                yield ''


if __name__ == '__main__':
    g = SentenceGenerator(rules)
    gg = g.sentence_generator("noun")
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    gg = g.sentence_generator("beautifulsentence noun")
    print(next(gg))
    print(next(gg))
    print(next(gg))
