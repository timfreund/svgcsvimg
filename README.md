SVG + CSV = IMG
===============

Overview
--------

This is a command line utility that generates a set of PNG images from
an SVG template and data provided in a CSV file.

Variable names are determined from the first row of the CSV file, and
the file *must* contain a 'filename' column.  The resulting PNG images
are created using the CSV supplied filename.

Use Cases
---------

I built this tool because I was too lazy to manually create intro 
slides for a series of videos.  I made the slide template, put all
of the video metadata into a csv file, and then spent two hours hacking
out this little project.  It's true, I could have manually created
all of those slides in that time, but then I wouldn't have this code
to give away.

My general rule of thumb is to do something manually once.  If it comes
up a second time, I will manually complete the task and write down the
steps with an eye toward repeatable automation.  Then I'm ready to write
up code when that third time comes around.  I had twenty slides to produce,
so I jumped straight to step three for this project.

Problems
--------

Does your text render as a solid rectangle?  There is a bug in the way
the rsvg library handles flowable elements that triggers this behavior.
Converting flowable text to single line is a (painful) workaround. 
Alternative SVG -> PNG rendering ideas will be entertained.



