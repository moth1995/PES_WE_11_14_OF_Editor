# PES/WE OF Editor 2011-2014
A simple tool to edit the saga game option file

Hi guys! 


## What can be done with this editor?

### Players:

- Edit stats, special abilities, basic settings, appearance, motion settings, growth type, etc
- Export/import players from/to a csv file, very useful to move players between versions of pes/we
- Copy/Paste from/to PSD, you can paste the data from the site https://pesstatsdatabase.com/ and also you can copy the data from the current player in the style of psd so you can paste this data again over another players

### Teams:

- Make transfers of players between all the teams, i have tested the logic and seems to be all fine, but in case you notice any unusual/undesire behaviour, please report it and tell me how should it be
- Edit dorsals
- Edit kits configuration thanks to @YERRY11 for most of the code and logic to read this data, without him wont be possible

### Clubs:

- Edit names, supporter colour, flag assigned, and more data

### Stadiums:

- Change names

### Leagues:

- Change names

### Logos:

- Import/Export from/to PNG indexed and with a palette of 16 colours

## How to configure faces and hairs folder​

    You need to create a folder, you can put the name that you can, example "PES14 FACES HAIRS", inside there you have to create two new folders "faces" and "hairs", inside them you have to place your faces and hairs files, the name that you put to the bin is really important because that will determinate the face and hair ids, this a example of the logic, lets say that inside faces folder you have the following files:
    unknown_01521, unknown_01522, unknown_01523,
    the tool will assign the ids on this way
    1 -> unknown_01521
    2 -> unknown_01522
    3 -> unknown_01523

    and so on, the same logic applies to hairs, it will always depends on the names, so be careful with that
    Then you go into the menu edit -> select faces/hairs folder you choose your folder and also if your bins are from ps2 or psp

## IMPORTANT
File extension for faces and hairs files must ALWAYS be .bin or .str otherwise the files will be ignore by the tool


## Compatibility notes:

>If your OF is from PS2 you will be able to use any OF being decrypted or encrypted (default), for PSP only decrypted and if im not wrong the one from 3DS is only decrypted from all the test I've made so that's the only format and works fine

## Super important... ALWAYS MAKE A BACKUP OF YOUR FILE!!!​

## Download: https://github.com/moth1995/PES_WE_11_14_OF_Editor/releases/latest



## Thanks and credits

@PeterC10 without his base code to decrypt and encrypt the option file this won't even be possible, also he manage to map the growth type which is really useful, a big part of the existance of the tool.

@YERRY11 for the help with the kit configuration and the importing/exporting of images into the option file, really a big part of the doing of this editor

Compulsion for the excellent base of his pes fan editor made in java which helped me to create my own in python
@adams06 who had the idea of the PSD Copy

Gerardo Canalla who provided me PS2 option files

Kratos82 who provided me 3DS option files