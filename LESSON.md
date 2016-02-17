# Lesson

This exercise is meant to be as similar to a real world data cleaning task as possible. That means that in addition to writing some Python code, you'll be doing some command line work and using Git. 

I've had to take just a few shortcuts due to some limitations of Python Anywhere, which I will note throughout the lesson. 

What seems like the biggest shortcut -- I prepared the skeleton of the code for you already -- isn't a shortcut in the real world at all. I *always* start data projects with a data processing template. I often develop it to a point I can pass it off to another developer who can handle the task but shouldn't have to worry about weird system and Python quirks. 

If you need to do this kind of work, you're probably going to be spending a lot of time studying and modifying other people's code.

## The problem

A reporter at your publication would like you to clean up some data for a story about fringe religious groups in Mexico. She doesn't need anything fancy, just an overall count of the number of groups in the country and a count of the number of members per group.

The good news is that Mexican government has collects and releases data about known religious groups. The not-so-good news is that instead of a friendly CSV file that you could import into Excel, the data is locked up in a [1,964 page PDF document](http://www.asociacionesreligiosas.gob.mx//work/models/AsociacionesReligiosas/pdf/Numeralia/MC_por_SGAR.pdf).

You could try to copy and paste and manually clean up the data, but that's a lot of work. Who wants to do a lot of work? More importantly, you'll have even *more* work if you make a mistake, and if the government releases a new list, you'll have more work still. But if you write some code to clean the data, you can repeatedly process the data. With a little code, mistakes are no longer time-killers. If new data is released, you can simply swap out the old data for the new and re-run your analysis.

## The starting point

