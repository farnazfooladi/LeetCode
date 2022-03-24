class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def add_word(spaces, curr):
            spaces += maxWidth - (curr + spaces)            # add remaining spaces
            if len(line) > 1:                               # contain multiple words
                mid, last = divmod(spaces, len(line) - 1)   # get expected len of spaces 
                if not last:                                # spaces divided evenly
                    res = (" " * mid).join(line)
                else:                                       # spaces divided oddly
                    res = []
                    for word in line:                       # reiterate words in line to add spaces
                        add = 0
                        if last:                            # check if we have more extra spaces
                            add += 1                        # add + 1 until we exceed all 'last' spaces
                            last -= 1                       # decrement accordingly
                        res.append(word)                    # add word
                        res.append(" " * (mid + add))       # add space
                    res.pop()                               # remove last extra space
                    res = "".join(res)
                lines.append(res)
            else:                                           # contain single word
                lines.append("".join(line) + " " * spaces)
        
        lines = []
        line = []
        curr = 0
        spaces = 0
        for word in words:
            if not line:                                    # start of a sentence
                line.append(word)
                curr += len(word)
            elif curr + spaces + 1 + len(word) > maxWidth:  # new line
                add_word(spaces, curr)
                line = [word]                               # init to start of a sentence
                curr = len(word)
                spaces = 0
            else:                                           # continue with curr line
                line.append(word)
                curr += len(word)
                spaces += 1
        if line:                                            # add last line
            final_line = [" ".join(line)]
            final_line.append(" " * (maxWidth - (curr + spaces)))
            lines.append("".join(final_line))
        return lines