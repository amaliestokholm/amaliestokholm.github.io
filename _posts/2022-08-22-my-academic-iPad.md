---
layout: blog
category: Blog
title: My academic iPad or how to link Zotero and Obsidian
---
# My academic iPad  or how to link Zotero and Obsidian
At one of the summer conferences, I noticed just how many people in the audience that would take their notes on an iPad during the talks. I wanted to try it out - here is my experience with it.

I got a refurbed iPad Pro as a birthday gift. I bough an Apple Pen, a Paperlike screen protector and a case for it (so I don't break it too easily).

I uninstalled most apps, changed the wallpaper, and installed my paper reference manager <a href="https://zotero.org" target="_blank" rel="noopener">Zotero</a>. And that is it. My idea is that this iPad is supposed to be a bit 'dumb' with few-to-no distractions and only a nice set-up just for reading.

<br>

---
## What is Zotero?
<a href="https://zotero.org" target="_blank" rel="noopener">Zotero</a> is a free and open-source reference manager you can use to manage bibliographic metadata and notes of research papers. From it, you can extract bibtex-entries or bibliographies of research papers rather easily.

Furthermore, Zotero has a decent built-in pdf viewer and annotator so you can take notes and highlight passages while reading the paper. This last part is what I want to use it for on my academic iPad.

<br>
## What is Obsidian?
However, I also want to easily get an overview of all of my notes on a single paper. For this I use a workflow that connects Zotero with my note-taking app <a href="https://obsidian.md" target="_blank">Obsidian</a> and saves my notes in a readable, searchable, nice-looking markdown file.

As mentioned in my post on <a href="/blog/2022/08/22/my-Obsidian/" target="_blank">my Obsidian</a>, Obsidian is a note-taking and knowledge management app that saves all of your notes in plain markdown files in a local folder. It is a free tool and because it stores the data locally in simple text files, you do not rely on a cloud-service or on keep using Obsidian for the rest of your working life. The notes will always be readable to you and you can always access them.

I use it as a repository for notes, ideas, code snippets, and lists, but there are many different ways of using it. One strength of Obsidian is the many community-driven plug-ins that adds amazing functionalities and customizations so you can design the workflow that best suits you.


<br>
## Devices and workflow
I have Zotero and Obsidian on both my work laptop and my personal laptop. The laptops synchronize the Obsidian Vault using git and the Obsidian plug-in <a href="https://github.com/denolehov/obsidian-git" target="_blank" rel="noopener">Obsidian Git</a>). This then also works as a backup for all of my notes.

For the pdf's and notes in Zotero, I use the build-in Zotero Sync. This choice makes it possible for me to synchronize with the IOS app on my iPad and therefore use it for taking notes and reading. You get up to 300 MB for free and can update to more for relatively cheap.

So the workflow is:
- when I find a paper on one of the laptops, I use the chrome extention of Zotero to add the pdf to my Zotero library.
- I then read it, highlight it, and take notes in it on my iPad.
- With two clicks in Zotero, a nicely formatted text with all my notes on this specific paper pops up inside my Obsidian Vault for easy accessing and use.

I love it!


<br>
## How I take notes on the academic iPad
As of now there is only 5 colours in the built-in Zotero Annotator. I use them for marking different things in a research paper:
- Yellow `#ffd400` are default highlights
- Red  `#ff6666`  are things that I disagree with the author of the paper on
- Green `#5fb236` marks tasks such as references I want to follow up and read or tests I want to do
- Blue `#2ea8e5` highlights things that confuse me
- Purple `#a28ae5` are important conclusions

Besides highlighting text in the paper, I will take general notes in sticky notes.

All of these highlights and notes will be saved, converted to markdown files, and become part of my Obsidian Vault. Here they get tagged and formatted based on their colours and nature, meaning I get a single nice-looking markdown file with all of my notes and references for every single paper.

This makes them easily searchable and usable with the great backlinking system in Obsidian and its network view of notes. For me, this actually makes them a lot more useful. Back when I had a more physical, non-electronic system, I rarely went through my notes from paper reviews or conferences -- but this new system has changed that.

With the Apple pencil, I can write my notes and get the handwriting converted into text using the brilliant <a href="https://support.apple.com/en-us/HT208459#:~:text=Turn%20handwriting%20into%20text%20with%20Scribble&text=In%20a%20document%2C%20tap%20Apple,the%20screen%2C%20then%20start%20writing." target="_blank" rel="noopener">Scribble function</a>, which is enabled in newer versions of iPad IOS.

