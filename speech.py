import textwrap

def speech_bubble(text):
    top_line="_"*35 # Creates a line 35 dashes long
    print("\n", top_line.rjust(52)) # Prints the line justified to the right
    print("/".rjust(18), "\ ".rjust(36)) # Prints the first line of slashes
    if len(text) < 30:
        print('|'.rjust(17), text.rjust(5 + len(text)), '|'.rjust(33 - len(text)), end="\n", sep="")
        print('\\'.rjust(18), ('_'*32).rjust(33), '/', end="")
    else:
        wrapper = textwrap.TextWrapper(width=30)
        word_list = wrapper.wrap(text=text)
        for i in range(len(word_list)):
            if i == 0:
                print('/'.rjust(17), word_list[i].rjust(2 + len(word_list[i])), '\\'.rjust(34 - len(word_list[i])))
            if i == 1:
                print('\\'.rjust(17), word_list[i].rjust(2 + len(word_list[i])), '/'.rjust(34 - len(word_list[i])), end="")

