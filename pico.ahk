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

#if (getKeyState("F19", "P"))
F19::return

z::
Run, C:\Users\Kavin\Desktop\pico\deej.exe
return

a::msgbox, a
b::msgbox, b
c::msgbox, c
d::msgbox, d
e::msgbox, e
f::msgbox, f
g::msgbox, g
h::msgbox, h

#if