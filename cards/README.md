# The other side up

Double-sided informal [visiting card(s)](https://en.wikipedia.org/wiki/Visiting_card). Full-size [images below](https://github.com/isaacbernat/presentations/tree/master/cards#full-size-images).

## Side A
![Side A notes reference](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideA_notes.png)
### Element description
#### 0-3 Screen
##### 0 Frame:
Original plastic colour from an [SVGA](https://en.wikipedia.org/wiki/Super_VGA) monitor (the first one I ever owned!).
##### 1 Margin:
Space between the projected screen image and the border of the frame. The margin in the picture was further darkened (not only 100% black, but also other [CMYK colours](https://en.wikipedia.org/wiki/CMYK_color_model)). This is so the printed card better represents the real contrast with the neighbouring sections.
##### 2 Curvature:
The glass on the front panel of the [CRT screen](https://en.wikipedia.org/wiki/Cathode-ray_tube) is curved, not flat. It's clearly seen when compared to the lower plastic frame variable width (thicker at the corner (near `0`) than at the middle section (near `5`)).
##### 3 Reflection:
`IsaacBernat` text is reflected on the surface. This is despite materials, angle, texture... are not optimised for that purpose.

#### 4-6 Pathname
##### 4 Repository:
This is how [git repositories](https://en.wikipedia.org/wiki/Git) are represented in my zsh terminal. `RepositoryName git:(BranchName)`. That path is printed on each line, to indicate the user's location within the file system.
##### 5 Brightness:
The image was post processed so that `IsaacBernat` colour was white. This increases the perceived brightness on printed paper. I wanted no ink to be used there, because the original background colour looks shinier. The effect is subtle. It highlights the most important part of the card (the name) without being too obvious. The path is shown twice to reinforce the relevant part of the message (and is also consistent with real terminal usage).
##### 6 Branch:
The default `master` branch is used. Pun intended. It implies Isaac Bernat's skill level on git is that of a master ^_^ .

#### 7-C Command
##### 7 Name:
[cowsay](https://en.wikipedia.org/wiki/Cowsay) is a 1999 perl program that generates [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) of a cow and a text message using a [speech balloon](https://en.wikipedia.org/wiki/Speech_balloon).
##### 8 Arguments:
`-d` represents a dead cow. It uses `X` for eyes. Also used `-fsmall`, to have a smaller version suitable for a card, but didn't add it here, as it took too much space.
##### 9 Parameter:
`0xDEADBEEF` is a 32-bit [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) number (equivalent to 3735928559). It can also be read as "dead beef", which would be a pun on the "dead cow" represented below in ASCII art. The number [originally had other meanings](https://stackoverflow.com/questions/2907262/what-does-dead-beef-mean), and was used in systems like the classic Mac OS as a [magic debug value](https://en.wikipedia.org/wiki/Magic_number_(programming)#Debug_values).
##### A Bang bang!‼:
`‼` takes the space of one character, but it looks like two `!!`. I thought it was fun :D .
##### B ASCII people:
Using [ASCII characters](https://ss64.com/ascii.html) like `☻` or `☺`, there's the image of a person giving a card to another. That could be you and me B-) .
##### C Recursion:
The command is somewhat [self-referential](https://en.wikipedia.org/wiki/Self-reference). By running `cowsay -fsmall -d cowsay -d 0xDEADBEEF‼` in a terminal one gets the result shown below, which is similar to the text in the speech balloon `cowsay -d 0xDEADBEEF‼`.
```
 _________________________
< cowsay -d 0xDEADBEEF‼ >
 -------------------------
       \   ,__,
        \  (xx)____
           (__)    )\
            U ||--|| *
```

#### D-F Content
##### D Font selection:
Used `IBM CGAthin`, [available here among many others](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_cgathin). The font selected was a thin one because the pictures were taken in a dark environment (to reduce the glass reflection of the camera taking the picture). Therefore, white pixels were so bright that would overwhelm surrounding areas too (a clear example is the size of the eyes or mouth of those 2 heads (`☻` vs. `☺`). They should be the exact same size, but are not). Reducing the exposure time to diminish the glow effect was not viable either, since the raster pattern/scan lines were too obvious and the rows lightning uneven at the 60hz screen [refresh rate](https://en.wikipedia.org/wiki/Refresh_rate). An acceptable compromise was achieved using this font.
##### E Scale:
The size of each [logical pixel](https://en.wikipedia.org/wiki/Pixel#Logical_pixel) was enlarged (so it would use several physical pixels). This was because taking the picture in its 1:1 size, the result would display individual [RGB subpixel](https://en.wikipedia.org/wiki/Pixel#Subpixels) colours and their shadow mask patterns. The result did not display white colour as desired, but instead red, green and blue circles on a black background, which was not the desired effect. The larger scale also makes the curvature more apparent (a feature of CRT screens).
##### F Special thanks:
To [Nicolau Suárez Olalla](https://nsuarez.com/), for photography and post-processing.


## Side B
![Side B notes reference](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideB_notes.png)
### Element description
##### 0 Support:
3½-inch [floppy disk](https://en.wikipedia.org/wiki/Floppy_disk#3%C2%BD-inch_disk) (aka _Micro diskette_, _Micro disk_, or even _Micro floppy_). Not a fancy render of a save icon ^_^U
##### 1 Source:
Image taken from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Floppy_disk_300_dpi.jpg). Part of [Wikimedia Foundation](https://en.wikipedia.org/wiki/Wikimedia_Foundation) a project I support and you should too!
##### 2 Dimensions:
I wanted the representation of the disk to be 1:1, as close as possible to the real size (90mm × 94mm). Even if that meant cropping the borders (card dimensions are smaller). The image source resolution is 300 dpi, the same as the print, so no image re-scaling or quality loss here.
##### 3 HD
Not the best medium for HD videos... but it doesn't stand for [High Definition](https://en.wikipedia.org/wiki/High-definition_video). It means High-Density (even [Ultra High-Density in 1986](https://books.google.es/books?id=rDwEAAAAMBAJ&pg=PA19&redir_esc=y#v=onepage&q&f=false) yet it wouldn't hold a single second of a 8k UHD video). Marketed as "1.44 MB" it really holds 1440 KiB. So that should be 1.47 MB decimal megabyte (MB) or 1.41 MiB binary mebibyte (MiB), but marketing teams know how to compromise irreconciliable positions :D
##### 4 Arrow
This way in ↑.

<div><img align="left" src="https://web.archive.org/web/20220728035111im_/https://pbs.twimg.com/media/FDQ9SQ6XMAAcuF3?format=png&name=small"/></div>

##### 5 Label
Or rather ¿ʃǝqɐ⅂? If "INDEX" is to be used as a one-line title/summary for its contents, it makes more sense to store the diskettes with the metallic part facing the bottom of the containter/box. This way, the visible border already contains the text to be searched for (not the metallic part), making it more easily acessible, requiring less space and movement to shuffle through floppies. But since these labels are stickers, if it fits... that's often as much thought anybody would give... could've benefited from a _"the other side up"_ note :D

← A good example of practicality is the archiver on the left, image courtesy of [archive.org](https://archive.org/), another cool project to support ^_^

##### 6 The other side up
What's the front and what's the back? _"This side up"_ would only be helpful when one is already holding the correct side... a bit ironic, not when that information is needed the most. Since information here is written and this is not to be inserted into a floppy drive, the other side holds more important information. Better turn it around to read the contact name ^_^
##### 7 Metal!
Including a shutter in its design, meant the smallest possible size was no longer square. This had the advantage that one could not introduce the disk sideways by mistake. So it served more uses than just protection. An intuitive design always trumps text labels as showcased in [The Design of Everyday Things](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things) in greater detail. But most importantly, the shutter was fun to pull and watch it return to the original position :D

## Full-size images
### Side A
![Side A](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideA_86x55.png)

### Side B
![Side B](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideB_86x55.png)

### Technical details
- The printed resolution is 300 dpi.
- The size 86x55mm is larger than the physical card. It includes "safety margins" required by the printer.
