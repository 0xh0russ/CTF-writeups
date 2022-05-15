# \[Web\] - Lamb Sauce

#### Points = 117

## Prompt

where's the lamb sauce
`https://lamb-sauce.tjc.tf/`

by kfb

#### Hints

\[None\]

## Provided Files

\[None\]

## Write Up

- Simple web page with an embedded youtube video.
	![webpage|500](../images/tjctf-2022/ramsey.png)
- There are no clues in the video itself.
- As always the #1 step is to view the page src.
	- the page src has this comment 
	`<!-- <a href="/flag-9291f0c1-0feb-40aa-af3c-d61031fd9896.txt"> is it here? </a> -->`
- Looks like tha path to the flag so we append this to the linke we already have.
	- `https://lamb-sauce.tjc.tf//flag-9291f0c1-0feb-40aa-af3c-d61031fd9896.txt`
	- flag found

## Flag

tjctf{idk_man_but_here's_a_flag_462c964f0a177541}