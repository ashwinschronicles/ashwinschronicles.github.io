Generativeart

* **Download the Latest Processing 3 Release for Linux**
* **Double-Click on Package and Extract Processing into /tmp**

**Relocate Processing into System Folder**
(For a Local installation without Admin Privileges install into Home…)
Setting the **SuperUser as Owner**



```bash
sudo chown -R root:root /tmp/processing*
```

Switch the Processing directory



```bash
sudo mv /tmp/processing* /opt/processing
```

If Got “User is Not in Sudoers file” then see: [How to Enable sudo](https://tutorialforlinux.com/2012/03/05/linuxsudoerrorisnotinthesudoersfile/)

Again **Add Processing to Ubuntu Path**
By making a Symlink:



```bash
sudo ln -s /opt/processing/processing /usr/local/bin/processing
```

Or Locally by:

```
ln -s /opt/processing/processing /home/magcig/.local/bin/processing
```

Snippet

```
"hype setup": {
  "prefix": "hype_setup",
  "body": [
    "void setup(){",
    "	size(${1:640},${2:640}${3:,P3D});",
    "	H.init(this).background(#${4:202020})${5:.use3D(true)}${6:.autoClear(${7:true})};",
    "	smooth();",
    "",
    "	",
    "}",
    " ",
    "void draw(){",
    "	H.drawStage();${8:",
    "",
    "	${9:// }saveFrame(\"frames/#########.tif\"); if (frameCount == 900) exit();}",
    "}"
  ],
  "description": "hype setup"
}
```

[https://snippet-generator.app/?description=hype+setup&tabtrigger=hype_setup&snippet=void+setup%28%29%7B%0A%09size%28%24%7B1%3A640%7D%2C%24%7B2%3A640%7D%24%7B3%3A%2CP3D%7D%29%3B%0A%09H.init%28this%29.background%28%23%24%7B4%3A202020%7D%29%24%7B5%3A.use3D%28true%29%7D%24%7B6%3A.autoClear%28%24%7B7%3Atrue%7D%29%7D%3B%0A%09smooth%28%29%3B%0A%0A%09%0A%7D%0A+%0Avoid+draw%28%29%7B%0A%09H.drawStage%28%29%3B%24%7B8%3A%0A%0A%09%24%7B9%3A%2F%2F+%7DsaveFrame%28%22frames%2F%23%23%23%23%23%23%23%23%23.tif%22%29%3B+if+%28frameCount+%3D%3D+900%29+exit%28%29%3B%7D%0A%7D&mode=vscode](https://snippet-generator.app/?description=hype+setup&tabtrigger=hype_setup&snippet=void+setup(){ size(%24{1%3A640}%2C%24{2%3A640}%24{3%3A%2CP3D})%3B H.init(this).background(%23%24{4%3A202020})%24{5%3A.use3D(true)}%24{6%3A.autoClear(%24{7%3Atrue})}%3B smooth()%3B 	 } + void+draw(){ H.drawStage()%3B%24{8%3A 	%24{9%3A%2F%2F+}saveFrame("frames%2F%23%23%23%23%23%23%23%23%23.tif")%3B+if+(frameCount+%3D%3D+900)+exit()%3B} }&mode=vscode)