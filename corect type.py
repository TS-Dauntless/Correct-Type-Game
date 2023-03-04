import pygame
import random
from math import ceil

# variable Declarations

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]  # Defining Alphabets(a to z)

letter = ""  # letter that is used to display in the Screen randomly

is_answer_correct = None  # to display colors when the user giving correct and wrong answers

score = 0  # Number of correct answers by player

round_counter = 0  # Total number of rounds(gets initialized in level_init() function)

color_time_counter = 0  # to display Selected color for limited second (also used to dim that color)

total_round = 0  # to see in which round the player is?

timer_counter = 0  # to see the remaining second in the screen (we get sec when divided by frame rate and ceil it)

max_timer_sec = 0  # to define total number of second in which we see as Timer (get initialized in level_init function)

is_display_level_screen = True  # to Display Easy, Medium and Hard to get input from Player

is_beginning_of_game = True  # to indicate it's first time to start of the game to display brief information about game

mouse_pos_x = -1  # to get x axis of mouse (only used when selecting the levels)

mouse_pos_y = -1  # to get x axis of mouse (only used when selecting the levels)

is_answer_time_over = None  # to get timer reach 0 to conclude that the answer time is over to display a yellow color

FRAME_RATE = 14  # Overall game's frame rate(fps)


# Initializing Pygame
pygame.init()  # (to use pygame library in our game)

# Creating Pygame window
screen = pygame.display.set_mode((800, 600))  # Creating window for our game in 800 * 600 px

# Giving Title and Icon
pygame.display.set_caption("Correct Type")  # Title of our game


# Function Block
def level_init(level):

    """
    To initialize the total_round, maximum time to answer a question
    according to which level player is selected
        If the player selected Easy
            total round = 10 rounds
            maximum time = 5 seconds
        If the player selected Medium
            total round = 15 rounds
            maximum time = 1 seconds
        If the player selected Hard
            total round = 10 rounds
            maximum time = 5 seconds
    """

    global total_round, max_timer_sec, is_display_level_screen

    if level == "Easy":
        total_round = 10
        max_timer_sec = 5

    elif level == "Medium":
        total_round = 15
        max_timer_sec = 3

    elif level == "Hard":
        total_round = 20
        max_timer_sec = 1

    is_display_level_screen = False
    key_pressed(None)


def display_level_screen():

    """
    To Display Easy, Medium and Hard Screen to let player know that they should select the level
    It display Easy, Medium and Hard text and
    a background HighLighter according to the mouse position to indicate the player
    (Level can either be selected using mouse or keyboard keys)
    """

    if 0 <= mouse_pos_x <= 800:
        if 0 <= mouse_pos_y <= 200:
            pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(0, 0, 800, 200))
        elif 200 <= mouse_pos_y <= 400:
            pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(0, 200, 800, 200))
        elif 400 <= mouse_pos_y <= 600:
            pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(0, 400, 800, 200))

    text = pygame.font.Font("freesansbold.ttf", 20).render("Use Mouse or Press the First Letter of the Word to Select",
                                                           True, (200, 200, 200))
    center = text.get_rect(center=(400, 15))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 50).render("Easy", True, (0, 0, 0))
    center = text.get_rect(center=(400, 100))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 50).render("Medium", True, (0, 0, 0))
    center = text.get_rect(center=(400, 300))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 50).render("Hard", True, (0, 0, 0))
    center = text.get_rect(center=(400, 500))
    screen.blit(text, center)


def check_for_e_m_h_input(event_):

    """
    To see the player Pressed E or M or H
    (only used when Display Level screen is Active)
    """

    if event_.key == pygame.K_e:
        level_init("Easy")
    elif event_.key == pygame.K_m:
        level_init("Medium")
    elif event_.key == pygame.K_h:
        level_init("Hard")


def next_letter():

    """
    to Get the Next Letter (First letter if letter variable is Empty) in letter variable
    (it do not get the same letter continuously)
    """

    global letter
    temp = []
    for alphabet in alphabets:
        if alphabet != letter:
            temp.append(alphabet)
    letter = random.choice(temp)


def show_letter():

    """
    to show the letter in the letter variable
    """

    text = pygame.font.Font("freesansbold.ttf", 500).render(letter, True, (0, 0, 0))
    center = text.get_rect(center=(800 / 2, 600 / 2))
    screen.blit(text, center)


