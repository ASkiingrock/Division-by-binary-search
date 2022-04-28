-------------- DIVISION by binary search -------------

So this is my division function without using division
- It's a bit slow
- No real need for it
- Also the limit of the numbers you can use is just for ease and not bothering about calculating what will throw a recursion error or whatever

Despite all of that I'm pretty proud of it just cause it's kind of interesting

How does it work?
-----------------

1) Get the number you want to divide (numerator), we'll call this T
2) Get the number you want to divide by (denominator), we'll call this M
3) It does binary search of the numbers up to T, to see what numbers are closest to, when multiplied by M, resuling in T
4) This is accomplished through altering the upper and lower bounds and then guessing in the middle (binary search)
5) This is accomplished using recursion
6) Once he whole part of the number is calculated, then it iteratively runs the function again, rounding to smaller and smaller decimal places
7) This goes up to 13 decimal places, as it throws a recursion error if I go any further

For the square root file, instead of step 3, it checks whether the guess * guess == T

How do I run it?
----------------

For division, run division.py
For square roots, run sqrt.py

Will this crash the housing market?
-----------------------------------

No, why would you ask that?

Will you be coming to tour around my home city showing off your intellectual prowess?
-------------------------------------------------------------------------------------

Depends on what's in it for me

Is this the end of he README?
-----------------------------

Yes.
