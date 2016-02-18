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

## Describe how you're going to process the data

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

### Step 3

This is where things start to get interesting. This isn't a single step as much as a process that needs to be repeated, over and over. 

So, in step 3, your instructions should specify that the person processing the data should read line by line and make some decisions. Let's take a closer look at the data again:

```
SGAR/2:3/13 OBRA DE CLERIGOS EN AYUDA SOLIDARIA
Nombre Completo
ADALBERTO SANDOVAL ACEVEDO

Total
4

JESUS CARLOS CABRERO ROMERO
OSCAR FLORES RAMIREZ
OSCAR ROBERTO DOMINGUEZ COUTTOLENC
SGAR/2/92 CONFERENCIA DEL EPISCOPADO MEXICANO
Nombre Completo
ABELARDO ALVARADO ALCANTARA

Total
159

ADALBERTO ALMEIDA MERINO
ADOLFO ANTONIO HERNANDEZ HURTADO
ADOLFO ANTONIO SUAREZ RIVERA
ADOLFO M. CASTA?O FONSECA
ALEJO ZAVALA CASTRO
ALFONSO CORTES CONTRERAS
ALFONSO HINOJOSA BERRONES
ALFONSO HUMBERTO ROBLES COTA
ANCELMO ZARZA BERNAL
ANTONIO GONZALEZ SANCHEZ
ANTONIO ORTEGA FRANCO
ANTONIO SAHAGUN LOPEZ
ARTURO A. SZYMANSKI RAMIREZ
ARTURO LONA REYES
BENJAMIN CASTILLO PLASCENCIA
BENJAMIN JIMENEZ HERNANDEZ
BRAULIO RAFAEL LEON VILLEGAS
CARLOS AGUIAR RETES
CARLOS GARFIAS MERLOS
CARLOS QUINTERO ARCE
CARLOS SUAREZ CAZARES
CARLOS TALAVERA RAMIREZ
CONSTANCIO MIRANDA WECKMANN
DOMINGO DIAZ MARTINEZ
EDUARDO CARMONA ORTEGA
EMILIO CARLOS BERLIE BELAUNZARAN
ENRIQUE DIAZ DIAZ
ERNESTO CORRIPIO AHUMADA
ESTANISLAO ALCARAZ FIGUEROA
FABIO MARTINEZ CASTILLA
FAUSTINO ARMENDARIZ JIMENEZ
FELIPE AGUIRRE FRANCO
FELIPE ARIZMENDI ESQUIVEL

www.asociacionesreligiosas.gob.mx

Página 1
```

There are three key patterns in the data to be aware of. 

1. The name of the religious group always precedes the names of the registered members.
2. The line with the name of the group always starts with the letters `SGAR` followed by some letters, numbers, and a space before the name of the group.
3. In addition to the names of the members, there's some junk strewn about the file: The agency's URL, the page number, a header before the names that says "Nombre completo", a line that says "Total", empty lines, and a line with a number corresponding to the total.

These patterns pretty much spell out what needs to happen. For each line:

* If the line starts with SGAR, get the stuff after the space and write it down as the current religious group.
* If the line matches any of the junk you identified, skip it and move on to the next one.
* If none of the conditions above are met, the line must be a name. Write down the name along with the current religious group.

Let's put it together into detailed instructions:

* **Step 0:** Open the file.
* **Step 1:** Skip the first 9 lines of the file.
* **Step 2:** Prepare a place to write down the clean data.
* **Step 3:** Read the file, line by line:
    * If the line starts with SGAR, write down the name after the first space as the current religious group. Take care to fix the capitalization of the group's name so it is more readable.
    * Skip the line if it:
        * Says 'Total'.
        * Says 'Nombre completo'.
        * Says 'www.asociacionesreligiosas.gob.mx'.
        * Starts with 'Pàgina'.
        * Is a number.
        * Is blank.
    * Otherwise, write down the current line and the current religious group on the clean data sheet. Take care to fix the capitalization of the name so it is more readable.

### Step 4

It might seem obvious, but the final step is to give back the cleaned data. You wouldn't want someone to do all that work and then forget to share it with you!

* **Step 0:** Open the file.
* **Step 1:** Skip the first 9 lines of the file.
* **Step 2:** Prepare a place to write down the clean data.
* **Step 3:** Read the file, line by line:
    * If the line starts with SGAR, write down the name after the first space as the current religious group. Take care to fix the capitalization of the group's name so it is more readable.
    * Skip the line if it:
        * Says 'Total'.
        * Says 'Nombre completo'.
        * Says 'www.asociacionesreligiosas.gob.mx'.
        * Starts with 'Pàgina'.
        * Is a number.
        * Is blank.
    * Otherwise, write down the current line and the current religious group on the clean data sheet. Take care to fix the capitalization of the name so it is more readable.
