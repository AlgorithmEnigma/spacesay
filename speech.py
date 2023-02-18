import textwrap


def speech_bubble(text: str):
    max_length = 35

    wrapped_text = []
    split_text = text.split(", ")
    for i in split_text:
        wrapped_text.append(textwrap.wrap(i, max_length))
    # print(wrapped_text)

    top_line = "_" * max_length
    print("\n", top_line.rjust(52))
    print("/".rjust(18), "\ ".rjust(37), sep="", end="\n")
    for i in wrapped_text:
        print("|".rjust(17), "    ", i[0], "|".rjust(34 - len(i[0])), sep="")

    print("\\".rjust(18), ("_" * (max_length - 2)).rjust(35), "/", sep="", end="")
