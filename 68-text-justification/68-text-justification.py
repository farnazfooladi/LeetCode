class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        # number of words in the current line
        count_words = 0
        # number of non-space characters in the current line
        count_chars = 0
        # start index of the word list in the current line
        start = 0
        for i in range(len(words)):
            # if current line ends with the previous words
            # all words + space between them + the current word (no space with the previous word if any) reaches/exceeds the maxWidth of the current line, append the current line to the result and start a new line
            if count_chars + count_words - 1 + len(words[i]) >= maxWidth:
                # count the number of additional space character between words
                space = maxWidth - count_chars - (count_words - 1)
                # check whether the denominator is 0 (only one word in the current line)
                if count_words == 1:
                    res.append(words[start] + ' '*space)
                # count number of additional space evenly distributed across words and the extra remainder of space for the first few words
                else:
                    sep = space // (count_words-1)
                    rem = space % (count_words-1)
                    temp = ''
                    for j in range(start, i):
                        temp += words[j] + (' ' * (sep+2) if j < start+rem else ' ' * (sep+1))
                    res.append(temp[: maxWidth])
                # reset and start a new line
                start = i
                count_chars = 0
                count_words = 0
            # count the current word
            count_words += 1
            count_chars += len(words[i])
        # last line left justified
        space = maxWidth - count_chars - (count_words - 1)
        res.append(' '.join(words[start:]) + ' '*space)
        return res