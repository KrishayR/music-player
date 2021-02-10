from pygame import mixer
from tkinter import Tk, Label, Button, filedialog
from tkmacosx import Button
#vars
current_vol = float(0.5)
#funcs
def play_song():
    filename = filedialog.askopenfilename(title='Please select your music file')
    current_song = filename
    song_title = filename.split('/')
    song_title = song_title[-1]
    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_vol)
        mixer.music.play()
        song_title_lab.config(fg='#f79579',text='Now playing:' + str(song_title))
        volume.config(fg='#f79579',text='Volume: '+ str(current_vol))
    except Exception as e:
        print(e)
        song_title_lab.config(fg='red',text='Error playing track')
        
def reduce_volume():
    try:
        global current_vol
        if current_vol <=0:
            volume.config(fg='#f79579',text='Volume: Muted')
            return
        current_vol -= float(0.1)
        current_vol = round(current_vol,1)
        mixer.music.set_volume(current_vol)
        volume.config(fg='#f79579',text='Volume: '+str(current_vol))
    except Exception as e:
        print(e)
        song_title_lab.config(fg='red',text="Track hasn't been selected yet")
def increase_volume():
    try:
        global current_vol
        if current_vol >=1:
            volume.config(fg='#f79579',text='Volume: Max')
            return
        current_vol += float(0.1)
        current_vol = round(current_vol,1)
        mixer.music.set_volume(current_vol)
        volume.config(fg='#f79579',text='Volume: '+str(current_vol))
    except Exception as e:
        print(e)
        song_title_lab.config(fg='red',text="Track hasn't been selected yet")
def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_lab.config(fg='red',text="Track hasn't been selected yet")
def play():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_lab.config(fg='red',text="Track hasn't been selected yet")
#main screen
root = Tk()
root.title('Music Player')
root.config(bg='#cce6e1')
#labels
Label(root,text='Music Player',font=('MuseoModerno',50),fg='#425df5',bg='#cce6e1').grid(sticky='N',row=0,padx=120)
Label(root,text='Please select a music file to play',font=('MuseoModerno',20),fg='#7A8DF8',bg='#cce6e1').grid(sticky='N',row=1)
Label(root,text='Volume',font=('MuseoModerno',20),fg='#7A8DF8',bg='#cce6e1').grid(sticky='N',row=4)
song_title_lab = Label(root,font=('MuseoModerno',20),fg='#7A8DF8',bg='#cce6e1')
song_title_lab.grid(sticky='N',row=3) 
volume = Label(root,font=('MuseoModerno',20),fg='#7A8DF8',bg='#cce6e1')
volume.grid(sticky='N',row=5)
#buttons
Button(root,text='Select Music', font=('MuseoModerno',20),fg='#7A8DF8',bg='#CCEEFF',command=play_song).grid(sticky='N',row=2)
Button(root,text='Pause', font=('MuseoModerno',20),fg='#7A8DF8',bg='#CCEEFF',command=pause).grid(sticky='E',row=3)
Button(root,text='Play', font=('MuseoModerno',20),fg='#7A8DF8',bg='#CCEEFF',command=play).grid(sticky='W',row=3)
Button(root,text='-', font=('MuseoModerno',20),fg='#7A8DF8',bg='#CCEEFF',command=reduce_volume).grid(sticky='W',row=5)
Button(root,text='+', font=('Museo Moderno',20),fg='#7A8DF8',bg='#CCEEFF',command=increase_volume).grid(sticky='E',row=5)


root.mainloop()