With the Apple Pencil I can also draw in the paper on Zotero, however, these drawings do not get converted and saved in Obsidian. I therefore usually accompany a drawing with a sticky note (that does make it into my Obsidian Vault) so I remember that the drawing exists and can look it up if needed.

<br>

---
## More technical: Linking Obsidian and Zotero
So how do you actually link Obsidian to Zotero in order to extract your notes in a nice way?

I started out with the workflow outlined <a href="https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536" target="_blank" rel="noopener">here</a>. Here you download Obsidian and the plug-ins Better Bibtex, Zotfile, and Mdnotes and you change some of the default settings.

As I want to connect Zotero with my iPad, I did not make the set-up with a shared folder. Instead I enabled Zotero Sync. Otherwise, I followed the guide all the way to section 3.2.

Zotero had been updated from version 5 to 6 since the tutorial was posted and this basically broke section 3.2 which concerns a set-up using Zotfile to extract annotations from Zotero. 

Luckily, Zotero 6 has many of the same functionalities as Zotfile (see e.g. <a href="https://github.com/jlegewie/zotfile/pull/573" target="_blank" rel="noopener">this page</a>). Here is my version of section 3.2 (which I also posted <a href="https://forum.obsidian.md/t/zotero-zotfile-mdnotes-obsidian-dataview-workflow/15536/101?u=cassiopyas" target="_blank" rel="noopener">as a reply in the thread</a>)):

<br>
### Extraction of Notes
When you have added your notes to a paper in Zotero 6 using their annotator, you can create a note with all annotations in the PDF by right-clicking on the parent item in the items list and select `Add Note from Annotations`. (see <a href="https://www.zotero.org/support/pdf_reader#adding_annotations_to_notes" target="_blank" rel="noopener">here</a>)

Following this you can right-click on the parent item in the items list and select `Mdnotes -> Create full export note` to get the formatted output in Obsidian.

The `Create full export note` menu exports an item's metadata and its Zotero notes as a single file. For that it uses the `Mdnotes Default Template.md`, which you should edit by adding your desired metadata placeholders like done in this tutorial. Zotero notes included in this export will use a new template you need to add to the same root directory as `Mdnotes Default Template.md` called `Zotero Note Template.md`. My `Zotero Note Template.md` only contains one line
```
{%raw%}{{noteContent}}{%endraw%}
```

<br>
### Formatting the extraction of notes
The customizing of annotations can be done using note templates in the Config Editor in Zotero, like in Section 3.1. A brief link on how the Config Editor customization works can be found <a href="https://www.zotero.org/support/note_templates" target="_blank" rel="noopener">here</a> . Now you need to change 
- `extensions.zotero.annotations.noteTemplates.title`
- `extensions.zotero.annotations.noteTemplates.note`
- `extensions.zotero.annotations.noteTemplates.highlight`

<br>
### 3.2.2 Changing the Note Title
In Zotero's Config Editor, you need to change the setting  `extensions.zotero.annotations.noteTemplates.title` to change the title of the Extracted note. The default is `{%raw%}<h1>{{title}}<br/>({{date}})</h1>{%endraw%}` but as I am not interested in keeping the date, I changed it to `{%raw%}<h3>{{title}}<br/></h3>{%endraw%}`.

<br>
### 3.2.3 Editing the Annotated Comments
I want to highlight my annotated comments from parts of the main text that are highlighted. However, Mdnotes does not yet support italics or bold (In the (<a href="https://argentinaos.com/zotero-mdnotes/changelog/" target="_blank" rel="noopener">Changelog</a>) this feature is listed under "Unreleased").

In Zotero's Config Editor, you need to change the setting  `extensions.zotero.annotations.noteTemplates.note` to change the behavior of Notes/Sticky Notes
So for now I have changed it to `{%raw%}<p>[[Note]] {{highlight quotes='true'}} {{citation}}</p> <blockquote><p>{{comment}}</p></blockquote> {{if tags}} <blockquote><p><b>Tags:</b> #{{tags join=' #'}}</p></blockquote>{{endif}}{%endraw%}`

Line by line:
```
{%raw%}<p>[[Note]] {{highlight quotes='true'}} {{citation}}</p>{%endraw%}
```

This adds the link Note to this comment and tells me where in the document I added this sticky note.

```
{%raw%}<blockquote><p>{{comment}}</p></blockquote>{%endraw%}
```

This adds my own note as a blockquote to separate it from the rest of the main text.

```
{%raw%}{{if tags}} <blockquote><p><b>Tags:</b> #{{tags join=' #'}}</p></blockquote>{{endif}}{%endraw%}
```

