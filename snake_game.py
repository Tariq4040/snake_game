from pygame import * #this will import everything inside the pygame module
import pygame
import random


# oper wali 2 lines likhne k sath sath hm pylint ko uninstall b kre ge tb hi
#  error remove ho ga

# Color Define for Our Window.....and also Snake and its Ground.....
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
#pip install pygame-->>this module is used to create the game,basic module
# import pygame   #but es trha se error ata h uncomment kr k daikh skte h ap

# basics Variables

width=400       #height of Window
height=400      #width of  Window
fps=30
exit_game=False
game_over=False
snake_x = 50            #snake setting on x_axis
snake_y = 50            #snake setting on y_axis
snake_size = 20         #snake Size setting
val_x=0
val_y=0
# snake_food_x=100        #snake food Place setting on x_axis,but below we generate randomaly
snake_food_x=random.randint(0,width)
# snake_food_y=100        #snake food Place setting on y_axis
snake_food_y=random.randint(0,width)
snake_food_size=20      #snake food Size setting
score=0
snake_list = []
snake_length=1

# Now we Initializing the Pygame module......

pygame.init() #Initializing pygame here....
pygame.mixer.init()  #game me voice ko import krne k lea......
wind = pygame.display.set_mode((width,height))  #window seting.
pygame.display.set_caption("Snake Game By M.Tariq Ahmad") #game title....
clock_var = pygame.time.Clock()
def Sreen_Text(text,color,x,y):
    font_text = pygame.font.SysFont('Time New Roman,arial',25)
    screen_text = font_text.render(text,True,blue)
    wind.blit(screen_text,(x,y))

def snake_plot(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,(x,y,snake_size,snake_size))

while not exit_game:
    if game_over:
        wind.fill(white)
        Sreen_Text("Game Over",blue,150,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              exit_game=True

        clock_var.tick(fps)
        pygame.display.update()


    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    val_x = 0
                    val_y = -5  #yahan pe y-axix(oper move mtlb +ve me move krne k lea 
                                #value ko hm -ve m le ge
                if event.key == pygame.K_DOWN:
                    val_x = 0
                    val_y = 5   #yahan pe y-axix(neche move mtlb -ve me move krne k lea, 
                                #value ko hm +ve m le ge

                if event.key == pygame.K_LEFT:
                    val_x = -5   #yahan pe x-axis(left move mtlb -ve me move krne k lea, 
                                #value ko hm -ve m le ge
                    val_y =0

                if event.key == pygame.K_RIGHT:
                    val_x = +5   #yahan pe x-axis(right move mtlb +ve me move krne k lea, 
                                #value ko hm +ve m le ge
                    val_y = 0
        
        snake_x=snake_x + val_x
        snake_y= snake_y + val_y

        if abs(snake_x - snake_food_x)<5 and abs(snake_y - snake_food_y)<5:
            score = score+10
            # print(score)  me print ni krwana chahta blk,window scereen pe show krna chahta hn
            # es lea Sreen_Text() ko neche define kr rha hn
            snake_food_x=random.randint(0,width)
            snake_food_y=random.randint(0,width)
            snake_length = snake_length+5



        head=[]
        head.append(snake_x)        
        head.append(snake_y)
        snake_list.append(head) 

        if len(snake_list)> snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over=True

        if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
            game_over=True      



        wind.fill(black)
        Sreen_Text("Your Score : " + str(score),white,50,10)
        snake_plot(wind,green,snake_list,snake_size)
        # pygame.draw.rect(wind,green,(snake_x,snake_y,snake_size,snake_size)) #snake code on window
        #snake food code on window below
        pygame.draw.rect(wind,red,(snake_food_x,snake_food_y,snake_food_size,snake_food_size))
        
        clock_var.tick(fps)
        pygame.display.update()

pygame.quit()
quit()
