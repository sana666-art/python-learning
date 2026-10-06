"""Topic 8: Operator Precedence

Precedence decides which operator grabs its operands first. When two
operators compete, the higher one binds tighter. Brackets always win.

Run with:  python 08-operator-precedence.py
"""

print("=" * 60)
print("WHY PRECEDENCE MATTERS")
print("=" * 60)
print("Python has to decide what 1 + 2 * 3 means. It could be 9 if the plus")
print("went first, or 7 if the times went first. Precedence fixes the order")
print("so expressions always have one meaning.")

print()
print("1 + 2 * 3 ->", 1 + 2 * 3, "  (* binds tighter, so it goes first)")
print("(1 + 2) * 3 ->", (1 + 2) * 3, "  (brackets force the plus first)")

print()
print("Read an expression by thinking about which operator is grabbed first.")
print("The tightest one wins, then the next, and so on.")

print()
print("=" * 60)
print("THE FULL PRECEDENCE TABLE")
print("=" * 60)
print("Highest at the top. Operators on the same row share a level, so they")
print("are applied from left to right unless the table says otherwise.")
print("""
 1  ()            brackets, subscript [], call (), attribute .
 2  **            exponent, right to left
 3  +x  -x  ~x    positive, negative, bitwise NOT (unary)
 4  *  /  //  %   multiply, divide, floor divide, remainder
 5  +  -          add, subtract
 6  <<  >>        bit shifts
 7  &             bitwise AND
 8  ^             bitwise XOR
 9  |             bitwise OR
10  ==  !=  <  >  <=  >=  in  not in  is  is not   comparisons
11  not           logical NOT
12  and           logical AND
13  or            logical OR
14  if else       conditional expression
15  lambda        small anonymous function
16  :=            walrus, assignment expression
""")

print("=" * 60)
print("LEVELS IN ACTION: THE ARITHMETIC GROUP")
print("=" * 60)

