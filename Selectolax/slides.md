---
marp: true
theme: uncover
---
# selectolax
https://github.com/rushter/selectolax
---
---
# What's Behind It?
Useses Modest backend by default. Lexbor as the other option.
Modest is a HTML parser written entirely in C that was ported over to python
https://github.com/lexborisov/modest
The author wrote lexbor more recently, but the selectolax readme says it's still in beta.
The lexbor readme says it's stable and we should use it. 
---


View method definitions
.pxi and .pyx
HTMLParser - https://github.com/rushter/selectolax/blob/master/selectolax/parser.pyx
Node - https://github.com/rushter/selectolax/blob/master/selectolax/modest/node.pxi
Selection - https://github.com/rushter/selectolax/blob/master/selectolax/modest/selection.pxi
