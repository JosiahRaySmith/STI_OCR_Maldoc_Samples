#!/usr/bin/env python3
import re
import sys
with open(sys.argv[1], "rb") as fp:
    contents = fp.read()
    match = re.search(b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", contents)
    if not match:
        sys.exit("No match")
    with open("output", "wb") as output:
        output.write(contents[match.start():])
