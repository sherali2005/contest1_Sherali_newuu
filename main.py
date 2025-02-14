# Full name: Jabborqulov Sherali
# Student Id: 230304
# Course: Intro to Data Science
# Contest #1
# Solved 21:32, 14th Feb 2025
# Task-1: typeBasedTransformer: Modifies values based on their type.
# Task-2: kwargsAcceptFun: Accepts and prints named arguments.
# Task-3: decorator_1: Measures execution time of a function.

from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer

if __name__ == "__main__":
 kwargsAcceptFun(
  fullName="Jabborqulov Sherali",
  studentId=230304,
  averageGpa=3.05,
  isMarried=False, 
 )
 typeBasedTransformer(
  intNumber=4,
  floatNumber=5.67,
  string="I Love You Uzbekistan",
  bloolean=True,
  myList=[1, 2, 3],
  myDict={"q": 1, "w": 2, "e": 3},
  notSupported={4, 5, 6}
 )
