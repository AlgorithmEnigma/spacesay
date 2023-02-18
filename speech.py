import textwrap


def speech_bubble(text: str | list):
    max_length = 35

    top_line = "_" * max_length
    print("\n", top_line.rjust(52))
    print("/".rjust(18), "\ ".rjust(37), sep="", end="\n")

    if isinstance(text, str):
        wrapped_text = []
        split_text = text.split(", ")
        for i in split_text:
            wrapped_text.append(textwrap.wrap(i, max_length))
        # print(wrapped_text)

        for i in wrapped_text:
            print("|".rjust(17), "    ", i[0], "|".rjust(34 - len(i[0])), sep="")

    else:
        print("|".rjust(17), "The ISS is over: ".rjust(25), "|".rjust(13), sep="")
        print(
            "|".rjust(17),
            text[0].rjust(8 + len(text[0])),
            "|".rjust(30 - len(text[0])),
            sep="",
        )
        print("|".rjust(17), "As of: ".rjust(15), text[1], "|".rjust(13), sep="")

    print("\\".rjust(18), ("_" * (max_length - 2)).rjust(35), "/", sep="", end="")