print("Multiplication beats addition:")
print("   1 + 2 * 3      ->", 1 + 2 * 3)
print("   2 * 3 + 1      ->", 2 * 3 + 1)
print("   10 - 4 / 2     ->", 10 - 4 / 2, "  (/ beats -)")
print("   10 - 4 // 2    ->", 10 - 4 // 2, "  (// beats -)")
print("   2 * 3 % 4      ->", 2 * 3 % 4, "  (* and % tie, so left to right:")
print("                                       2*3=6, then 6%4=2)")

print()
print("Exponent beats multiplication:")
print("   2 * 3 ** 2     ->", 2 * 3 ** 2, "  (3**2=9, then 2*9=18)")
print("   (2 * 3) ** 2   ->", (2 * 3) ** 2, "  (6**2=36)")

print()
print("Unary signs beat multiplication and exponent on their own operand:")
print("   -2 ** 2        ->", -2 ** 2, "  (** binds tighter, so this is -4)")
print("   (-2) ** 2      ->", (-2) ** 2, "  (4, because the brackets hold)")
print("   2 ** -2        ->", 2 ** -2, "  (negative exponent is fine on the right)")
print("   -3 * 2         ->", -3 * 2)
print("   4 + -3         ->", 4 + -3, "  (unary minus attaches to the 3 only)")

print()
print("The classic traps:")
print("   -2 ** 2  is  -(2 ** 2)  = -4, not 4.")
print("   2 ** 3 ** 2 is 2 ** (3 ** 2) = 512, not 64, because ** is right to")
print("   left: 3 ** 2 = 9 first, then 2 ** 9 = 512.")

print()
print("=" * 60)
print("ASSOCIATIVITY: WHICH DIRECTION")
print("=" * 60)
print("Most operators go left to right. ** and a few others go right to left.")

print("Left to right:")
print("   10 - 3 - 2  ->", 10 - 3 - 2, "  ((10-3)-2 = 5, not 10-(3-2) = 9)")
print("   100 / 10 / 2 ->", 100 / 10 / 2, "  (5.0, not 20.0)")
print("   2 ** 3 ** 2  ->", 2 ** 3 ** 2, "  (right to left: 2**(3**2) = 512)")

print()
print("Assignment goes right to left, so a value is computed once:")
a = b = c = 7
print("   a = b = c = 7  ->  a =", a, "| b =", b, "| c =", c)

print()
print("Left to right is the default when you are unsure, but brackets remove")
print("the doubt entirely.")

print()
print("=" * 60)
print("COMPARISONS ALL SHARE ONE LEVEL")
print("=" * 60)
print("==, !=, <, >, <=, >=, in, is and their opposites are one family,")
print("which is why they chain and why a misunderstanding is easy.")

print("   1 + 2 == 3      ->", 1 + 2 == 3, "  (+ beats ==, so it checks 3)")
print("   5 > 2 + 1       ->", 5 > 2 + 1, "  (+ beats >)")
try:
    10 in 5 + 5
except TypeError as error:
    print("   10 in 5 + 5       -> TypeError:", error)
print("   (+ runs first and leaves a number, and a number is not a container)")

print()
print("Because comparisons share a level, they can be written in a chain:")
x = 5
print("x =", x)
print("   1 < x < 10    ->", 1 < x < 10, "  (means 1 < x and x < 10)")
print("   1 < x > 10    ->", 1 < x > 10, "  (means 1 < x and x > 10)")
print("   x == 5 or 6   ->", x == 5 or 6, "  (= binds tighter than or)")
print()
print("A chain is not the same as comparing a comparison to a number:")
print("   1 < x and x < 10  ->", 1 < x and x < 10)
print("   Compare that with writing 1 < x < 10, which is the clean form.")

print()
print("A comparison against a boolean is usually a mistake:")
print("   1 < x < True   would fail or mislead, because chained links must")
print("   each be a comparison, not a bool.")

print()
print("=" * 60)
print("MEMBERSHIP AND IDENTITY SIT WITH COMPARISONS")
print("=" * 60)
print("in, not in, is and is not are the same level as < and ==")
print("because they all answer a yes or no question.")

numbers = [1, 2, 3]
print("numbers =", numbers)
print("   2 in numbers          ->", 2 in numbers)
print("   1 + 1 in numbers      ->", 1 + 1 in numbers, "  (+ beats in)")
print("   numbers and 2 in numbers ->", numbers and 2 in numbers)
print("   (and binds looser, so the membership test runs first)")

print()
print("=" * 60)
print("LOGICAL OPERATORS: not, and, or")
print("=" * 60)
print("Each level is looser than the last, which gives a fixed reading order.")

print("   not True or False     ->", not True or False,
      "  (not binds tighter: (not True) or False)")
print("   not (True or False)   ->", not (True or False))
print("   True or False and False ->", True or False and False,
      "  (and binds tighter than or)")
print("   (True or False) and False ->", (True or False) and False)

print()
print("So a chain always reads as:")
print("   a or b and c      means  a or (b and c)")
print("   not a and b       means  (not a) and b")
print("   not a or b        means  (not a) or b")

print()
print("Brackets are cheap and make the intent obvious. Use them when a")
print("condition has more than two parts.")

print()
print("=" * 60)
print("BRACKETS ALWAYS BEAT MEMORY")
print("=" * 60)
print("Rather than memorise the table, write brackets when anything is in")
print("doubt. Extra brackets cost nothing and read clearly.")

print()
print("value = (2 + 3) * (4 - 1)      ->", (2 + 3) * (4 - 1))
print("result = (age >= 18) and (score > 50)")
age = 20
score = 70
print("   with age =", age, "score =", score, "->", (age >= 18) and (score > 50))
print()
print("Python ignores brackets that are not needed, so (a + b) is identical")
print("to a + b at run time. They exist for the reader.")

print()
print("=" * 60)
print("A FULL EXPRESSION, UNPACKED")
print("=" * 60)
print("Take one line and read it with the table, one level at a time.")

expression = "2 + 3 * 4 ** 2 - 6 // 4"
print("   ", expression)
print()
print("Step 1  ** binds tightest:        4 ** 2 = 16")
print("Step 2  * and // share a level, applied left to right through the")
print("        expression: 3 * 16 = 48, and 6 // 4 = 1")
print("Step 3  + and - are the last level, left to right: 2 + 48 = 50,")
print("        then 50 - 1 = 49")
print()
print("    2 + 3 * 4 ** 2 - 6 // 4  =", 2 + 3 * 4 ** 2 - 6 // 4)
print()
print("Check it with brackets that spell out the same order:")
print("    2 + (3 * (4 ** 2)) - (6 // 4) =",
      2 + (3 * (4 ** 2)) - (6 // 4))

print()
print("=" * 60)
print("OPERATORS AND PARENTHESISED CALLS")
print("=" * 60)
print("A call or a subscript binds tighter than any arithmetic, because it is")
print("level 1.")

print("   len('abc') + 1      ->", len("abc") + 1)
print("   [1, 2, 3][0] * 5    ->", [1, 2, 3][0] * 5)
print("   2 * len('abcd')     ->", 2 * len("abcd"))

print()
print("This is why a function call can be used directly in an expression")
print("without brackets around it.")

print()
print("=" * 60)
print("CONDITIONAL EXPRESSIONS BIND LOOSELY")
print("=" * 60)
print("The one line form value_if_true if condition else value_if_false sits")
print("just above lambda, so almost everything else runs first inside it.")

age = 20
status = "adult" if age >= 18 else "minor"
print("   age = 20")
print('   "adult" if age >= 18 else "minor" ->', status)
print()
print("   1 if True else 2 + 5 ->", 1 if True else 2 + 5,
      "  (the + runs before the choice)")
print()
print("Because it binds so loosely, mixing it with or is a common source of")
print("surprises. Add brackets:")
mixed = (1 if True else 2) or 3
print("   (1 if True else 2) or 3 ->", mixed)

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. -2 ** 2 read as 4. It is -4, because ** binds tighter than unary minus.
2. 2 ** 3 ** 2 read as 64. It is 512, because ** runs right to left.
3. Thinking a line of and / or must be evaluated strictly left to right.
   It is not: all of the and parts are settled first, then the or parts,
   which happens to match how (a and b) or c is grouped but is not the
   same rule.
4. Forgetting that ==, in and is share one level, so 1 + 1 == 2 works but
   1 + 1 in 2 is an error.
5. Mixing a conditional expression with or without brackets.
6. Chaining comparisons with a boolean at the end.
7. Believing brackets change the meaning of plain arithmetic. They only
   change which part runs first.
""")

print("Quick proofs:")
print("   -2 ** 2              ->", -2 ** 2)
print("   2 ** 3 ** 2          ->", 2 ** 3 ** 2)
print("   1 + 2 * 3 == 7       ->", 1 + 2 * 3 == 7)
print("   10 - 3 - 2           ->", 10 - 3 - 2)
print("   not True or False    ->", not True or False)
print("   True or False and False ->", True or False and False)
print("   2 + 3 == 5           ->", 2 + 3 == 5)

print()
print("=" * 60)
print("A PRACTICAL RULE OF THUMB")
print("=" * 60)
print("""
1. ** and unary signs first, then * / // %, then + -.
2. Comparisons and membership next, then not, and, or.
3. Write brackets whenever a line has two different families of operator.
4. If you have to think for more than a second, add brackets. The reader
   will thank you, and Python will produce the same answer either way.
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Precedence decides which operator binds its operands first; brackets
  always override it.
- ** is right to left, so 2 ** 3 ** 2 is 512. Unary minus binds looser
  than **, so -2 ** 2 is -4.
- Arithmetic levels run left to right: * / // % together, then + -.
- Comparisons, in and is share one level, which is why they chain.
- not, then and, then or, with conditional expressions binding loosest.
- When in doubt, use brackets. They cost nothing and help the reader.
""")