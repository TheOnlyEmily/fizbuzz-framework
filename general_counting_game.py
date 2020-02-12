class GeneralCountingGame:

    def __init__(self, phrase_number_pairs):
        sorted_pairs = sorted(phrase_number_pairs, key=lambda v: v[-1])
        self._phrase_number_pairs = sorted_pairs

    def game_sequence(self, upper_limit):
        for i in range(1, upper_limit):
            response = self.build_text_response_for_number_(i)
            yield response if response else i

    def build_text_response_for_number_(self, n):
        filter_fn = lambda v: self.add_phrase(n, v[-1])
        filtered_pairs = filter(filter_fn, self._phrase_number_pairs)
        phrases = map(lambda v: v[0], filtered_pairs)
        return ''.join(phrases)

    def add_phrase(self, n, num):
        raise NotImplementedError()
