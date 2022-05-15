# \[Forensics\] - Fake Geoguesser

#### Points = 122

## Prompt

We don't do guess challs here at TJCTF, so that means no Geoguessr 😞 Since I took this photo myself, though, you can find out precisely where it was taken, and some Bonus Content™️, from my Camera Model Name to the Circle Of Confusion. Maybe you'll find a flag there?

by alliredapple

#### Hints
\[None\]

## Provided Files

[files](../../files/tjctf-2022/fake_geoguesser) - link to files

- `lake.jpg` - JPEG image of a lake

## Write Up

- Forensics challenges are guessy in the beginning so we just start with basic commands.
- first we run file to make sure its actually a JPEG:
![file|650](geo_file.png)
	- ok, checks out
- now lets see if the flag is included as a string
![file|650](geo_strings.png)
	 - this reveals our flag

## Flag

tjctf{thats_a_lot_of_metadata}