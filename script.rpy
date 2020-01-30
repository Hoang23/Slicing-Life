define n = Character("Nikki", who_color="#ca03fc", what_color="#ca03fc", what_prefix = '"', what_suffix='"')
define em = Character("Emma", who_color="#fc036b", what_color="#fc036b", what_prefix = '"', what_suffix='"')
define me = Character("Me", who_color="#aaaaaa", what_color="#aaaaaa", what_prefix = '"', what_suffix='"')

### Testing inventory ###
# default points = 0
# When the variable points is not defined at game start, this statement is equivalent to:
default inventory = [] # inventory is a list?
default selected_item = None
default pc = Player(10, 1, 1, 5, 5, 5, 63, 10)

# knows to automatically look for sword from the images.rpy
default school_uniform_item = Armor("school_uniform_icon", 50, 5, 0, "outfit") # name/image, value, atk, wpn type
default pie_item = Consumable("pie_icon", 4, 2, 0)

# init python - lets us know that it is python code as opposed to renpy
# so none of these statements need a cash sign $ to prefix them
init python: 

    # "self" refers back to the original class ("Item") and the period is a break in the hierarchy.
    # "name" comes directly after that, so name is a property of "Item". 
    class Item: 
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

        # allows the inventory class to perceive the Item by item name instead of address in memory    
        def __repr__(self):
            return str(self.name)
        
        def __str__(self):
            return str(self.name)

    # self refers to inventory (As all these functions are within the Inventory class)
    class Inventory:
        def __init__(self, money=10): # he "Inventory" (self) is defined as having "10" money at initialization
            self.money = money
            self.items = []

        def buy(self, item): # We define another function: "buy" with the property of "item."
            if self.money >= item.cost: # if money contained within inventory is greater than the cost of the tiem
                self.money -= item.cost # reduce the money from inventory by the cost
                self.items.append(item) # append the item to the items list
                return True # return True (the player bought the item)
            else:
                return False # The player didn't buy the item.

        def earn(self, amount):
            self.money += amount

        # This is a function that checks to see if the item is in the inventory or not.
        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False

