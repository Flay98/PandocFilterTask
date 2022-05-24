from panflute import *
import sys

headers = []


def repeated_header_message(elem):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write("Attention! Repeated header!" + stringify(elem))
        else:
            headers.append(stringify(elem))


def header_level_changer(elem, _):
    if isinstance(elem, Header) and elem.level >= 3:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def bold_the_word_bold(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([repeated_header_message, header_level_changer], prepare=bold_the_word_bold)