This adds another blockquote with any tags given to this note.


<br>
### 3.2.4 Changing Underlines
This I could not find the setting for.

<br>
### 3.2.5 Highlight Colors
In Zotero's Config Editor, you need to change the setting  `extensions.zotero.annotations.noteTemplates.highlight` to change the behavior of the highlight.

This is a bit more limited than before as there as of now only are 5 colours in Zotero Annotator : yellow: '#ffd400', red: '#ff6666', green: '#5fb236', blue: '#2ea8e5', purple: '#a28ae5'.

As mentioned above, my highlighting system currently is:
- yellow is a default highlight
- red is notes I disagree with the authors
- green marks interesting follow-up material
- blue highlights things that confuse me, and
- purple highlights are important conclusions.

For now I have changed the setting to this long bit 

```
{%raw%}{{if comment}} {{if color == '#ffd400'}}<p>{{highlight quotes='true'}} {{citation}}</p><blockquote><p>{{comment}}</p></blockquote> {{elseif color == '#5fb236'}}<p>{{highlight quotes='true'}} {{citation}}</p><p> - [ ] {{comment}} #task</p> {{elseif color == '#ff6666'}}<p>[[Disagreement]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote> <p>{{comment}}</p></blockquote> {{elseif color == '#2ea8e5'}}<p>[[Confusion]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote><p>{{comment}}</p></blockquote> {{elseif color == '#a28ae5'}}<p>[[Important]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote><p>{{comment}}</p></blockquote> {{else}}<p>{{highlight quotes='true'}} {{citation}}</p><blockquote><p>{{comment}}</p></blockquote>{{endif}} {{if tags}} <blockquote><p><b>Tags:</b> #{{tags join=' #'}}</p></blockquote>{{endif}} {{else}}<p>[[Highlight]]:{{highlight quotes='true'}} {{citation}}</p>{{endif}}{%endraw%}
```

Again let us go through it line by line:

```
{%raw%}{{if comment}}{%endraw%}
```

If a text comment was added to the highlight, do some of the following

```
{%raw%}{{if color == '#ffd400'}}<p>{{highlight quotes='true'}} {{citation}}</p><blockquote><p>{{comment}}</p></blockquote>{%endraw%}
```

If the color is yellow, just add a blockquote note.

```
{%raw%}{{elseif color == '#5fb236'}}<p>{{highlight quotes='true'}} {{citation}}</p><p> - [ ] {{comment}} #task</p>{%endraw%}
```

If the color is green, add a to-do item with the comment and tag the item with the label `#task`. This makes it possible to do the neat Dataview extraction in Obsidian as explained at the end of tutorial.

```
{%raw%}{{elseif color == '#ff6666'}}<p>[[Disagreement]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote> <p>{{comment}}</p></blockquote>{%endraw%}
```

If the color is red, mark the comment as `Disagreement` and add the note in a blockquote.

```
{%raw%}{{elseif color == '#2ea8e5'}}<p>[[Confusion]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote><p>{{comment}}</p></blockquote>{%endraw%}
```

If the color is blue, mark the comment as `Confusion` and add the note in a blockquote.

```
{%raw%}{{elseif color == '#a28ae5'}}<p>[[Important]]: {{highlight quotes='true'}} {{citation}}</p> <blockquote><p>{{comment}}</p></blockquote>{%endraw%}
```

If the color is purple, label the comment as `Important` and add the note in a blockquote.

```
{%raw%}{{else}}<p>{{highlight quotes='true'}} {{citation}}</p><blockquote><p>{{comment}}</p></blockquote>{{endif}}{%endraw%}
```

If the color is something else (not yet implemented), then just add the note in a blockquote.

```
{%raw%}{{if tags}} <blockquote><p><b>Tags:</b> #{{tags join=' #'}}</p></blockquote>{{endif}}{%endraw%}
```

All tags added in Zotero are added to a list

```
{%raw%}{{else}}<p>[[Highlight]]:{{highlight quotes='true'}} {{citation}}</p>{{endif}}{%endraw%}
```

If the highlight contains no notes, mark it as `Highlight`.

<br>
## Workflow
So the workflow becomes:
- Save the pdf in Zotero via a browser.
- Open the paper in Zotero on the iPad and add notes and highlights to it,
- Right-click paper and `Add Note from Annotations` on a laptop,
- Right-click paper and `Mdnotes -> Create full export note` on a laptop
- Open your Obsidian Vault and hurrah -- the file with all the metadata and your notes is now there!
