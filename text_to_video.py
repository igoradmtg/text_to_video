# -*- coding: utf-8 -*-
import os
from moviepy.editor import *
from moviepy.editor import TextClip,VideoFileClip, concatenate_videoclips

dir_name = "" 
dir_output = ""
fnamemp4 = "File.mp4"
fnamegif = "File.gif"
text_site = "https://github.com/igoradmtg" # Intro and outro text 
font_name_intro = "ttf/font3.ttf"
#font_name = "Y:/html/_python/slideshow04/ttf/CursedTimerUlil-Aznm.ttf"
font_name = "ttf/font6.ttf"
duration_intro = 2 # Duration of the text clip 

fontsize_intro = 30 # Font size for intro and outro 
fontsize_text = 20
Video_type = 5 # Video Resolution  1 - 720х480, 2 - 854x480, 3 - 1280x720, 4 - 1920x1080,  5 - 3840x2160
W = 720 # Default clip width 1280
H = 480 # Default clip height 720 
#W = 1280
#H = 720
    
DW = 1 # 1 - Up  2 - Down
DH = 1 # 1 - Left 2 - Right
K_W_H = W / H # Width and height ratio  1920 / 1080 = 1,77777
SIZE = (W, H) # Video size 
CHANGE_DIRECTION = True # Change direction
    
def intro() :
    global text_site, SIZE, fontsize_intro, duration_intro
    logo1 = (TextClip(txt=text_site,color="#0000AA", align='West',fontsize=fontsize_intro,font = font_name_intro).set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
    logo1_clip = CompositeVideoClip([logo1.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255])  
    logo2 = (TextClip(txt="present",color="#0000AA", align='West',fontsize=fontsize_intro,font = font_name_intro).set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
    logo2_clip = CompositeVideoClip([logo2.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255])  
    return concatenate_videoclips([logo1_clip,logo2_clip])
  
def outro(start_time) :
    global text_site, SIZE, fontsize_intro
    logo1 = (TextClip(txt=text_site,color="#0000AA", align='West',fontsize=fontsize_intro,font = font_name_intro).set_duration(duration_intro).margin(right=8, top=8, opacity=0).set_pos(("center","center"))) # (optional) logo-border padding.set_pos(("right","top")))
    logo1_clip = CompositeVideoClip([logo1.fadein(0.5,initial_color=[255,255,255]).fadeout(0.5,final_color=[255,255,255])], size=SIZE, bg_color = [255,255,255]).set_start(start_time)  
    return logo1_clip


def text_clips(ar_texts) :
    clips = []
    clips.append(intro())
    max_number = len(ar_texts)
    #print(max_number)
    start_clip = duration_intro*2 # Начало вывода клипа после интро
    time_for_number = 2.8 # Time for string
    max_duration = max_number * time_for_number # Max time
    clips.append(outro(max_duration+start_clip))
    i=1
    for text in ar_texts:
        clip1 = (TextClip(txt = text, color='red', align='West', fontsize=fontsize_text, font = font_name)
            .set_start((i-1)*time_for_number + start_clip)
            .margin(right=8, top=8, opacity=0)
            #.set_duration(time_for_number).set_pos(("center","center")))
            .set_duration(max_duration - (i-1) * time_for_number)
            .set_pos(("center",(i-1)*60))
            .crossfadein(.5))
             
        clips.append(clip1)
        i+=1
    return clips
        

def save_clip() :
    global dir_name, fnamemp4 , SIZE , dir_output
    ar_texts = [
        "<Lorem Ipsum is simply dummy text>",
        "<of the printing and typesetting industry.>",
        "<Lorem Ipsum has been the industry's>",
        "<standard dummy text ever since the 1500s,>",
        "<when an unknown printer took a galley>",
        "<of type and scrambled it to make>",
        "<a type specimen book.>"]
    #max_number = 24 # Количество цифр
    #for i in range(1,max_number+1): 
    #    ar_texts.append("Text "+str(i))
    clips = text_clips(ar_texts)    
    final_clip_f2 = CompositeVideoClip(clips, size=SIZE, bg_color = [255,255,255])         
    #final_clip_f2.write_videofile(os.path.join(dir_output, fnamemp4), fps=30, threads=4, audio = False)
    final_clip_f2.write_gif(os.path.join(dir_output, fnamegif), fps=10)

def main() : 
    global dir_name, fnamemp4, dir_output, Video_type
    save_clip()
  
if __name__ == "__main__":
    main()  
  