# Regex Symbols Cheat Sheet

---

## Basic Symbols
- **`.`** → any character except a newline  
- **`*`** → 0 or more occurrences (repetition) of the preceding element  
- **`+`** → 1 or more occurrences (repetition) of the preceding element  
- **`?`** → 0 or 1 occurrence (optional) of the preceding element  
- **`^`** → beginning of a string  
- **`$`** → end of a string  

---

## Character Sets & Quantifiers
- **`[]`** → a set of characters  
- **`[^]`** → matches any one character _not_ inside the brackets 
- **`{}`** → exact number of occurrences of the preceding element  
- **`{m}`** → exactly *m* occurrences of the preceding element  
- **`{m,n}`** → from *m* to *n* occurrences of the preceding element  
- **`|`** → either or  
- **`()`** → grouping (capturing group; stores the match for later reference)
- **`A|B`** → matches either **'A'** or **'B'**
- **`(?:)`** → non‑capturing group (groups without storing the match)

---

## Escapes & Special Classes
- **`\`** → escape special characters  
- **`\d`** → any digit (0–9)  
- **`\D`** → any non-digit character  
- **`\w`** → any alphanumeric character (a–z, A–Z, 0–9, _)  
- **`\W`** → any non-alphanumeric character  
- **`\s`** → any whitespace character (space, tab, newline)  
- **`\S`** → any non-whitespace character  