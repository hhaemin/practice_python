import random
from time import sleep


class Song:
    
    def __init__(self, t, s, pt):
        self.title = t
        self.singer = s
        self.play_time = pt
        
    def printSongInfo(self):
        print(f'Title: {self.title}, Singer: {self.singer}, Play time: {self.play_time}')
        
class Player:
    
    def __init__(self):
        self.songList =[]
        self.isLoop = False
        
    def addSong(self, s):
        self.songList.append(s)
        
    def play(self):
        if self.isLoop:
            while self.isLoop:
                for s in self.songList:
                    print(f'Title: {s.title}, Singer: {s.singer}, Play time: {s.play_time}sec')
                    sleep(s.play_time)
                    # isLoop가 True이면, 무한루프에 빠짐
        else:
           for s in self.songList:
                    print(f'Title: {s.title}, Singer: {s.singer}, Play time: {s.play_time}sec')
                    sleep(s.play_time) 
                    # while문이 없으므로 songlist의 곡이 한바퀴를 돌면 실행을 멈춘다.
                    
    def shuffle(self):
        random.shuffle(self.songList)   
        
    def setIsLoop(self, flag):
        self.isLoop = flag