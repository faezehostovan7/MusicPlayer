import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame


Win = tk.Tk()
Win.title('Music Player')
Win.geometry('500x400')
Win.config(bg = 'white')

pygame.mixer.init()

song_list = tk.Listbox(Win, width = 60, bg = '#54ffeb', fg = 'black')
song_list.pack(pady = 20)

def add_song():
    songs = filedialog.askopenfilenames(initialdir = 'C:/faezeh program/music', title = 'Add Music', filetypes = (('mp3 Files', '*.mp3'),))
    for song in songs:
        songs = song.replace('C:/faezeh program/music/', '')
        song_list.insert(END, songs)

def play_song():
    song = song_list.get(ACTIVE)
    song = f'C:/faezeh program/music/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_song():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

global paused
paused = False
def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def play_next_song():
    next_song = song_list.curselection()
    next_song = next_song[0] + 1
    song = song_list.get(next_song)
    song = f'C:/faezeh program/music/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    song_list.selection_clear(0, END)
    song_list.selection_set(next_song, last = None)

def play_previos_song():
    next_song = song_list.curselection()
    next_song = next_song[0] - 1
    song = song_list.get(next_song)
    song = f'C:/faezeh program/music/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    song_list.selection_clear(0, END)
    song_list.selection_set(next_song, last = None)
    
frame = tk.Frame(Win, bg = 'white')
frame.pack()

play_button = tk.Button(frame, text = 'play', padx = 10, pady = 10, bg = 'blue', command = play_song)
pause_button = tk.Button(frame, text = 'pause', padx = 10, pady = 10, bg = 'blue', command = pause_song)
stop_button = tk.Button(frame, text = 'stop', padx = 10, pady = 10, bg = '#FFFF00', command = stop_song)
next_button = tk.Button(frame, text = 'next', padx = 10, pady = 10, bg = 'blue', command = play_next_song)
previos_button = tk.Button(frame, text = 'previos', padx = 10, pady = 10, bg = 'blue', command = play_previos_song)

play_button.pack(side = LEFT, padx = 5)
pause_button.pack(side = LEFT, padx = 5)
stop_button.pack(side = LEFT, padx = 5)
next_button.pack(side = LEFT, padx = 5)
previos_button.pack(side = LEFT, padx = 5)

add_song_btn = tk.Button(Win, text = 'Add songs', padx = 10, pady = 3, bg = '#FF5400', command = add_song)
add_song_btn.pack(pady = 20)
Win.mainloop()