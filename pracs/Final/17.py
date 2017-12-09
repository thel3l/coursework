with open('STORY.TXT', 'w') as file:
    file.write('abc def\nfdsfs sdfs\nzzz xcc')

# Do not write what's above this line.
# -----------------------------------

c = 0
with open('STORY.TXT', 'r') as file:
    for line in file:
        if line[0].lower() != 'a':
            c += 1

print 'Number of lines not starting with A:', c