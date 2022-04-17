import cv2
import numpy as np
import math

ons = np.ones([3000,3000,3])* 255 #세로, 가로
x,y,c = ons.shape


class map_hint:

    def cvtpointer(self,Angle,c):
        r = self.r
        Angle += r
        Angle = math.radians(Angle)
        se = c * math.cos(Angle)

        ga = c * math.sin(Angle)
        return se,ga

    def re_point(self,s,g):
        rosx = self.rosx
        rosy = self.rosy
        s = rosy + s
        g = rosx + g

        return s,g

    def hit_input(self,image,x,y, color = [0,255,0]):
        sub_color = [0,0,255]
        image[x,y] = color


        image[x,y+1] = sub_color
        image[x+1,y] = sub_color

        image[x,y-1] = sub_color
        image[x-1,y] = sub_color

        return image


    def axis_run(self,c,r):
        ro = r

        self.ro += ro
        ro = self.ro
        Angle = math.radians(ro)
        se = c * math.cos(Angle)

        ga = c * math.sin(Angle)



        self.r = ro

        rosx = self.rosx
        rosy = self.rosy

        s = rosy + se
        g = rosx + ga

        self.rosx = g
        self.rosy = s


    def __init__(self,x,y): #최초 보정값
        self.rosx = x
        self.rosy = y
        self.r = 0
        self.ro = 0

def tutorial():

    #튜토리얼
    #--------------------------------------------------------------

    ons = np.ones([3000,3000,3])* 255 #도화지 크기 설정 (세로, 가로) 가장 중요!!(이거 너무 작게 만들면 나중에 에러코드 뜸)
    x,y,c = ons.shape

    #--------------------------------------------------------------
    '''
    하얀색의 백지 생성

    '''
    #--------------------------------------------------------------
    hitori = map_hint(500,500)
    #--------------------------------------------------------------
    '''
    맵 좌표 시작점 생성
    '''


    i = 0
    kt = True
    lgu =0

    while True:

        w,h = hitori.cvtpointer(270,250) #츠정 각도와 측정된 거리 입력
        #삼각함수를 이용해서 각도와 빗변을 이용해 밑변과 높이 구하기

        s,g = hitori.re_point(w,h)# 이전 함수에서 빗변과 높이 입력
        #현재 맵에 입력을 위해 좌표계에 맞춰 값 변환

        #=============
        s = int(s)
        g = int(g)
        #부동소수점을 자연수로 변환
        #=============


        ons = hitori.hit_input(ons,s,g) #맵과 좌표를 입력
        #이미지에 그리기

        #===============================
        w,h = hitori.cvtpointer(90,250)
        s,g = hitori.re_point(w,h)
        s = int(s)
        g = int(g)
        ons = hitori.hit_input(ons,s,g)
        #===============================


        i += 0.5


        if i > 1800:
            break
        if i > 900 and lgu < 90: # 특정값에 맞추어 회전
            lgu += 1

            print("tun_up", lgu)
            hitori.axis_run(5,1) # 직진 거리와 회전각도 입력
        else:
            hitori.axis_run(1,0) # 위와 같음



        print('run : ', i, "x : ", g, "y : ", s)

    cv2.imwrite("test_map.png",ons) # 이미지 저장