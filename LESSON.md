# Lesson

This exercise is meant to be as similar to a real world data cleaning task as possible. That means that in addition to writing some Python code, you'll be doing some command line work and using Git. 

I had to take one shortcut due to some limitations of PythonAnywhere, which I will note in the lesson. 

What seems like the biggest shortcut -- I prepared the skeleton of the code for you already -- isn't a shortcut in the real world at all. I *always* start data projects with a data processing template. I often develop it to a point I can pass it off to another developer who can handle the task but shouldn't have to worry about weird system and Python quirks. 

If you need to do this kind of work, you're probably going to be spending a lot of time studying and modifying other people's code. Pattern recognition is the name of the game here. You'll need to recognize the patterns in the data in order to clean it up. And you'll need to recognize patterns in code in order to modify it to suit your needs.

## The problem

A reporter at your publication would like you to clean up some data for a story about fringe religious groups in Mexico. She doesn't need anything fancy, just an overall count of the number of groups in the country and a count of the number of members per group.

The good news is that Mexican government has collects and releases data about known religious groups. The not-so-good news is that instead of a friendly CSV file that you could import into Excel, the data is locked up in a [1,964 page PDF document](http://www.asociacionesreligiosas.gob.mx//work/models/AsociacionesReligiosas/pdf/Numeralia/MC_por_SGAR.pdf).

The data includes the name of each religion followed by names of known members of the group. 

You could try to copy and paste and manually clean up the data, but that's a lot of work. Who wants to do a lot of work? More importantly, you'll have even *more* work if you make a mistake, and if the government releases a new list, you'll have more work still. But if you write some code to clean the data, you can repeatedly process the data. With a little code, mistakes are no longer time-killers. If new data is released, you can simply swap out the old data for the new and re-run your analysis.

## The starting point

Your colleague David started working on the project using the team's data processing template. The code and data is in a git repo that you've forked and installed on PythonAnywhere.

_**Note:** If this were a true front-to-back exercise, we'd store the data outside of the git repository and write code to download the PDF and extract the text using a utility like `pdftotext`. Because PythonAnywhere has some significant processing limits for free accounts, I've done this for you and trimmed the dataset from 1,964 pages to 25._

To get started, you should study the [source PDF](http://www.asociacionesreligiosas.gob.mx//work/models/AsociacionesReligiosas/pdf/Numeralia/MC_por_SGAR.pdf) and the lightly processed [text file](data/MC_por_SGAR-trimmed.txt) that will be used in your script.

## From messy input to clean output

You have input data that looks like this:

```
SGAR/2:3/13 OBRA DE CLERIGOS EN AYUDA SOLIDARIA
Nombre Completo
ADALBERTO SANDOVAL ACEVEDO

Total
4

JESUS CARLOS CABRERO ROMERO
OSCAR FLORES RAMIREZ
OSCAR ROBERTO DOMINGUEZ COUTTOLENC
```

Yup, that's messy. But there's a pattern to it: The name of the church, a list of names, and some gunk you'll need to filter out.

A reasonable output format is fairly clear. You probably want it to look something like:

```
Obra de Clerigos en Ayuda Solidaria, Adalberto Sandoval Acevedo
Obra de Clerigos en Ayuda Solidaria, Jesus Carlos Cabrero Romero
Obra de Clerigos en Ayuda Solidaria, Oscar Flores Ramirez
Obra de Clerigos en Ayuda Solidaria, Oscar Roberto Dominguez Couttolenc
...
```

Or, to write it more generally:

```
<Clean church name>, <Clean member name>
```

This is what you hope to take to your colleague before she needs to file her story.

---

## Hold me back!

**Warning:** The rest of the lesson will be covered in person. If you are attending the Hacks/Hackers DC meetup, please stop here. If you can't make it, rock on!

---

## Writing some pseudo-code

First, find a partner to work with. Pair programming is, paradoxically, often more efficient than working in isolation. 

Hopefully, you've carefully studied the [source data](data/MC_por_SGAR-trimmed.txt). 

Now, get out that highly advanced technology called paper and pen (a word processor will work too) and write down human-language instructions about how you would process the data. Think about how you would explain it to someone who had to do it by hand.

Before reading further, take 15 minutes to write down how you'd process and clean the data. 

Got it? Great. Read on to see how I tackled the problem.

### Step 0

"Open" the file. For a human, that means just looking at it. You'll worry about how a machine opens the file when you get to the code.

* **Step 0:** Open the file.

### Step 1

For this data set, there's some gunk at the top of the file that comes from the PDF header:

```
DIRECTORIO DE MINISTROS DE CULTO
POR CLAVE DE REGISTRO SGAR

12/02/2016
Total: 76210

Dirección General de
Asociaciones Religiosas

```

Hey, there's the first data processing step: Skip the gunk at the top.

Since you need to be very clear in your instructions, you should put a finer point on it: Since there are exactly 9 lines of junk, skip the first 9 lines of the file.

* **Step 0:** Open the file.
* **Step 1:** Skip the first 9 lines of the file.

### Step 2

Now that you've written instructions to open the file and skip the first 9 lines, it seems like it's about time to start cleaning up the data. But not so fast! First, you need to make sure the instructions specify a place to put the cleaned data. 

* **Step 0:** Open the file.
* **Step 1:** Skip the first 9 lines of the file.
* **Step 2:** Prepare a place to write down the clean data.

(To be continued)
