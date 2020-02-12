class GeneralCountingGame:
    """
    Effectively plays a series of counting games like Fiz Buzz.

    Fiz Buzz is played by counting (starting at 1). When a multiple of 3 is
    reached, the player must say "Fiz", and when a multiple of 5 is reached,
    the player must say "Buzz". Reaching a multiple of both 3 and 5 means the
    player must say "Fizbuzz".

    Essentially, these games are played by first counting up from 1 and
    periodically replacing numbers with words, depending on the properties of a
    particular number the player counts up to. Should multiple rules/phrases
    apply, then the phrases are combined lowest to highest, with respect to the
    number associated with each phrase (ie. in Fizbuzz 15 is both a multiple of
    3 and 5 five, as 3 < 5 the correct phrase becomes "fiz" + "buzz").
    """
    def __init__(self, phrase_number_pairs):
        """
        Prepairs a list of phrase number associations.

        Arguments:
            phrase_number_pairs (Sequence(tuple(str, int))): The str or phrase
            will be outputted when the rule associated with the int is triggered.
        """
        sorted_pairs = sorted(phrase_number_pairs, key=lambda v: v[-1])
        self._phrase_number_pairs = sorted_pairs

    def game_sequence(self, upper_limit):
        """
        The main generator method, used to create the number/phrase sequences
        that result from playing a counting game.

        Arguments:
            upper_limit (int): Represents the highest number being counted up
            to (non-inclusive).

        Yields:
            (str | int): A number or phrase in accordance with the game rules.
        """
        for i in range(1, upper_limit):
            response = self.build_text_response_for_number_(i)
            yield response if response else i

    def build_text_response_for_number_(self, n):
        """
        Responsible for producing in phrases resulting from the game rules.

        Arguments:
            n (int): The number that the games rules are being applied to.

        Returns:
            (str): If no rules apply, then an empty string is returned.
            Otherwise, every applicable phrase is found and concatinated
            together with the other applicable phrases to create the
            resulting phrase.
        """
        filter_fn = lambda v: self.add_phrase(n, v[-1])
        filtered_pairs = filter(filter_fn, self._phrase_number_pairs)
        phrases = map(lambda v: v[0], filtered_pairs)
        return ''.join(phrases)

    def add_phrase(self, n, num):
        """
        Responsible for applying rules to a number being counted up to, so it
        can be determined if the associated phrase should be produced.

        Arguments:
            n (int): The number that has been counted up to.

            num (int): The number that n is being compared to using the rules
            of the game.

        Returns:
            (bool): Whether the phrase associated with num should be produced,
            according to the rules of the game. 
        """
        raise NotImplementedError()
