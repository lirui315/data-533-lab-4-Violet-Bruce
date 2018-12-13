# data-533-lab-4-Violet-Bruce
533 lab4 group repository for Violet(Rui Li) and Bruce(Xiangyu Pei)

## Travis CI Status:
***
[![Build Status](https://travis-ci.org/lirui315/data-533-lab-4-Violet-Bruce.svg?branch=master)](https://travis-ci.org/lirui315/data-533-lab-4-Violet-Bruce)

## 100% coverage has achieved on all of our four function. `birth`, `month`, and `nanur` 3 functions with 2 try-except each on this package called `padaku`, 

as the functions are producing graphs for different ranges of numeric values in the data using if-else statements. But the test datasets used to cover all these conditions(especially two extremes) could not be found. The data satisfying each of the conditions can be simulated but it is a time-consuming process.


## The main package 
***
from lab2 is called **`padaku`** which has 2 subpackages as below:

### Sub-package 1. *`birth`*

A. The sub-package *`birth`* has a module named *`birthdate`* which has class(*`birthinfo`*) and it has  sub-class(*`Year`*) and (*`Month`*) as inheritance

*`Year`*

TO DO: 
1. take birthday then returns the person's birth year

2. chinese_zodiac return the person's Chinese zodiac

**note: The Chinese zodiac is a classification scheme that assigns an animal and it represents for each year in a repeating 12 year cycle. Animals including in the cycle are rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, rooster, dog and pig.**

`Probably you can try it for yourself.`

*`Month`*

TO DO:
1. take person's birth month and date then return the person's constellation


B. The sub-package *`birth`* also has a *`number`* module which has a life_path_number function

TO DO: 
1. Group the numbers of birthdate together before adding

2. Do not reduce the Master Numbers of 11 or 22 to single digits until the final calculation.


### Sub-package 2. perinfo

A. The sub-package *`perinfo`* has an age module which has an *`age`* function

TO DO:
1. take a person's birthday as "YYYY-MM-DD" then returns the person's age


B. The sub-package *`perinfo`* has a *`nanur`* module which has a *`name`* function for name numerology.

TO DO:
The name function returns the person's name numerology which is showing the person's personality based on his/her full name. 

## The test package 
***
from lab 3**`testsuite`** which has a module **`TestSuite`** and a subpackage called **`unittests`**

1. **`TestSuite`** is the suite of four unit tests

2. the subpackage **`unittests`** has 4 unit tests to test 4 modules in **`padaku`** package seperately.