def if_alphabet_pressed(event_):

    """
    to see if any alphabets is pressed and
    if any alphabet is pressed by player it calls key_pressed() function to denote which alphabet is pressed
    """

    if event_.key == pygame.K_a:
        key_pressed("a")
    elif event_.key == pygame.K_b:
        key_pressed("b")
    elif event_.key == pygame.K_c:
        key_pressed("c")
    elif event_.key == pygame.K_d:
        key_pressed("d")
    elif event_.key == pygame.K_e:
        key_pressed("e")
    elif event_.key == pygame.K_f:
        key_pressed("f")
    elif event_.key == pygame.K_g:
        key_pressed("g")
    elif event_.key == pygame.K_h:
        key_pressed("h")
    elif event_.key == pygame.K_i:
        key_pressed("i")
    elif event_.key == pygame.K_j:
        key_pressed("j")
    elif event_.key == pygame.K_k:
        key_pressed("k")
    elif event_.key == pygame.K_l:
        key_pressed("l")
    elif event_.key == pygame.K_m:
        key_pressed("m")
    elif event_.key == pygame.K_n:
        key_pressed("n")
    elif event_.key == pygame.K_o:
        key_pressed("o")
    elif event_.key == pygame.K_p:
        key_pressed("p")
    elif event_.key == pygame.K_q:
        key_pressed("q")
    elif event_.key == pygame.K_r:
        key_pressed("r")
    elif event_.key == pygame.K_s:
        key_pressed("s")
    elif event_.key == pygame.K_t:
        key_pressed("t")
    elif event_.key == pygame.K_u:
        key_pressed("u")
    elif event_.key == pygame.K_v:
        key_pressed("v")
    elif event_.key == pygame.K_w:
        key_pressed("w")
    elif event_.key == pygame.K_x:
        key_pressed("x")
    elif event_.key == pygame.K_y:
        key_pressed("y")
    elif event_.key == pygame.K_z:
        key_pressed("z")


def key_pressed(key):

    """
    to see if player input is correct or not and
    to initialize timer counter variable to show the remaining time in the screen and
    to get next letter that is next_letter() function is called
    """

    global is_answer_correct, score, color_time_counter, round_counter, timer_counter, is_answer_time_over

    if letter != "":
        if key == letter.lower():
            if timer_counter > 0:
                score += 1
                is_answer_correct = True
            else:
                is_answer_time_over = True
        else:
            is_answer_correct = False

        color_time_counter = 0

    next_letter()
    round_counter += 1
    timer_counter = FRAME_RATE * max_timer_sec


def display_beginning_screen():

    """
    to display how to start the Game and
    to display a brief about the Game
    """

    text = pygame.font.Font("freesansbold.ttf", 60).render("Press any key to Start", True, (0, 0, 0))
    center = text.get_rect(center=(400, 200))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 30).render("Then You should click the letter when,", True,
                                                           (125, 55, 144))
    center = text.get_rect(center=(400, 400))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 30).render("that letter is displayed on the screen", True,
                                                           (125, 55, 144))
    center = text.get_rect(center=(400, 450))
    screen.blit(text, center)


def display_background():

    """
    to display the BackGround of our game window and
    to change the color when the answer is Wrong, the answer is correct and when the answer time is over
    (color change will happen only after the key is pressed from the user)

        Correct   - Green color
        Wrong     - Red color
        Time Over - Yellow color
            (color change will fade to background in one second)

    (when the answer is wrong it will display red color even when the time is over but
    when the answer is correct and the time is over it will display yellow color)
    """

    fill_color = 255 * color_time_counter / FRAME_RATE
    if is_answer_time_over is True and is_answer_correct is None:
        screen.fill((255, 255, fill_color))
    elif is_answer_correct is None:
        screen.fill((255, 255, 255))
    elif is_answer_correct is True:
        screen.fill((fill_color, 255, fill_color))
    elif is_answer_correct is False:
        screen.fill((255, fill_color, fill_color))


def small_display_score_and_round():

    """
    to display current Score and current Round when we getting input by player when they play actual game
    Current Round will display on the top left corner and
    Current Score will be displayed on the top right corner and
    the Score will be displayed as "Current Score / Total Round"
    """

    text = pygame.font.Font("freesansbold.ttf", 30).render(f"Round : {round_counter}", True, (0, 0, 255))
    screen.blit(text, (0, 0))

    text = pygame.font.Font("freesansbold.ttf", 30).render(f"Score: {score} / {total_round}", True, (0, 0, 255))
    top_right = text.get_rect(topright=(800, 0))
    screen.blit(text, top_right)