* **Step 4:** Return the cleaned data.

## From pseudo-code to Python code

At this point, you have what programmers call "pseudo-code". It isn't real code that a computer can understand, but it does systematically describe the process your program needs to use. That's important. Once you know what you're trying to do, it will be a lot easier to ask Google (or your friends and colleagues) for help. 

Eventually, you probably won't need to write pseudo-code when you process data. But it *never* hurts to describe the patterns in your input data or your desired output. I still do this for just about any relatively complex task I need to tackle and it's absolutely essential for the trickier data cleaning and parsing tasks that come up from time to time.

This is the part where I introduce you to my patented pedagogical technique, tested with many an aspiring coder (just ask NPR's interns), in which I dangle you out the window by your ankles and then let go! 

Ok, I'm mostly kidding. What I am going to do is introduce a lot of programming concepts, but narrowly or shallowly. Some people want to understand the whole system before they get started. In my experience, that works great for a small number of people and rather poorly for most people (myself included). For me, there's a back-and-forth, practice-based process. 

If I understand enough concepts to get something working, even if I don't understand all of it, that's perfect. As I keep working, the concepts start to deepen and become more real, and then I can keep adding new wrinkles to my practice and taking on new challenges.

If you're one of those people who needs to and can understand a system comprehensively before diving in, this lesson probably isn't for you (and I'm insanely jealous -- how do you do it?!?!). This lesson is for you if you like to make things that work, no matter how rickety, with limited knowledge and clever Googling, and build your skills through practice.

## Reading the structure of the script

As mentioned above, your colleague left you a place to start. Before you start to sing your colleague's praises (I *do* appreciate the flattery), remember that's both a blessing and a curse. It's useful because it means there's some work and structure you don't have to worry about. It can be frustrating to try to figure out what's going on and how to change it to suit your needs.

First, you need to take a look at the overall structure of the [processing script](process.py). Here's a modified version of file with most of the code stripped away so you can see the structure better:

```python
def process():
   """
   Process the data
   """
   output = list()
   # processing code
   return output

if __name__ == '__main__':
   output = process()
   print(output)
```

The first part, `def process():`, defines a function. A function is sort of like a little machine that takes some action. In this case, that's processing the data, which is why the function is named `process`. Note that you could have named the function just about anything you want (provided it doesn't include whitespace), but giving the function a weird name like `bojangles` would be like naming a bicycle "Labrador Retriever" -- confusing to everyone.

In all events, everything that is indented underneath `def process():` is part of that function. The function ends when there's a line that begins with `return` or a non-idented line.

The second part, `if __name__ == '__main__':` looks really weird. That's because it really weird. To be honest, I'm not really sure why the people who made Python thought that was a cool pattern; it certainly took me a long time to understand it. 

But just trust me on this one. Everything indented underneath that line will be executed when you run the script, either via PythonAnywhere's "run" button or from the command line (something we might be able to cover later).

That's why there's a line that reads `output = process()` in that section. It can help to read that line right-to-left. On the right side, you're executing the function called `process()` -- you're asking the little machine to do something for you. On the left side, you're assigning the output of the `process()` function to a variable called `output`. 

A variable is just a way of storing assigning a name to some piece of data. The data could be alphanumeric characters ("Hacks/Hackers DC"), a whole number (50), a decimal number (35.5), a list of multiple pieces of data (["Seattle", "Chicago", "New York City"]). It turns out there are many *types* of data that can be stored with a variable. For this lesson, we'll be mostly worried about *strings* (a sequence of letters and numbers) and *lists* (a way of storing multiple pieces of data).

Just like the function named `process`, you *could* call the variable just about anything you want. But in programming, clarity trumps creativity. (Tangentially, keeping track of stuff that *you* name, versus stuff that is just built-in, is one of the great challenges and confusing parts of programming for newcomers.)

In all events, the key idea to keep in mind is that the function is where you put the processing code. The `__name__ == '__main__'` block is where you execute the processing code and see what it did.

Finally, did you notice the lines that start with `#` or multiple-line blocks that start and end with `"""`? Those are comments, which don't mean anything in terms of instructing the computer; they are simply notes to yourself or others who might use the code.

## Started at the bottom... 

You might think you want to start at the top, but that's pretty rarely the case. The first step, for the moment, is to modify the section at the bottom to give you more useful information about what the heck is actually going on. Then you can start editing the `process()` function to crunch the data.  

Go ahead and open the file called process.py via the files tab on Python Anywhere.

Here's what that code at the bottom looks like now:

```python
if __name__ == '__main__':
    # Print start message.
    print('It works! Running `process_data()`')

    # Assign return values of `process_data()` function to `output` variable.
    output = process_data()

    # Print the `output` variable.
    print('Here is the first line of output data:')
    print('    {0}'.format(output[0]))
    print('See you in class!')

    # Print that we're done.
    print('Done.')
```

Edit the code to cut out some of the example debugging message and to print the whole output variable:

```python
if __name__ == '__main__':
    # Assign return values of `process_data()` function to `output` variable.
    output = process_data()

    # Print the `output` variable.
    print('Output of process_data function:')
    print(output)
```

Sweet! That's a little easier to read, and is going to provide you with much more valuable feedback when you run your program.

Try running it now to see what happens. You should see a very lightly processed version of the original data, minus blank lines. This will help give you some insight into what's happening in the `process()` function currently.

## ...Now we're processing

Now, take a look at the processing function that's here for you to modify. It doesn't seem very useful just yet, but at least it takes care of a few of the steps from your pseudo-code:

```python
def process_data():
    """
    Process data.
    You must modify this function to shape the data the way you need.
    """

    # Make an empty list to hold the processed data.
    output_list = list()

    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()

    # Loop over each line of the data file. Each time the loop runs, the current
    # line is assigned to a variable called `line`.
    for line in data:

        # Remove any whitespace characters from beginning and end of line
        line = line.strip()

        # If the line is not empty, add it to the output
        if line != '':
            output_list.append(line)

    # Return the processed data
    return output_list
```

The first significant lines of the function are:

```python
    # Make an empty list to hold the processed data.
    output_list = list()
```

Hmmm, where have you seen that before? Oh yeah, it was one of the steps in processing the data! Step 2, to be specific. It's not quite in same order as the pseudo-code, but nobody's perfect. 

Really, the first few steps could really be in any order -- just like in real life, it doesn't matter if you open the file before or after you get out a pad of paper to record the cleaned data, it just matters that you make sure you do both before starting to clean the data.

The next few lines correspond nicely to the pseudo-code from earlier as well:

```python
    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()
```

You don't have to entirely understand what's going on these lines to see that that I've assigned the contents of the data file to a variable called `data`. Make a mental note of this -- if you want to change the data file, you'll need to remember it -- but move on. You've got a variable called `data` to play with and unless you run into problems, how you got it doesn't matter that much.

Next up is a processing loop that looks at each line of the file, just as the great oracle of pseudo-code predicted:

```
    # Loop over each line of the data file. Each time the loop runs, the current
    # line is assigned to a variable called `line`.
    for line in data:

        # Remove any whitespace characters from beginning and end of line
        line = line.strip()

        # If the line is not empty, add it to the output
        if line != '':
            output_list.append(line)
```

You'll be digging into this more in just a moment. Clearly, this doesn't do everything you need it to, but it gives you a pattern to start building off.

The last two lines are especially important to understand: If the line is not empty (`!=` is how you saw "not equals" in Python and several other programming languages), then `append` the line to the `output_list` variable defined earlier.

And finally:

```python
    # Return the processed data
    return output_list
```

Excellent! You can scratch a few items off the list:

* ~~**Step 0:** Open the file.~~
* **Step 1:** Skip the first 9 lines of the file.
* ~~**Step 2:** Prepare a place to write down the clean data.~~
* **Step 3:** Read the file, line by line:
    * If the line starts with SGAR, write down the name after the first space as the current religious group. Take care to fix the capitalization of the group's name so it is more readable.
    * Skip the line if it:
        * Says 'Total'.
        * Says 'Nombre completo'.
        * Says 'www.asociacionesreligiosas.gob.mx'.
        * Starts with 'Pàgina'.
        * Is a number.
        * Is blank.
    * Otherwise, write down the current line and the current religious group on the clean data sheet. Take care to fix the capitalization of the name so it is more readable.
* ~~**Step 4:** Return the cleaned data.~~

Even though there's code in place to read the file line-by-line, without skipping the first lines of the file and applying all that complicated logic, we can't really say we've accomplished step 3.

The first thing you need to do is skip the first 9 lines of the file. Helpfully, the file as been loaded a list -- each element of the list corresponds to a line in the file. Because the data is a list, you can loop over it. You can also use Python's handy "slice" syntax. To slice off the first 9 items of the list, you can do something like `mylist[9:]`.

Edit the file to add a new `trimmed_data` variable and loop over *that*.

```python
    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()

	trimmed_data = data[9:]

    # Loop over each line of the data file. Each time the loop runs, the current
    # line is assigned to a variable called `line`.
    for line in trimmed_data:
	
    	...
```

Now you can scratch step 1 off the list as well. 

* ~~**Step 1:** Skip the first 9 lines of the file.~~

That leaves step 3, where the real action happens. Before you dig in, might as well run the script again. What do you expect to see compared to the first time you ran it? 

If you said "the same dang thing but without the first nine lines" then you're absolutely correct! 

As I write code, I tend to make these sorts of small changes, think about what I expect to see in the output, and then run the program to make sure the output is in fact what I expected. If it isn't, then either my expectation is wrong or my code is wrong -- and it's usually my code. Running your code early, often, comparing what you expect with what actually happens is a nice recipe for learning quickly and writing solid, mistake-free code.

On to step 3, or at least a first pass at it!

Let's walk through what's there more closely and then modify it.

First is the loop itself:

```python
    for line in trimmed_data:
```

Everything "inside" the loop (e.g. indented after this line of code) will operate on each element of the `trimmed_data` list. `line` is just a temporary name for the element being processed. Like function names and variable names, it can be anything you want. What's important here is consistency: Inside the loop, `line` will always refer to the line from the source file that's being processed.

---

**Aside**: If that makes sense, go ahead and skip this note. If not, here's an example that might help. Executing:

```python
cities = ['NYC', 'Chicago', 'Detroit']
for city in cities:
    print(city)
```

will print:

```
NYC
Chicago
Detroit
```

This code is, despite using `GO_SEAHAWKS_WHOO` instead of `city` as the loop variable, will do the exact same thing:

```python
cities = ['NYC', 'Chicago', 'Detroit']
for GO_SEAHAWKS_WHOO in cities:
    print(GO_SEAHAWKS_WHOO)
```

This code, however, will fail with an error:

```python
cities = ['NYC', 'Chicago', 'Detroit']
for city in cities:
    print(GO_SEAHAWKS_WHOO)
```

---

The next bit of code, `line = line.strip()` pops up in just about every data cleaning scenario. `"   Hacks/Hackers DC ".strip()` returns `"Hacks/Hackers DC"`. The `strip()` method simply removes any whitespace characters from the beginning and end of a string.

```python
    for line in trimmed_data:

        # Remove any whitespace characters from beginning and end of line
        line = line.strip()

        # If the line is not empty, add it to the output
        if line != '':
            output_list.append(line)
```

You're finally in the belly of the data-cleaning beast. If you'll recall, the once you're looking at the data line by line, the first test you need to run is if the line starts with "SGAR". How might you do this in Python? You'll need to rewrite a bit more code this time to make it all work:

```python
    for line in trimmed_data:

        # Remove any whitespace characters from beginning and end of line
        line = line.strip()

        # If the line is not empty, add it to the output
        if line.startswith('SGAR'):
            line_parts = line.split(' ', 1)
            identifier = line_parts[0]
            group_name = line_parts[1]
        elif line != '':
            output_list.append([group_name, identifier, line])
```

Now, your code checks to see if the line starts with SGAR. If it does, you'll need to do some processing magic. The `split()` method turns a string into a list but "splitting" on a given character, like a space or comma. The first argument to the method is a separator (`' '` in our case), and the second argument specifies how many times to apply the split before stopping. 

---

**Aside**: Splitting can be confusing. If my vague and confusing explanation wasn't sufficient, using an interactive Python console might help. Try splitting one of the lines of the data. First try it without the second argument:

```python
>>> 'SGAR/2/92 CONFERENCIA DEL EPISCOPADO MEXICANO'.split(' ')
['SGAR/2/92', 'CONFERENCIA', 'DEL', 'EPISCOPADO', 'MEXICANO']
```

Getting close, but you only want to split the identifier and the name of the religious group, not all the words in the name of the group.

```python
>>> 'SGAR/2/92 CONFERENCIA DEL EPISCOPADO MEXICANO'.split(' ', 1)
['SGAR/2/92', 'CONFERENCIA DEL EPISCOPADO MEXICANO']
```

Perfect! Element 0 of the returned list is the identifer, and element 1 is the name of the religious group. 

---

Like `strip()`, you'll find yourself using `split()` all the time when doing data cleaning work.
