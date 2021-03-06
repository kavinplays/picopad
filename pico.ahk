#NoEnv 
SetWorkingDir %A_ScriptDir% 
Menu, Tray, Icon, shell32.dll, 190

#WinActivateForce
SetKeyDelay, -1, -1
SetWinDelay, -1 
SetControlDelay, -1

SendMode Input
#InstallKeybdHook
#UseHook On
#SingleInstance force 
;i don't know about any of the above code i have used it from taranvh's guide at https://github.com/TaranVH/2nd-keyboard

#if (getKeyState("F19", "P")) ;all commands under here work only when the F19 key is pressed down
F19::return ;this needs to be done or the program glitches out

z:: ;this opens deej as deej cannot run before the pico is connected so running it at startup like the ahk script does not work
Run, C:\Users\Kavin\Desktop\pico\deej\deej.exe ;change C:\Users\Kavin\Desktop\pico\ to the location where the files are saved
return

a::msgbox, button1 ;opens a messagebox(alert box) and states the button which has been pressed
b::msgbox, button2 ;change these to actually usefull ahk commands
c::msgbox, button3
d::msgbox, button4
e::msgbox, button5
f::msgbox, button6
g::msgbox, button7
h::msgbox, button8

#if
