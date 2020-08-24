---
Title:Producing Beamer slide shows from markdown using Pandoc
Date: 2020-06-06
Modified:2020-06-20
category: Blog
Tags: Pandoc,slides,markdown
Slug: beamer-slides-using-markdown-and-pandoc
Summary: Short note on bueatiful Producing Beamer slide shows from markdown using Pandoc
---
# Producing slide shows with pandoc
Pandoc is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library.

You can use pandoc to produce an HTML + JavaScript slide presentation that can be viewed via a web browser. There are five ways to do this, using [S5](https://meyerweb.com/eric/tools/s5/), [DZSlides](http://paulrouget.com/dzslides/), [Slidy](https://www.w3.org/Talks/Tools/Slidy2/), [Slideous](https://goessner.net/articles/slideous/), or [reveal.js](https://revealjs.com/). You can also produce a PDF slide show using LaTeX [`beamer`](https://ctan.org/pkg/beamer), or slides shows in Microsoft [PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) format.

Here’s the Markdown source for a simple slide show, `Demo.md`:

```md
---
title:
- AI Playground
author:
- Ashwin Kumar K
theme:
- Copenhagen
date:
- March 22, 2020

---



# What's AI?

- Artificial Intelligence- The ability of machine to think and behave like humans.
- How does the machine learn on its own? - That is called Machine Learning. ML is the study of computer algorithms that improve automatically with experience.
- Just like humans learn with experience - Machines also learn with experience!
- Examples of common AI? Alexa, Siri, Google Home, Self Driving Cars, Robots etc.

# What's out there?

![Verticles](img/Untitled.png)


# How do computers make decisions?

- Conditional statements are used to perform different actions based on different conditions.
- In many programming languages, decisions (also called conditionals) take the form of an if-then construct. They start with a condition, which is then evaluated as either True or False.

# How do computers make decisions?

![Flow chart](img/Untitled 1.png){ width=250px }

# Let's Build that

​```jsx
Bot.send("Are you going out to play?")
async function respond(inputText){
	if (inputText == "yes"){
		Bot.send("Wear a hat");
	}
	else {
		Bot.send("ok");
	}

 }
\```     <REMOVE THE \>

What we learned. - Bot.send() method - if else statements.

# Build a basic greetings bot

![Flow chart](img/Untitled 2.png)



# Benefits of AI Playground

- Streamlines a lot of back end operations, so that the you can just learn what AI is — and can get immediate results!
- User friendly!
- Designed to suit students needs.
- Students can see and publish new projects and thus learn from each other.

## How does learning AI help?

- Logical reasoning and Sequencing 
- Critical thinking
- Problem solving
- Mental Mathematics
    - The above skills are implicit skills that students learn along with AI. And this helps them in academics, life, etc.

# Extra 

The well known Pythagorean theorem $x^2 + y^2 = z^2$ was  proved to be invalid for other exponents. 
Meaning the next equation has no integer solutions:
$$x^n + y^n = z^n$$

Can AI, help find near misses for this equation?
    
```
The slides generated from this markdown can bee seen [here](https://ashwinschronicles.github.io/pdfs/Demo.pdf)

You can create a slide show broken up into sections by using the # and ## heading tags (you can also create a new slide without a header using a horizontal rule (---). You can also insert latex equations by going to math mode (Insert the equation in $ $ )

To produce an HTML/JavaScript slide show, simply type

```
pandoc -t FORMAT -s Demo.txt -o Demo.html
```

where `FORMAT` is either `s5`, `slidy`, `slideous`, `dzslides`, or `revealjs`.



To produce a PDF slide show using  LaTeX [`beamer`](https://ctan.org/pkg/beamer),  type

```
pandoc -t beamer Demo.txt -o Demo.pdf
```

Note that a reveal.js slide show can also be converted to a PDF by printing it to a file from the browser.

To produce a Powerpoint slide show, type

```
pandoc Demo.txt -o Demo.pptx
```

## Structuring the slide show

By default, the *slide level* is the highest heading level in the hierarchy that is followed immediately by content, and not another heading, somewhere in the document. In the example above, level-1 headings are always followed by level-2 headings, which are followed by content, so the slide level is 2. This default can be overridden using the [`--slide-level`](https://pandoc.org/MANUAL.html#option--slide-level) option.

The document is carved up into slides according to the following rules:

- A horizontal rule always starts a new slide.
- A heading at the slide level always starts a new slide.
- Headings *below* the slide level in the hierarchy create headings *within* a slide.
- Headings *above* the slide level in the hierarchy create “title slides,” which just contain the section title and help to break the slide show into sections. Non-slide content under these headings will be included on the title slide (for HTML slide shows) or in a subsequent slide with the same title (for beamer).
- A title page is constructed automatically from the document’s title block, if present. (In the case of beamer, this can be disabled by commenting out some lines in the default template.)

These rules are designed to support many different styles of slide show. If you don’t care about structuring your slides into sections and subsections, you can just use level-1 headings for all each slide. (In that case, level-1 will be the slide level.) But you can also structure the slide show into sections, as in the example above.

Note: in reveal.js slide shows, if slide level is 2, a two-dimensional layout will be produced, with level-1 headings building horizontally and level-2 headings building vertically. It is not recommended that you use deeper nesting of section levels with reveal.js.

## Incremental lists 

By default, these writers produces lists that display "all at once". If you want your lists to display incrementally (one item at a time), use the `-i`{.literal} option. If you want aparticular list to depart from the default (that is, to display incrementally without the `-i`{.literal} option and all at once with the `-i`{.literal} option), put it in a block quote:

```
> - Eat spaghetti
> - Drink wine

```

In this way incremental and nonincremental lists can be mixed in a
single document.


## Styling the slides 

To style beamer slides, you can specify a beamer “theme” or “colortheme” using the `-V` option:

```bash
pandoc -t beamer Demo.txt -V theme:Warsaw -o Demo.pdf
```




for more settings visit  [Pandoc Manual](https://pandoc.org/MANUAL.html) and [bookdown.org](https://bookdown.org/yihui/rmarkdown/beamer-presentation.html) 

