# Validando CPF com Negative Lookahead

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# http://regex101.com
import re

regex = r"^(?!(\d)\1{2}\.\1{3}\.\d{3}-\1{2})\d{3}\.\d{3}\.\d{3}-\d{2}$"

test_str = ("123.456.789-11\n"
            "222.444.555-66\n\n"
            "999.999.999-99\n"
            "111.111.111-11\n"
            "444.444.444-44\n"
            "777.777.777-77\n"
            "999.999.999-99\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
