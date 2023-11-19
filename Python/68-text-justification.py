class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        """
        https://leetcode.com/problems/text-justification/description/

        TC: O(m * n), SC: O(m) or O(1) where m = len(words) and n = maxWidth
        """
        full_justify = []

        def justify_last_line(line: list[str], line_char_count: int) -> None:
            total_number_of_spaces_to_add = maxWidth - line_char_count

            if total_number_of_spaces_to_add:
                for i in range(len(line)):
                    line[i] += " "
                    total_number_of_spaces_to_add -= 1
                    if total_number_of_spaces_to_add == 0:
                        break

            if total_number_of_spaces_to_add:
                line[-1] += " " * total_number_of_spaces_to_add

            full_justify.append("".join(line))

        def justify_line(line: list[str], line_char_count: int) -> None:
            total_number_of_spaces_to_add = maxWidth - line_char_count

            if len(line) == 1 or len(line) == 2:
                line[0] += " " * total_number_of_spaces_to_add
                full_justify.append("".join(line))
                return

            index = 0
            while total_number_of_spaces_to_add:
                line[index] += " "
                total_number_of_spaces_to_add -= 1
                index += 1

                if index == len(line) - 1:
                    index = 0

            full_justify.append("".join(line))

        line = []
        line_char_count = 0

        for word in words:
            if len(word) + len(line) + line_char_count > maxWidth:
                justify_line(line, line_char_count)
                line = [word]
                line_char_count = len(word)
            else:
                line.append(word)
                line_char_count += len(word)

        justify_last_line(line, line_char_count)

        return full_justify
