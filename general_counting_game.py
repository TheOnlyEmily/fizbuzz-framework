class GeneralCountingGame:

    def __init__(self, phrase_number_pairs):
        self._phrase_number_pairs = phrase_number_pairs

    def game_sequence(self, upper_limit):
        for i in range(1, upper_limit):
            response = self.build_text_response_for_number_(i)
            yield response if response else i

    def build_text_response_for_number_(self, n):
        response = ""
        for phrase, num in self._phrase_number_pairs:
            if n % num == 0:
                response += phrase
        return response
