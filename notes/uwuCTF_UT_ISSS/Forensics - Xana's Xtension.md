# \[Forensics\] - Xana's Xtension

#### Points = 150

## Prompt

Oh no! The evil AI Xana is preventing me from reading the flag! Can you help?
By Aya (@Aya the Awesome on discord)

#### Hints
\[None\]

## Provided Files

- code_lyoko.txt
	- apparently a text file, i haven't looked yet but from the challenge name I'm guessing this its not really.

## Write Up

- lets first inspect what is in the text file.
	- just outputs a lot of junk. 😯
	- lets see what it is really using the file command: `file code_lyoko.txt`
		- its actually a GIF.
	- open it using xviewer, or change the extension to `.gif` so you can just click it.
		- `xviewer code_lyoko.txt`
	- we get this nice gif, here's the flag.

![image info](../images/uwuCTF_UT_ISSS/code_lyoko.gif)


## Flag

utflag{jeremy=elite_h@x0r}