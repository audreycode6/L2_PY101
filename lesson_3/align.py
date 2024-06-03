'''Back in the stone age (before CSS), we used spaces
to align things on the screen. If we have a 40-character
wide table of Flintstone family members, how can we
center the following title above the table with spaces?'''
title = "Flintstone Family Members"

align_title = title.center(40)
print(align_title)

#OR MANUALLY
table_length = 40
length = len(title)
leftover_space = (table_length - length)
if leftover_space % 2 != 0:
    title += ' '
spacing = (leftover_space // 2) * " "
align_title = spacing + title + spacing
print(align_title)
print(len(align_title))