label start:
    $ inventory.append(school_uniform_item)
    $ school_uniform_item.equip(pc) # manually equip the uniform on game start
    $ inventory.append(pie_item)
 
    #call screen inventory_screen # call a screen
    #call prologue # call is similar to jump but returns after the call is finished
    
    scene bg_tree with fade
    pause
    "You wake up from your evening nap and head to the library"
    play music "bensound-onceagain.mp3"

    scene bg_library
    with fade

    "You see noone"

    "You let yourself in"

    show nikki surprised_back
    with dissolve
    
    pause
    
    n"... Hello?"
    
    me"Hi.. i was looking for the library assistant, I need help finding a book for my assignment"

    show nikki happy_waist at left
    with dissolve

    pause

    n"Well, you're in the right place. I can help you with that but on one condition."

    show nikki upset_waist at left with dissolve
    em"Hey Nikki!" 
    em"I can't find our finance envelope"

    show emma smile at right with easeinright
    pause

    n"Have you checked your pocket?"

    em"No way it's there"
    
    show emma embarrassed1 at right with dissolve
    pause

    em"..Ohh you're right"

    show emma embarrassed2 at right with dissolve
    
    "The girl notices you"

    em"Sorry I didn't know you were with someone"

    "You can feel her embarassment"

    em"I hope you didn't see that"

    n"Em, we need members for the club to exist, I was just about to ask him to join."

    me"Club?"
    
    show emma surprised at right
    with dissolve
    
    em"Oh he doesn't know?"

    me"Know what?"

    show emma smile at right

    em"We're part of the book club. Nikki is the president. I'm Emma, you can call me Em for short"
    
    em"We were stuffed if we couldn't get another member so it's good to have you on board" 

    n"He hasn't joined yet, I haven't even told him about what we do."

    show nikki blush_waist with dissolve
    em"Oh don't worry, who would decline the offer to join a club with such cute girls right?"



    menu: 
        "You bet. I love books!":
            show nikki happy_waist
            em"See Nikki?"
            $ choice_1 = True
            

        #  should not be rewarded for antisocial behaviour
        "Actually I have no interest":
            show emma sad at right with dissolve
            show nikki sad_waist at left with dissolve
            em"I understand"
            pause
            "Emma seems disappointed in you" 
            $ choice_1 = False

    show emma smile at right with dissolve
    em"Anyway I'm off, I don't have a free period unfortunately"
    if choice_1 == True:
        em"I'll see you again, uhh.."
    else:
        em"I hope you reconsider, uhh.."

    "She's waiting for you to introduce yourself"

    $ player_name = renpy.input("Enter your name")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Shuji"
    
    me"I'm %(player_name)s"

    n"Pleased to meet you, %(player_name)s"

    if choice_1 == True:
        em"Okay bye guys, you better come back %(player_name)s!"
        em"We have big plans"
    else:
        em"You better convince him to join Nikki, I'm sure %(player_name)s is just shy"

    # emma leaves 
    hide emma with dissolve

    n"I'll try find that book for you"

    hide nikki with dissolve

    "You spend some time thinking about the events"
    if choice_1:
        menu:
            "They're really nice, I can't wait to join the club":
                "It appears to be more than just a standard book club. I look forward to finding out."
            "They're way too excited about this book thing":
                "I kinda got caught up in it all. Let's see how it goes"

    else:
        menu:
            "I kinda regret saying no":
                "They were really excited about the possibility of me joining"
            "Reading isn't for me":
                "Nothing against those who love to read, it's just not my cup of tea" 
                "Funny enough, I'm getting a book right now however"
        

    show nikki happy_waist with dissolve

    n"Here is the book you requested for your assignment"

    python:
        book_item = Consumable("book_icon", 3, 0, 1)
        inventory.append(book_item)

    "You received a book"

    if choice_1 == True:
        "You talk more about the book club with Nikki and plan to meet again tomorrow"
    else:
        "You quickly leave after receiving the book"

    #play music "bensound-onceagain.mp3"
    scene bg_parkpath
    with fade
    pause


    "You leave the school ground"

    "Oh, look! I found ten coins!"

    menu:
        "Pick it up":
            # new
            $ pc.coin += 10
            $ current_money = pc.coin # this is a hack to make the field a global so we can use it as a dynamic string below
            "Now I have %(current_money)d coins."
        "Leave it":
            me"I'm sure someone else can make better use of it"
            pass

    "My stomach growls loudly."

    "Suddenly, I feel hungry."

    # instantiate items for the shop
    python:
        spaghetti_item = Consumable("spaghetti_icon", 3, 3, 0)
        olives_item = Consumable("olives_icon", 4, 1, 0)
        chocolate_item = Consumable("chocolate_icon", 11, -1, 1)

    menu: 
        "Go home":
            $ motivation.demotivated(1)
            $ current_motivation = motivation.motivation
            "The supermarket seems too far. I don't feel like going."
            pause
            # "Now I have %(current_motivation)d motivation."
            jump game_home
        "Head to the convenience store":
            me "I go into the store."
            # $ pass # does nothing and continues from the next line (can also put a jump statement here)

    # We redefine some of the properties of the items into global variables.
    label preshop:
        $ spaghetticost = spaghetti_item.value
        $ olivescost = olives_item.value
        $ chocolatecost = chocolate_item.value
    label shop2:
        menu shop:
            "Check my inventory":
                    call screen inventory_screen
                    jump shop2
            "Buy spaghetti for %(spaghetticost)d coins.":

                if pc.buy(spaghetti_item) == True: # $ pc.coin = pc.coin - spaghetticost (done in buy function)
                    $ inventory.append(spaghetti_item)
                    "Hey, those are uncooked. I can't eat those yet!"
                else:
                    "Not enough money... "
                    jump shop2

            "Buy olives for %(olivescost)d coins.":
                if pc.buy(olives_item) == True: # $ pc.coin -=  olivescost - done in buy function
                    $ inventory.append(olives_item)
                    me"I hate olives."
                    me"And they cost more than the spaghetti."
                    me"But at least I don't have to cook them... "
                else:
                    "Not enough money... "
                    jump shop2
                    

            "Buy chocolate for %(chocolatecost)d coins.":
                if pc.buy(chocolate_item) == True:
                    $ inventory.append(chocolate_item)
                    me"Mmmm, dark semi-sweet chocolate! My favorite!"
                else:
                    "Not enough money... "
                    jump shop2

            "Buy nothing.":
                jump game_continues

    jump game_continues

    label fallthrough:
        "Not enough money..."
        jump shop2

    label game_continues:
        "And so I left the store."
        $ current_money = pc.coin
        if pc.coin > 1:
            "I have %(current_money)d coins left"
        #else:
        #   "I have %(current_money)d coin left"

        # increase motivation
        python:
            pc.motivation += 1
            current_motivation = pc.motivation
        
        "You feel motivated after going grocery shopping"
        "Now I have %(current_motivation)d motivation."
        
        pause

    label game_home:
        if choice_1 == False:
            play music "bensound-betterdays.mp3"
        label home_menu:
            scene bg_bedroom
            with fade
            
            menu: 
                "Check my inventory":
                    call screen inventory_screen
                    jump home_menu
                
                "Do some extra study":
                    "You feel a little smarter after learning something new"
                    $ pc.intelligence += 1
                    $ current_intelligence = pc.intelligence
                    "Now I have %(current_intelligence)d intelligence."

                "Go on the computer":
                    if choice_1 and pc.motivation >= 6:
                        "You felt invigorated about today's interactions and spend some productive time on the computer"
                    else:
                        "You don't feel motivated for much else and end up playing games until late in the night"
                    
                "Go to bed":
                    "You head to bed early"
                    $ pc.hp = pc.max_hp
                    $ current_hp = pc.hp
                    "Your current health is restored to %(current_hp)d hp"
    
    "The day has ended"

    scene black with fade

    "Thanks for trying the demo!" 
    "Try playing again with different choices.."
    pause
return
