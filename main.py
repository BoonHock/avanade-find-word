def hasVowels(word):
    word = word.lower()
    return 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word

word0 = """abcdz
efghy
ijklx
mnopr"""

word00 = """ab
cd
ef
gh"""

word1 = """SVHNBMTLUTETWNIAOQ
OOHJCFTRENCHWANLCE
YPXRGDMISLEADRIXQM
RLGVLABORATORYYSMR
XGQAPPOINTGBMDXSTT
EWSIBUGRNBUNRAKOPR
RYWAKBDRYYANBIGUAA
GHECTACYKDEWNNDPLP
AWELUMPYBIYQSVSEMM
XATEMVETERANALRHJJ
EYAVOIVORYCZABGUUO
LHEALTHYAQBDGASZEH"""

word2 = """HCQEXPBKIHBFSOURLK
VFLHCUOVNGCLTPBPRK
GIANTKBLHFCBEWWFEP
HATYCONTAINSROISVR
SETTLEMENTAMEBGCIE
XENPPQSSKOJOONBHSD
IUNAWAREULQRTSIOEU
TRUYPRINCEMSYOXLVC
RAIXNJKTYOAEPHPAVE
PSSKINFOLIRLESARVF
NXKRMUQUZHKESTATEW
MPCANVASLKNULQYEFB"""

puzzles = [word2]
word_min_length = 3
lines = []

to_right = True
to_bottom = True
to_bottom_right = True

for puzzle in puzzles:
    array_split_line = puzzle.splitlines()
    # to right
    if to_right:
        for line in array_split_line:
            lines.append(line.lower())

    if len(array_split_line) > 0:
        # to bottom
        if to_bottom:
            for start_index in range(0, len(array_split_line[0])):
                line_text = ""
                for line in array_split_line:
                    line_text += line[start_index]
                if len(line_text) >= word_min_length:
                    lines.append(line_text.lower())

        # to bottom and right
        if to_bottom_right:
            for row_index in range(0, len(array_split_line)):
                line_text = ""
                for loop_row_index in range(row_index, len(array_split_line)):
                    if (loop_row_index - row_index >= len(array_split_line[loop_row_index])):
                        break
                    line_text += array_split_line[loop_row_index][loop_row_index - row_index]
                if len(line_text) >= word_min_length:
                    lines.append(line_text.lower())

            for col_index in range(1, len(array_split_line[0])):
                line_text = ""
                for loop_row_index in range(0, len(array_split_line)):
                    if (loop_row_index + col_index >= len(array_split_line[loop_row_index])):
                        break
                    line_text += array_split_line[loop_row_index][loop_row_index + col_index]
                if len(line_text) >= word_min_length:
                    lines.append(line_text.lower())

generated_words = []

for line in lines:
    for start_index in range(0, len(line) - word_min_length + 1):
        for x in range(start_index + word_min_length, len(line) + 1):
            if not line[start_index:x] in generated_words and hasVowels(line[start_index:x]):
                generated_words.append(line[start_index:x])

with open("words.txt", "w") as myfile:
    myfile.write('\n'.join(generated_words))

print(generated_words)