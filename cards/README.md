# The other side up

Double-sided informal [visiting card(s)](https://en.wikipedia.org/wiki/Visiting_card).

## Side A
![Side A](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideA_86x55.png)

## Side B
![Side B](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideB_86x55.png)

## Additional notes
### Side A
![Side A notes reference](https://github.com/isaacbernat/presentations/blob/master/cards/images/01_sideA_notes.png)

#### 0-3 Screen
##### 0 Frame:
Original plastic colour from a [SVGA](https://en.wikipedia.org/wiki/Super_VGA) monitor (the first one I ever owned!).
##### 1 Margin:
Space between the projected screen image and the border of the frame. The margin in the picture was further darkened (not only 100% black, but also other [CMYK colours](https://en.wikipedia.org/wiki/CMYK_color_model)). This is so the printed card better represents the real contrast with the neighbouring sections.
##### 2 Curvature:
The glass on the front panel of the [CRT screen](https://en.wikipedia.org/wiki/Cathode-ray_tube) is curved, not flat. It's clearly seen when compared to the lower plastic frame variable width (thicker on the corner (near `0`) than middle section (near `5`)).
##### 3 Reflection:
`IsaacBernat` text is reflected on the surface. This is despite materials, angle, texture... are not optimised for that purpose.

#### 4-6 Pathname
##### 4 Repository:
This is how git repositories are represented in my zsh terminal. `RepositoryName git:(BranchName)`. That path is printed on each line, to indicate the user's location within the file system.
##### 5 Brightness:
The image was postprocessed so that `IsaacBernat` colour was white. This increases the perceived brightness on print. I wanted no ink to be used on paper, so the natural background colour would appear to be shinier. The effect is subtle. It highlights the most important part on the card (the name) without being too obvious. The path is shown twice to reinforce the important part of message (and is also consistent with real terminal usage).
##### 6 Branch:
The default `master` branch is used. Pun intended, as it implies that Isaac's skill level on [git](https://en.wikipedia.org/wiki/Git) is that of a master ^_^ .

#### 7-C Command
##### 7 Name:
[cowsay](https://en.wikipedia.org/wiki/Cowsay) is a 1999 perl program that generates [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) of a cow and a text message using a [speech balloon](https://en.wikipedia.org/wiki/Speech_balloon).
##### 8 Arguments:
`-d` represents a dead cow. It uses `X` for eyes. Also used `-fsmall`, to have a smaller version suitable for a card, but didn't add it here, as it took too much space.
##### 9 Parameter:
`0xDEADBEEF` is a 32-bit [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) number (equivalent to 3735928559). It can also be read as "dead beef", which would be a pun on the "dead cow" represented below in ASCII art. The number [originally had other meanings](https://stackoverflow.com/questions/2907262/what-does-dead-beef-mean), and was used in systems like classic Mac OS as a [magic debug value](https://en.wikipedia.org/wiki/Magic_number_(programming)#Debug_values).
##### A Bang bang!‼:
`‼` takes the space of one character, but it looks like two `!!`. I thought it was fun :D .
##### B ASCII people:
Using [ascii characters](https://ss64.com/ascii.html) like `☻` or `☺`, there's the image of a person giving a card to another. That could be me and you B-) .
##### C Recursion:
The command is somewhat [self-referential](https://en.wikipedia.org/wiki/Self-reference). By running `cowsay -fsmall -d cowsay -d 0xDEADBEEF‼` in a terminnal one gets the result shown below, which is similar to the text in the speech balloon `cowsay -d 0xDEADBEEF‼`.
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
##### D font selection:
Used `IBM CGAthin`, [available here among many others](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_cgathin). The font selected was a thin one because the pictures were taken in a dark environment (to reduce the glass reflection of the camera taking the picture). Therefore, white pixels were so bright that would take over surrounding areas too (a clear example are the size of the eyes or mouth of these 2 heads `☻` vs `☺`. They should be the exact same size, but are not). Reducing the exposure time to diminish the glow effect was not viable either, since the raster pattern/scan lines were too obvious and the rows lightning uneven at the 60hz screen [refresh rate](https://en.wikipedia.org/wiki/Refresh_rate). An acceptable compromise was achieved with this font.
##### E scale:
The size of each pixel was enlarged (an ideal pixel would use several physical pixels). This was because taking the picture in its ideal size, the result would display individual [RGB subpixel](https://en.wikipedia.org/wiki/Pixel#Subpixels) colours and their shadow mask patterns. The result did not properly display white colour, but instead red, green and blue circles, which was not the desired effect. The bigger scale also makes the curvature more apparent (a feature of CRT screens).
##### F Special thanks:
To [Nicolau Suárez Olalla](https://nsuarez.com/), for photography and post-processing.


### Side B
- TODO

### Technical details
- The printed resolution is 300 dpi.
- The size 86x55mm doesn't correspond to the physical card. It includes "safety margins" required by the printer.