def display_score_screen():

    """
    to display Score Taken After the Actual game is Over
    It displays "Score out of Total Round" and the Procedure to Play the Game Again
    """

    text = pygame.font.Font("freesansbold.ttf", 50).render(f"Your Score is {score} out of {total_round}",
                                                           True, (0, 0, 0))
    center = text.get_rect(center=(400, 200))
    screen.blit(text, center)

    text = pygame.font.Font("freesansbold.ttf", 50).render("Press Enter to Play Again", True, (0, 0, 0))
    center = text.get_rect(center=(400, 400))
    screen.blit(text, center)


def show_timer():

    """
    To show the remaining time left for this round in the top middle
    """

    text = pygame.font.Font("freesansbold.ttf", 30).render(f"Timer : {int(ceil(timer_counter / 14))}",
                                                           True, (0, 0, 255))
    pos = text.get_rect(midtop=(400, 0))
    screen.blit(text, pos)


# Main Loop
running = True  # to define is the Game running and gets False only when the Played Quit the game

while running:

    # User Events
    for event in pygame.event.get():  # Loop to get all events by the User (Events by Keyboard, Mouse, etc.,)

        if event.type == pygame.QUIT:  # Condition to check the Your wish to Quit
            running = False  # Running loop will become False (to terminate from this while Loop)

        elif event.type == pygame.KEYDOWN:  # to check If any Key is Pressed by the Keyboard

            if is_beginning_of_game:  # If any Key Pressed Our Game will move next level so until any key Pressed
                is_beginning_of_game = False                                          # Some Content will be Displayed

            elif is_display_level_screen:  # To see if the Player sees the Levels in the screen
                check_for_e_m_h_input(event)  # To see if the player pressed E or M or H key in the KeyBoard

            elif round_counter > total_round:  # to see the Actual game ends

                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:  # to see the player inputs Enter
                    #                                                                   to move on to play the next game

                    # Resetting to some variable to the Next Game
                    letter = ""
                    score = 0
                    round_counter = 0

                    # To get the Level Screen For the Next Round
                    is_display_level_screen = True

            else:  # if the game does not in the beginning level, Choosing Difficulty level and at Result Level then
                #                             the Game must be at in the Actual Level where we need to see player events

                if_alphabet_pressed(event)  # to see if the Player Pressed the Alphabet

        elif is_display_level_screen:  # to see if the game at selecting the Level screen

            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # to get the exact mouse Position

            if event.type == pygame.MOUSEBUTTONDOWN:  # to see if any Mouse click Happens
                # to see if the mouse is inside our window and if it is inside our window, it is to see where is it
                if 0 <= mouse_pos_x <= 800:
                    if 0 <= mouse_pos_y <= 200:
                        level_init("Easy")
                    elif 200 <= mouse_pos_y <= 400:
                        level_init("Medium")
                    elif 400 <= mouse_pos_y <= 600:
                        level_init("Hard")

    # Displaying Background
    display_background()

    # Changing background color regarding to game or answers
    if is_answer_correct is not None or is_answer_time_over is not None:  # to see the input is pressed
        color_time_counter += 1  # to calculate 1 second to display color and it is also used to fade it

    if color_time_counter >= FRAME_RATE:  # to see of one sec is completed
        is_answer_correct = None    # if one sec completed it will change is_answer_correct from True or False to None
        is_answer_time_over = None  # and is_answer_time_over from True to None

    # Displaying game items
    if is_beginning_of_game:  # to see it is the Beginning of the Game
        display_beginning_screen()

    elif is_display_level_screen:  # to see it is in the selecting level's level
        display_level_screen()

    elif round_counter > total_round:  # to see if the Game Over
        display_score_screen()

    else:  # to see if the game is in the Actual Game level
        small_display_score_and_round()
        show_timer()
        show_letter()

    # Timing for Timer
    if timer_counter != 0:  # to see if the Timer Reached Zero
        timer_counter -= 1  # if the Timer Doesn't reached we need to decrease it to make the timer in the Game run

    # update window
    pygame.time.Clock().tick(FRAME_RATE)  # to tell the pygame to run this loop only FRAME_RATE times per second
    #                                                    it will pause the program run only FRAME_RATE times per second

    pygame.display.update()  # To Update the Content in the screen every time the loop runs
