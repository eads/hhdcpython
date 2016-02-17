# Lesson

This exercise is meant to be as similar to a real world data cleaning task as possible. That means that in addition to writing some Python code, you'll be doing some command line work and using Git. 

I've had to take just one shortcut due to some limitations of PythonAnywhere, which I will note in the lesson. 

What seems like the biggest shortcut -- I prepared the skeleton of the code for you already -- isn't a shortcut in the real world at all. I *always* start data projects with a data processing template. I often develop it to a point I can pass it off to another developer who can handle the task but shouldn't have to worry about weird system and Python quirks. 

If you need to do this kind of work, you're probably going to be spending a lot of time studying and modifying other people's code.

## The problem

A reporter at your publication would like you to clean up some data for a story about fringe religious groups in Mexico. She doesn't need anything fancy, just an overall count of the number of groups in the country and a count of the number of members per group.

The good news is that Mexican government has collects and releases data about known religious groups. The not-so-good news is that instead of a friendly CSV file that you could import into Excel, the data is locked up in a [1,964 page PDF document](http://www.asociacionesreligiosas.gob.mx//work/models/AsociacionesReligiosas/pdf/Numeralia/MC_por_SGAR.pdf).

You could try to copy and paste and manually clean up the data, but that's a lot of work. Who wants to do a lot of work? More importantly, you'll have even *more* work if you make a mistake, and if the government releases a new list, you'll have more work still. But if you write some code to clean the data, you can repeatedly process the data. With a little code, mistakes are no longer time-killers. If new data is released, you can simply swap out the old data for the new and re-run your analysis.

## The starting point

Your colleague David started working on the project using the team's data processing template. The code and data is in a git repo that you've forked and installed on PythonAnywhere.

_**Note:** If this were a true front-to-back exercise, we'd store the data outside of the git repository and write code to download the PDF and extract the text using a utility like `pdftotext`. Because PythonAnywhere has some significant processing limits for free accounts, I've done this for you and trimmed the dataset from 1,964 pages to 25._

To get started, you should study the [source PDF](http://www.asociacionesreligiosas.gob.mx//work/models/AsociacionesReligiosas/pdf/Numeralia/MC_por_SGAR.pdf) and the lightly processed [text file](data/MC_por_SGAR-trimmed.txt) that will be used in your script.

---

**Warning:** The rest of the lesson will be covered in person. If you are attending the Hacks/Hackers DC meetup, please stop here. If you can't make it, rock on!

## Writing some pseudo-code

First, find a partner to work with. Pair programming is, paradoxically, often more efficient than working in isolation. 

Hopefully, you've carefully studied the [source data](data/MC_por_SGAR-trimmed.txt). 

Now, get out that highly advanced technology called paper and pen (a word processor will work too) and write down human-language instructions about how you would process the data. Think about how you would explain it to someone who had to do it by hand.

For this data set, there's some gunk at the top of the file that comes from the PDF header:

```
DIRECTORIO DE MINISTROS DE CULTO
POR CLAVE DE REGISTRO SGAR

12/02/2016
Total: 76210

Dirección General de
Asociaciones Religiosas

```

Hey, there's step 1 of your instructions: Skip the gunk at the top.

Since you need to be very clear in your instructions, you should put a finer point on it: Skip the first 9 lines of the file.

* **Step 1:** Skip the first 9 lines of the file
