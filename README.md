# fizbuzz-framework

A simple library for designing programs to play Fiz Buzz and similar counting games. 

The rules of Fiz Buzz are as follows:

   1. A player starts counting up from 1.
   1. When the player reaches a number divisible by 3, they say "fiz", instead of that number.
   1. When the player reaches a number divisible by 5, they say "buzz". 
   1. When the player reaches a number divisible by both 3 and 5, they say "fizbuzz".
 
A program to play Fiz Buzz can be written as follows:
 
<pre><code>from general_counting_game import GeneralCountingGame


class ModGame(GeneralCountingGame):
    
    def add_phrase(n, num):
        return n % num == 0
        

fiz_buzz_player = ModGame((("fiz", 3), ("buzz", 5)))</code></pre>

Full details for how these games work and how to create them, can be found in both the main and test files.
