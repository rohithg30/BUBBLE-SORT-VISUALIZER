import pygame
import random
import math
pygame.init()


class Drawinformation:
    BLACK=0,0,0
    WHITE=255,255,255
    GREEN=0,255,0
    RED=255,0,0
    GREY=128,128,128
    BLUE=0,0,255
    background_color=WHITE
    sidepad=100
    toppad=150
    FONT=pygame.font.SysFont('Cuckoo',30)
    LARGE_FONT=pygame.font.SysFont('Long Island',40)


    greens=[(46, 182, 44),(87, 200, 77),(131, 212, 117)]
    grays=[(128,128,128),(160,160,160),(192,192,192)]
   
    


    def __init__(self,width,height,lst):  # set up Window of pygame 
        self.width=width
        self.height=height 

        self.window=pygame.display.set_mode((width,height))
        pygame.display.set_caption("Visualize Sorting Algorithm")
        self.set_list(lst)

    def set_list(self,lst):

        self.lst=lst
        self.min_val=min(lst)
        self.max_val=max(lst)

        self.block_width=round((self.width-self.sidepad)/len(lst))
        self.block_height=math.floor((self.height-self.toppad)/(self.max_val -self.min_val))
        self.start_x=self.sidepad//2


def generate_starting_list(n,minval,maxval):    # generate random integers into list 

    lst=[]
    for _ in range(n):
        val=random.randint(minval,maxval)
        lst.append(val)
    return lst



    




def draw(drawinfo,algo_name,ascending):    # which makes color to Window

    drawinfo.window.fill(drawinfo.background_color)

    title=drawinfo.LARGE_FONT.render(f"{algo_name}-{'Ascending' if ascending else'Descending'}",2,drawinfo.BLUE)
    drawinfo.window.blit(title,(drawinfo.width/2-title.get_width()/2,5))

    controls=drawinfo.FONT.render("R-Reset | A-ascending | D-Descending | SPACE- START",1,drawinfo.BLACK)
    drawinfo.window.blit(controls,(drawinfo.width/2-controls.get_width()/2,55))
    sorting=drawinfo.FONT.render(" ",1,drawinfo.BLACK)
    drawinfo.window.blit(sorting,(drawinfo.width/2-sorting.get_width()/2,85))
    drawlst(drawinfo)
    pygame.display.update()



def drawlst(drawinfo,color_pos={},clear_bg=False):
    lst=drawinfo.lst

    if clear_bg:
         clear_rect=(drawinfo.sidepad//2,drawinfo.toppad,drawinfo.width-drawinfo.sidepad,drawinfo.height-drawinfo.toppad)

         pygame.draw.rect(drawinfo.window,drawinfo.background_color,clear_rect)
    
    for i,val in enumerate(lst):
         x=drawinfo.start_x + i*drawinfo.block_width
         y=drawinfo.height-(val-drawinfo.min_val)*drawinfo.block_height

         if i in color_pos:
             color=color_pos[i]

         color=drawinfo.greens[i%3]
         pygame.draw.rect(drawinfo.window,color,(x,y,drawinfo.block_width,drawinfo.height))
    if clear_bg:
        pygame.display.update()


def bubblesort(drawinfo,ascending=True):

    lst=drawinfo.lst
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1=lst[j]
            num2=lst[j+1]
            
            if num1>num2 and ascending or num1<num2 and not ascending:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                drawlst(drawinfo,{j:drawinfo.GREEN,j+1:drawinfo.RED},True)
                yield True
    return lst


def main():
    run=True
    clock=pygame.time.Clock()
    minval=0
    maxval=100
    n=50
    lst=generate_starting_list(n,minval,maxval)
    draw_info=Drawinformation(1100,900,lst)
    ascending=True
    sorting =False

    sorting_algorithm=bubblesort
    sorting_algo_name="Bubble Sort"
    sorting_algorithm_generator=None

    while run:
        clock.tick(80)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting=False
        else:
            draw(draw_info,sorting_algo_name,ascending)
        pygame.display.update()
        
        for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 run=False
             if event.type!=pygame.KEYDOWN:
                 continue
             if event.key==pygame.K_r:
                 lst=generate_starting_list(n,minval,maxval)
                 draw_info.set_list(lst)
                 sorting =False
             elif event.key==pygame.K_SPACE and not sorting:
                 sorting=True
                 sorting_algorithm_generator=sorting_algorithm(draw_info,ascending)
             elif event.key==pygame.K_a and not sorting:
                 ascending=True
             elif event.key==pygame.K_d and not sorting:
                 
                 ascending=False

                 


    pygame.quit()
if __name__=="__main__":
    main()
   




