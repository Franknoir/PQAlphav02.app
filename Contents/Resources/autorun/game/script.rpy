# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Pickle Dad")


# The game starts here.

label start:

    scene bg room


    e "Well, hello, Pickle, I think you have a lot of questions. "

    e "First, you need to get out of this messy place, and I'll help you. You're in for a tough election and its consequences. 
    Good luck, buddy..."  

    scene start noir 
    with fade

   
    e "You're in this dirty, noisy town, you don't know who you are, and nobody knows who you are."

    e "You fell out of a window, and all you know is that you want to survive and get answers to your questions."

    e "Pick your starting location, pickle."

    menu:

        "Street": 

            jump street

        "Junk":

            jump junk

    label junk:

        scene junk
        with fade

        e "It's not the most beautiful place, but it is what it is."

    label garbage:

        scene garbage
        with fade

        e "There's a sudden stirring around here. What are you gonna do? "

    menu:

        "RUN!!!":
            jump run 
        
        "to pick up something that looks like a weapon":

            jump weapon
        
    label run:

        scene run
        with fade 

        e "HURRY UP AND GET OFF YOUR FEET OR WHATEVER IT IS YOU GOT!!!!"
        jump alleyfight

    label weapon:

        scene weapon
        with fade

        e "You grabbed a toothpick and stabbed the huge rat that attacked you, then heroically retreated out of the container."
        jump alleyfight

    label street:

        scene street 
        with fade

        e 'you get into heavy traffic, see a gap between the houses and decide to go through the crowd.'
           
    menu:

        "trying to roll between their legs":
            jump alley

        "grab a cat as transportation":
            jump cat 

    label alley: 

        scene alley
        with fade 

        e "people knocked you into a back alley."
        jump alleyfight

    label cat:

        scene cat
        with fade

        e "grabbed the cat and ran with it down the alley."

            

    label alleyfight:
        
        scene alleyfight 
        with fade

        e "you're in an alley where rats are fighting, but the cat scared them off, you know. "

    label pigeons:

        scene pigeons 
        with fade 

        e "Eventually, you think you're safe, but when you look up, you find strange creatures staring at you with scary eyes."

    menu:

        "Find shelter before sunset where you can wait out the night.":
            jump darkalley
        

        "Try to get away from them now.":
            jump escape
    

    label escape:

        scene escape
        with fade 

        e 'you try to get away from the pigeons, but they start chasing you. '
        e "you can see an open door at the end of the alley in front of you. "

    menu:

        "run into an open door ":
            jump opendoor


    

    

    label runj:

        scene runj 
        with fade 

        e "you ran "
        e "what else is left to do"
        e "you need to survive"
        e "an empty jar fell from somewhere and smashed in front of you. "
        e "it scared away the pigeons "
    
    

    label screaming2:

        scene screaming2
        with fade 


        e "you ran as fast as you could and ran under the next table."
        e "it turned out to be occupied by someone else."
        jump cockroaches

    label cockroaches:
        
        scene cockroaches
        with fade 

        e "They've got their own kitchen, they're staring at you. "

        e "One huge boss cockroach coming at you, the rest of them scattered across the kitchen floor. "

    menu:
        "Ride the cockroach boss.":
            jump rodeo


        "get away with the hype " :
            jump ground

    


    label ground:

        scene ground
        with fade 

        e "you run out into the backyard and there's a playground with a sandbox in front of you. "
        e "in the sandbox, you see a sports car your size. "
        e "there's a remote control lying around and no one else is around. "
        e "Those kids are so inconsiderate..."

    menu:

        "get in the car and take the remote control ":
            jump car 

        "dive in the sand":
            jump sand 

    
    label sand:

        scene sand 
        with fade 


        e "you buried yourself in the sand next to the kids' toys. "
        e "you buried yourself in the sand next to the kids' toys"
        jump castle 

    
    label castle:

        scene castle
        with fade 


        e "a kid was making a sandcastle and got you in his bucket. "

    
    label sandjar:

        scene sandjar
        with fade 


        e "a kid brought you home with sand and put it in a glass jar. "
        e "I don't think his mom's gonna like it."



    menu:

        "stay in the sand " :
            jump toilet

        "get out before it's too late":
            jump uniform


    label uniform:

        scene uniform 
        with fade


        e "you crawled out of the sand "        
        e "the baby's mother's work uniform caught your eye. "
        e "the uniforms were from the pickle factory. "

    menu:

        "to reach into her uniform pocket and wait for a miracle.":
            jump pocketu 


        "to keep looking at uniforms, why not?":
            jump uniformu 
    



    label uniformu:

        scene uniformu 
        with fade 


        e "you're staring as if the uniform is telling you: You look lonely, I can fix that...."
        e "A woman walks up and yells :"
        e "Fuck, I brought a pickle home from work again. Mr. Simon's gonna kill me. That's the sixth time this week. "
        e "she stuffed you in her pocket and took you to the factory. "
        jump factoryday






    label pocketu:

        scene pocketu 
        with fade 


        e "you reached into your breast pocket "
        e "you were at this woman's workplace in the morning "
        jump factoryday



    label toilet:

        scene toilet
        with fade 


        e "his mother noticed he'd brought sand from the street and put it on the windowsill.  "
        e "she asked him to explain himself, but he just mumbled.  "
        e "she put all the sand in the toilet and flushed you down the drain. "
        e "the sewage pipes brought you to the pickle factory. "
        jump factoryday



    label car:

        scene car 
        with fade 


        e "you get in the car and you steal it. "

    menu:

        "drive and stop at the store ":
            jump storecar 


        "keep driving ":
            jump busstop
    


    label busstop:

        scene busstop
        with fade 


        e "the super car's battery is dead "

        e "You got out of the car, I don't know what you're supposed to do. "

        e "you looked up and saw a job posting for a pickle factory at the bus stop. "

        e "that's where you're going. "

    menu:

        "follow the signs to the factory ":
            jump factoryday

        "you're tired of walking, you're addicted to vehicles. Take the bus that goes to the factory anyway. ":
            jump factoryday 
    
    label storecar:

        scene storecar
        with fade 


        e "You stopped by the store, and you saw an interesting sign on the truck across the street. "

        e "you looked closely."
        jump cartruck 

    
    label cartruck:

        scene cartruck 
        with fade 


        e "this is the address of the pickle factory "
        e "THAT'S EXACTLY WHAT WE NEED!!!"


    menu: 

        "get in the truck":
            jump factoryday


        "follow the truck":
            jump factoryday



    label rodeo:

        scene rodeo 
        with fade 

        e "you started a freakin' rodeo on that cockroach!"
        e "you rushed out of the damn building, through the feet of the cooks. "
        jump board 

    label board:

        scene board 
        with fade 

        e "you're on the street and there's a huge billboard in front of you. "
        e "it has some interesting information about the pickle factory. "
        e "Damn, this is exactly where you need to go. "
   

    menu:

        "go to the address on the billboard ":
            jump factoryday

        "to get revenge on the pigeons on the cockroach. ":
            jump pf

    


    label pf:
        scene pf
        with fade 


        e "the pigeons were actually bigger than the cockroach"
        e "That was a weird decision, buddy. "
        e "they kicked your ass and you scrambled to get to the factory address. "
        jump factoryday



    label opendoor:

        scene opendoor
        with fade


        e "you run through an open door and there's horror in the flesh before your eyes. "
        e "you can't believe your eyes that there can be such cruelty... "
        e "that's when you lost faith in humanity."
        jump kitchen
    
    label kitchen:

        scene kitchen 
        with fade 

        e "..."
        e "you're in the kitchen."

    menu:

        "take a look in the kitchen ":
            jump cook 


        "quickly run to the pantry":
            jump darkz



    label darkz:

        scene darkz
        with fade 

        e "It's very dark in here. "        
        e "you've found the light switch"
        e "click*"
        jump zombi 

    label zombi:

        scene zombi 
         


        e "the lights come on and you find that behind the pantry door in total darkness they are storing ZOMBIE- VEGETABLES !"
        e "it took you a few seconds to realize it was just rotten vegetables..."    
        e "they won't hurt you, just stink."
        e "you see an empty jar on the top shelf. "
        e "you got two ideas "
        e "to cover yourself in rotten vegetables to be mistaken for one of them."
        e "or climb up on the top shelf to look at the jar. "

    menu:

        "to cover yourself in rotten vegetables":
            jump angry 


        "climb on a shelf.":
            jump jart 
    

    label angry:

        scene angry  
        
        e "A cook breaks violently into the pantry and yells :"
         

        e "WHY HAVEN'T YOU THROWN OUT THE VEGETABLES, ASSHOLES, THEY'RE ALREADY STINKING !!!!"

    menu:

        "stay still" :
            jump trash 

        "pretend to be a zombie vegetable ":
            jump boo


    label boo:

        scene boo

        e "BOOO!"
        jump jesus




    label jesus:

        scene jesus 

        e "The cook was scared and quickly made a molotov cocktail, took out a bible and started reading a prayer.  "
        e "He threw a molotov cocktail at you. "

    
    menu:

        "accept your destiny":
            jump burn 


        "to run into an unknown crevice in the wall. ":
            jump hole 


      
    label hole:

        scene hole 
        with fade 

        e "ran into the hole between the closet and the toilet. "
        jump mantoilet 


    label mantoilet:

        scene mantoilet

        e "there's some guy sitting in the bathroom "    
        e "he's busy with the paper, whatever else people do in the bathroom. "
        e "I guess he didn't see you."


    menu:

        "get into his pants pocket, they're on the floor. ":
            jump derek


        "bite him":
            jump scary 

    

    label derek:

        scene derek 
        with fade 


        e "the man finished and went back to his dinner table with his wife. "
        e "a woman noticed something sticking out of his pocket and asked him:"
        e "Derek, are you so happy to see me? "
        e "the man doesn't know what she's talking about. "  
        e "you found a hole in his pocket and a nasal raft. "


    menu:

        "make a cape and get off ":
            jump batpickle 


        "poke through the hole":
            jump kicka 


    label kicka: 

        scene kicka 

        e "the man sensed something wrong and started rubbing his leg. "  
        e "you fell out and he kicked you to the exit. "      
        e "the last thing you heard was:"
        e "Ugh, Derek, you just came from the bathroom!"
        jump mister


    
    label batpickle:


        scene batpickle 
        with fade 


        e "you came out of your pocket and you felt really cool. "
        e "That's when you remembered you don't know where your parents are or if they even exist. "
        e "as you flew to the exit and reminisced about your past. "
        jump mister 

    

    label mister:

        scene mister 
        with fade 

        e "some stranger just before you left grabbed you with the words: "
        e "You're the one I'm looking for. "
        e "and threw you in the jar with the rest of the pickles. "
        e "he took you to an unknown destination. "
        jump factoryday 







    label scary:

        scene scary 


        e "a man screamed in fear of being bitten by a zombie pickle. "  
        e "the fear and despair in his eyes. "      
    

    menu:

        "keep attacking":
            jump kill 

        "while he's yelling to jump in the toilet. ":
            jump toiletu 


    label toiletu:

        scene tioletu 
        with fade 

        e "you went to the toilet and ended up in the sewer. "        

        e "you took a long walk down a straight pipe in the sewer."
        
        e "until at the end of the road you saw the light and came to the ..."
        jump factoryday 



    label kill:

        scene kill 
        with fade 


        e "he just squashed you."
        return 






    label burn:

        scene burn 
        with fade 

        e "You're burned."
        return 






    label trash:

        scene trash 
        with fade 


        e "The cooks ran to the screams and quickly threw all the rotten vegetables into the garbage can outside "
        e "you, too. "


    menu:

        "lie down and relax":
            jump trashcar


        "to get down from the trash can and go stink. " :
            jump animal 

    

    label trashcar:

        scene trashcar 
        with fade 


        e "while you were relaxing, a garbage truck came by and picked you up with the trash. "
        e "but you didn't care, you'd been through a lot and you just wanted to relax. "
        e "the garbage truck stopped and you looked out to see where you were. "
        jump factoryday




    label animal:


        scene animal 
        with fade 


        e "you smelled so bad you got the raccoon's attention. "    
        e "and he didn't realize you were a living organism and ate you. "    
        e "To him, you're just a stinking vegetable by the dumpster in the back alley. "
        return





    label jart: 

        scene jart 
        with fade 


        e " you get on the shelf and see that the jar is labeled from a pickle factory. "
    
    
    menu: 

        "crawl into an empty jar ":
            jump shard 


        "look at the label in detail":
            jump address 


    label address:

        scene address 
        with fade 


        e "you looked at the label and found the factory address "        
        jump cooka 

    label cooka:

        scene cooka 
        

        e "the cook bursts into the pantry and yells :"
        e "WHY HAVEN'T YOU THROWN OUT THOSE VEGETABLES? THEY'RE ALREADY STINKING!!!"

    menu:

        "kick the jar off the shelf":
            jump kitchens 


        "to jump on his chef's hat ":
            jump smoke 


    label smoke:

        scene smoke 
        with fade 


        e "the cook comes back to the kitchen and says he's going out for a smoke. "     
        e "the cook looks tired. " 
        e "he might not even see if you jump. " 


    menu:

        "jump off the top of my head into the street ":
            jump truckcar


        "wait for the right time " :
            jump cart 

    
    
    label cart:

        scene cart 
        with fade 

        e "sitting on his hood, you see some truck pull up. "
        e "If you get any closer, you'll recognize the logo "
        e "it's the logo for the pickle factory!"

    menu:

        "jump off and sneak into the trunk of a truck ":
            jump darkq


        "to jump into the driver's hood ":
            jump darkw




    label truckcar:

        scene truckcar
        with fade 

        e "you jumped off, he didn't even notice."
        e "a truck comes around the corner and stops. "
        e "there's a huge pickle factory logo on the truck. "
        e "He's definitely from there, you'd think. "
        e "the truck driver came out to talk to the cook "


    menu:

        "sneak into the truck stealthily " :
            jump darkq 


        "get in the driver's pocket " :
            jump darkw 


    
    label darkw:

        scene darkw 
        with fade 


        e "It's dark and tight in here. "
        e "the truck drove off and then stopped a while later. "
        e "the driver went outside and you jumped out unnoticed. "
        jump factoryday



    label darkq:

        scene darq 
        with fade 

        e "It's dark in here. "
        e "the car stops and you get out "
        jump factoryday 



    label kitchens:

        scene kitchens 
        with fade 


        e "you distracted him and went back to the kitchen. "
        e "you're back in this hell..."
        e "you can't stay here for long. "

    menu:

        "climb into a dish on the table ":
            jump food 

        "crawl up a waiter's pant leg. ":
            jump leg 

    

    label food:

        scene food 
        with fade 

        e "that's where you came in. "
        e "but there's something wrong here."
        e "I think I know what..."
        jump bye 

    

    label bye:

        scene bye 
        with fade 

        e "..."
        e "you got into an uncooked dish and you were cooked with it. "
        return 




    label leg:

        scene leg
        with fade 

        e "you're in a pant leg. "
        e "the waiter started moving abruptly somewhere"
        jump order



    label order:

        scene order

        e "the waiter takes the customer's order "
        e "he's walking across the hall"

    menu:

        "jump out and crawl under the carpet to the front door. ":
            jump crushed 

        "to get under the client's pants. ":
            jump client 



    label client:

        scene client 
        with fade 

        e "He was wearing long socks "        
        e "he didn't notice you. "
        e "you hear him get a call, and in the phone conversation you realize he's an inspector and he needs to get to the pickle factory right away. "

    menu:

        "stay in the pant leg ":
            jump cari


        "climb into his sock":
            jump kick 


    label kick:

        scene kick 

        e "he felt discomfort and kicked you away. "     
        e "he kicked you hard. "   
        e "there must have been a lot of discomfort "
        jump garbaget

    label garbaget:

        scene garbaget
        with fade 


        e "you flew into a garbage truck "
        e "the garbage truck just lucky enough to get you where you need to go. "
        jump factoryday
    


    label cari:

        scene cari
        with fade 


        e "the inspector had to cut short his lunch and go to the factory. "

        e "he got in his car and went on a call. "
        jump factoryday




    label crushed:

        scene crushed 
        with fade 


        e "..."
        e "you've been squashed. "
        return 




    label shard:

        scene shard
        with fade 


        e "you got in the jar, it started to wobble. "
        e "a can fell off the top shelf and shattered. "
        e "you've been stabbed through with a shard...."
        e "Better luck next time, buddy. "
        return 

    label cook:

        scene cook 
        with fade 

        e "the chef saw you on the floor and started yelling like a sick fuck. "
        e "- HOW MANY TIMES HAVE I TOLD YOU NOT TO DROP YOUR VEGETABLES ON THE FLOOR, YOU IDIOTS !!!!"

    menu:

        "play dead, close your eyes and mouth. ":
            jump dead 


        "try to escape the scene":
            jump screaming2

    label dead:

        scene dead 
        with fade 

        e "you're playing dead."
        e "I gotta say, you've got talent. "
        e "the chief came over, picked you up and threw you among the other vegetables on the table. "


    menu:

        "keep playing dead ":
            jump salad


        "stand up and run across the table":
            jump chop 
    
    
    label salad:

        scene salad
        with fade 

        e "The chef didn't like this customer, so he threw you whole in the salad. "
        e "you're being brought out on a plate to this client. "
        e "to be eaten, if you haven't figured that out by now. "

    label lary:

        scene lary
        with fade 

        e "that client is Larry."
        e "ooh shit..."
        e "Brother, this is a very dangerous man. You need to think fast. "

    menu:

        "jump in his cuddy, buy some time. ":
            jump caddy


        "run screaming ":
            jump screaming
    

    label caddy:

        scene caddy 
        with fade 

        e "You jumped into his breast pocket because you saw a pen there and you wanted to use it to attack Larry. "
        e "but once you're in your pocket, you're quiet. "
        e "you hear his radio saying there's an accident at the pickle plant and the exact address. "

    menu:

        "stay in the pocket":
            jump factoryday

        "to jump out and get there on your own ":
            jump factoryday 



    label screaming:

        scene screaming
        with fade 

        e "you jump on the floor and run outside. "
        e "he starts chasing you, but he can't keep up. "
        e "Larry only recently started eating salads "
        e ":D"
    
    label out:

        scene out
        with fade 

        e "need to make a quick decision "
    
    menu:

        "to jump on a passing girl's shoe. ":
            jump shoe 


        "to hide under the tire of a parked car. ":
            jump wheel
    

    label shoe:

        scene shoe
        with fade 

        e "you sneak up on her shoes "
        e "I don't even know how you did that."
        e "the girl walked quickly in one direction. "
        e "Larry's behind "
        e "A girl came to check on her father at his work. You were surprised to see this place. "
        e "because it's..."
        jump factoryday

    label wheel:

        scene wheel
        with fade 

        e "you've got your teeth caught in a tire pump. "
        e "the car's started, it's gonna be a rough ride. "
        e "the car stopped, you unhooked, and you saw in front of you..."
        jump factoryday

    label chop:

        scene chop 
        with fade 

        e "you ran across the table, a neighboring chef saw you and cut you in half with his knife. "
        e "Better luck next time, buddy. "
        
        return 
    
    label darkalley:

        scene darkalley
        with fade

        e "you wait till night and you come out of hiding, you hear some voices."

    menu:

        "you go to the polls hoping to see if any other pickles have passed through.":
            jump homeless

    
        "you think it's a bad idea to go for the voice and you go the other way.":
            jump club
    
    label club:

        scene club 
        with fade 

        e "you went the other way and came upon a door with loud music coming from it. It's a door leading to a club. "
      

        e "you have to disguise yourself so you won't be recognized as a talking pickle. "
    

    menu:

        " pick out and put on glasses, tie, wig? ":
            jump clubin

        "I don't give a fuck, one pair of sunglasses will do. ":
            jump clubin

    label clubin:
        
        scene clubin
        with fade 

        e "You walk into a club, the music is loud, you don't know how to act or where to start. "

        e "but you gotta start somewhere.  "

    menu:

        "approach the bartender ":
            jump barman 

        "rock the dance floor, baby. ":
            jump dance
    
    label dance:

        scene dance
        with fade 

        e "you started to do a fancy dance and a girl spotted you."

    menu:
        "hook up with a girl":
            jump breakfast

        "to ask her for the pickles":
            jump talk 
    

    label talk:

        scene talk 
        with fade 

        e "you went someplace quieter "
        e "she told you she works at the pickle factory. She asked why you were asking  "
        e "You said you had unfinished business and it's important, more important than the two of us, Rebecca. "
        e " her name is Rebecca, by the way. "
        e "Rebecca looked at you with an understanding look and offered to drive you there in the morning "
        
        menu:
            "agree to go with her in the morning.":
                jump allnight


            "to demand that she take you there now": 
                jump card
    

    label card:

        scene card 
        with fade 

        e "she gives you the plant's business card and you know exactly what you need to do. "
        jump factory



    label allnight:

        scene allnight 
        with fade 

        e "you've been partying all night, no one even suspected you were a pickle. "
        e "the morning she took you to the factory and you said goodbye. "
        jump factoryday

    label breakfast:

        scene breakfast
        with fade 

        e "you turned out to be a very brave pickle .... You've had a lot to drink. "
        e "You wake up in her bed in the morning, you don't remember how you got here or what you did that night that was so dirty and inexplicable. "   
        e "Did you notice she's making breakfast for you? She probably never realized you were a cucumber. The disguise was pretty fucking good. "
        e "what's she cooking? you see something familiar on the table, wait a minute, what's that...?"
        e "PICKLES!!! SHE CUTS THEM UP AND ADDS THEM TO THE EYES (you're feeling flashback) "

    menu:

        "Run away quietly because she'll eat you like Jeffrey Dummer. ":
            jump door 

        "ask her what she's doing?":
            jump ask 
    

    label door:

        scene door
        with fade 


        e "you look around and see an open door, your only chance to escape and not share the fate of the salty brothers. "
        e "before you memorized the address on the pickle jar label. P.S. It's a well-known fact that pickles and eagles have the best eyesight."
        e "you've come to the right place, because you've had enough adventures for one day. "
        jump factoryday


    label ask:

        scene ask
        with fade 

        e "she says she's making breakfast. What else could she say? "
        e "You're asking where she got those pickles on the table that are in the jar. Damn it, you're very careful. "
        e "she says she works at a pickle factory and every breakfast she makes has pickles in it. "
        e "you're gonna throw up...."
        e "you ask her to take you to that factory."
        e "she agrees suspiciously "
        jump factoryday


    label barman:

        scene barman 
        with fade 

        e "walks up to the bartender and sees him throwing an olive into a martini."
        e "You're asking if he's got one with pickles "
        e "the bartender shows me a jar of pickles. You see the address of the factory on it "

    menu:

        "go now ":
            jump factory 

        "to have fun and go to an address in the morning ":
            jump factoryday

    label homeless:

        scene homeless
        with fade 

        e "you met some homeless people "

    label homeless1:

        scene homeless1
         

        e "who wanted to eat you!!!"

    menu:

        "try to explain that you don't need to be eaten.":
            jump homelessway


        "Fuck, I gotta run again.":
            jump fallenhomeless


    label homelessway:

        scene homelessway
        with fade 

        e "they're shocked that they're talking to a pickle, and they're telling him to fuck off to the store or the factory."
    
    menu:

        "go to the factory ":
            jump factory

        "go to the store":
            jump store 

    label fallenhomeless:

        scene fallenhomeless
        with fade

        e "you try to run between their legs, but the bum steps on you and slips like a banana. You're okay. Don't worry. "
    
    menu:

        "Running at your own speed":
            jump runnight

        "grab with his teeth at a passing cat that is running in the same direction":
            jump catnight

    label runnight:

        scene runnight
        with fade 

        e "you ran so fast you stuck to the label on the floor."

    label catnight:
        
        scene catnight
        with fade 

        e "the cat led you to the end of the alley and you saw a big truck. "
    
    label truckad:

        scene truckad
        with fade 

        e "it was plastered with ads for something familiar to you. "
        e "it's an advertisement for PICKLES !! with the address of the factory. "

    menu:

        "to jump in the driver's pocket ":
            jump pocket

        "jump in the car ":
            jump dark1 

    label pocket:

        scene pocket 
        with fade 

        e " It's pretty spacious. The driver was a dandy and wears loose pants. He didn't even see you. "
        e "the truck stopped and the door opened. You found yourself..."
        jump factory
    
    label dark1:

        scene dark1
        with fade

        e "It's very dark in here. "
        e "the truck stopped abruptly and you jumped out and saw .... in front of you."
        jump factory


    label factory:

        scene factory
        with fade 

        e "END"
    return

    label store:

        scene store
        with fade 

        e "you walk up to the store and you see some weird sign ..... you take a closer look..."
    
    label signboard:

        scene signboard
        with fade 

        e "the sign says : best pickles at our factory!!! And the address where it is."

    menu:
        
        "went to an address at the factory":
            jump factory
        
        "saw the truckers unloading products with the logo from this plant and jumped in the van.":
            jump factory
    return
  
    label factoryday:
        scene factoryday
        with fade 

        e "FIN"
    return 