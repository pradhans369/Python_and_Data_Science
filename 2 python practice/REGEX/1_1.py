"""
.           :  Any Character Except New Line
\d          :  Digit (0 - 9)
\D          :  Not a Digit (0 - 9)

\w          :  Word Character (a - z, A - Z, 0 - 9, _)
\W          :  Not a Word Character

\s          :  Whitespace (space, tab, newline)
\S          :  Not Whitespace (space, tab, newline)

\b          :  Word Boundary
\B          :  Not a Word Boundary

^           :  Beginning of a String
$           :  End of a String
.           :  Matches all the symbols

[]          :  Matches Characters in brackets
[^ ]        :  Matches Characters NOT in brackets
|           :  Either Or
( )         :  Group

"^_text_"   : searches only for text that is at the start of the string
"_text_$"   : searches only for text that is at the end of the string

---QUANTIFIERS---
*           :  0 or More
+           :  1 or More
?           :  0 or One
{3}         :  Exact Number
{3,4}       :  Range of Numbers (Minimum, Maximum)


re.search()     : prints the first occurace in the string and its span
re.findall()    : prints all the occurances in the string 









"""