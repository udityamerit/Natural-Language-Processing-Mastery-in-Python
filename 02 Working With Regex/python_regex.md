# Python RegEx

Python provides a module named `re` to work with regular expressions. This module offers various functions and constants to perform operations on strings using regular expressions.

| **Method**     | **Description**                                                                 | **Example**                                                                                  |
|----------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `re.findall()` | Returns a list of all matches in the string.                                    | `re.findall('\d+', 'hello 12 hi 89. Howdy 34')` <br> Output: `['12', '89', '34']`            |
| `re.split()`   | Splits the string at each match and returns a list of strings.                  | `re.split('\d+', 'Twelve:12 Eighty nine:89.')` <br> Output: `['Twelve:', ' Eighty nine:', '.']` |
| `re.sub()`     | Replaces matches in the string with a specified string.                         | `re.sub('\s+', '', 'abc 12\\de 23 \n f45 6')` <br> Output: `abc12de23f456`                   |
| `re.subn()`    | Similar to `re.sub()`, but returns a tuple with the new string and number of substitutions. | `re.subn('\s+', '', 'abc 12\\de 23 \n f45 6')` <br> Output: `('abc12de23f456', 4)`           |
| `re.search()`  | Searches for the first location where the pattern matches and returns a match object. | `re.search('\APython', 'Python is fun')` <br> Output: Match object or `None`                |
| `match.group()` | Returns the part of the string where there is a match.                         | `match.group(1)` <br> Example: `'801'`                                                      |
| `match.start()`| Returns the start index of the match.                                           | `match.start()` <br> Example: `2`                                                           |
| `match.end()`  | Returns the end index of the match.                                             | `match.end()` <br> Example: `8`                                                             |
| `match.span()` | Returns a tuple containing the start and end index of the match.                | `match.span()` <br> Example: `(2, 8)`                                                       |

This table provides a quick reference to the key functions and methods of the `re` module, along with simple examples to illustrate their usage.

## Getting Started

To use regular expressions in Python, you need to import the `re` module:

```python
import re
```

The module defines several functions to work with RegEx, such as `findall()`, `split()`, `sub()`, `subn()`, `search()`, and more.

## Functions and Examples

### 1. `re.findall()`

The `re.findall()` method returns a list of strings containing all matches of the pattern in the string.

**Example 1: Extracting numbers from a string**

```python
import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)
# Output: ['12', '89', '34']
```

If the pattern is not found, `re.findall()` returns an empty list.

### 2. `re.split()`

The `re.split()` method splits the string where the pattern matches and returns a list of strings.

**Example 2: Splitting a string by numbers**

```python
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)
# Output: ['Twelve:', ' Eighty nine:', '.']
```

You can also pass the `maxsplit` argument to limit the number of splits.

```python
import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# Split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)
# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
```

### 3. `re.sub()`

The `re.sub()` method replaces the matches of the pattern in the string with the specified replacement string.

**Example 3: Removing all whitespaces**

```python
import re

string = 'abc 12\\de 23 \n f45 6'
pattern = '\s+'
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)
# Output: abc12de23f456
```

You can also pass the `count` argument to limit the number of substitutions.

```python
import re

string = 'abc 12\\de 23 \n f45 6'
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1)
print(new_string)
# Output:
# abc12de 23
# f45 6
```

### 4. `re.subn()`

The `re.subn()` method is similar to `re.sub()` but returns a tuple containing the new string and the number of substitutions made.

**Example 4: Removing all whitespaces and counting substitutions**

```python
import re

string = 'abc 12\\de 23 \n f45 6'
pattern = '\s+'
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)
# Output: ('abc12de23f456', 4)
```

### 5. `re.search()`

The `re.search()` method searches for the first location where the pattern matches in the string. If found, it returns a match object; otherwise, it returns `None`.

**Example 5: Searching for a pattern**

```python
import re

string = "Python is fun"

# Check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
    print("Pattern found inside the string")
else:
    print("Pattern not found")
# Output: Pattern found inside the string
```

### 6. Match Object

A match object contains information about the match and can be queried using methods like `group()`, `start()`, `end()`, `span()`, etc.

**Example 6: Working with a match object**

```python
import re

string = '39801 356, 2102 1111'
pattern = '(\d{3}) (\d{2})'

match = re.search(pattern, string)

if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
    print(match.start())
    print(match.end())
    print(match.span())
# Output:
# 801 35
# 801
# 35
# ('801', '35')
# 2
# 8
# (2, 8)
```

### 7. Using `r` Prefix for Raw Strings

The `r` prefix before a string means it's a raw string, where backslashes are treated as literal characters.

**Example 7: Raw string with escape sequences**

```python
import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string)
print(result)
# Output: ['\n', '\r']
```
