import tkinter as tk
from tkinter import PhotoImage
import pyttsx3
import time
import os


def type_out(text, delay=0.014):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_and_speak(text, engine):
    """Prints the text with a typewriter effect and speaks it."""

    print()

    engine.say(text)
    engine.runAndWait()

#initialize the tKiniter GUI
root = tk.Tk()
root.title("Golf Putter Information")

# Label to display images
image_label = tk.Label(root)
image_label.pack()

image_paths = {
    "link1_user_review": "C:/Users/stlau/Downloads/Justin Christmas/Link1_Address-Line.png",
    "link1_technology": "C:/Users/stlau/Downloads/Justin Christmas/link1 tech.png",
    "link1_design": "C:/Users/stlau/Downloads/Justin Christmas/link1_hero_gold.png",
    "mezz1_user_review": "C:/Users/stlau/Downloads/Justin Christmas/Mezz1_Front_FinalGraphics_Black0074_Square_Site.png",
    "mezz1_design": "C:/Users/stlau/Downloads/Justin Christmas/mezz1.png",
    "mezz1_technology": "C:/Users/stlau/Downloads/Justin Christmas/Mezz_Standard_Colors_Black.png",
    "df21_design": "C:/Users/stlau/Downloads/Justin Christmas/df2.1top.png",
    "df21_user_review": "C:/Users/stlau/Downloads/Justin Christmas/df2.1.png",
    "df21_technology": "C:/Users/stlau/Downloads/Justin Christmas/df2.1bottonm.png",
    "er2": "C:/Users/stlau/Downloads/Justin Christmas/er2.png",
    "malibu": "C:/Users/stlau/Downloads/Justin Christmas/malibu.png",
    "phantom": "C:/Users/stlau/Downloads/Justin Christmas/phantom.png",
    "christmas": "C:/Users/stlau/Downloads/Justin Christmas/christmas.png",
    "caddie2": "C:/Users/stlau/Downloads/Justin Christmas/caddie2.png",
}
    # Path to your video
video_path = 'C:/Users/stlau/Documents/justincard.mp4'

def display_image(image_key):
    photo = PhotoImage(file=image_paths[image_key])
    image_label.config(image=photo)
    image_label.photo = photo

engine = pyttsx3.init()

# Set the engine to use Microsoft Hazel voice
hazel_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', hazel_voice_id)

# Adjust the rate of speech if necessary
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)  # Adjust the rate as needed

def mezz1_technology(engine):
    display_image("mezz1_technology")
    root.update_idletasks()
    technology_text = (
        "Like all L.A.B. Golf putters, the MEZZ1 is one hundred percent Angle Balanced to make putting easier and more fun. It feels like magic… but it's just science. "
        "With MEZZ.1, you'll feel contact more than you will with our largest and more forgiving mallets: MEZZ.1 MAX and DF 2.1. This added responsiveness is great for golfers that want a little more feedback about how their putter is moving and can help with controlling pace on ultra-slick putts.")         
    print_and_speak(technology_text, engine)
    

def mezz1_design(engine):
    display_image("mezz1_design")
    root.update_idletasks()
    design_text = (
        "Looks are important, but so is science. That's why MEZZ.1 looks pretty much like a normal mid-mallet putter. But unlike those other putters, it actually helps you hole more putts. "
        "Design of MEZZ.1: It features a sleek, small, black fang-style design. "
        "The putter is center-shafted with a white ACCRA X L.A.B. golf shaft, "
        "creating a futuristic and almost alien-like appearance.")
    print_and_speak(design_text, engine)
    

def mezz1_user_reviews(engine):
    display_image("mezz1_user_review")
    root.update_idletasks()
    review_text = (
        "User Reviews of MEZZ.1: Users often remark on the putter's excellent feel and consistent roll. "
        "Its unique design and technology contribute to more confident and accurate putting on the greens.")
    print_and_speak(review_text, engine)
    
def explore_mezz1(engine):
    while True:
        display_image("caddie2")
        root.update_idletasks()
        print_and_speak("\nMezz One:", engine)
        print("    ________________________________________")
        print("    | profile: Justin St-Laurent     U.K   |")
        print("    |--------------------------------------|")
        print("    |        MEZZ.1       | 1. Technology  |")
        print("    |        -----        |----------------|")
        print("    |                     | 2.   Design    |")
        print("    |        Small        |----------------|")
        print("    |         But         | 3.   User      |")
        print("    |        Mighty       |     Review     |")   
        print("    |---------------------|----------------|")
        print("    |                     | 4.   Back      |")
        print("    |_Caddie__By_SI_Labs__|________________|")
        print(" ")

        choice = input("          Enter your choice (1-4): ")

        if choice == '1':
            mezz1_technology(engine)
        elif choice == '2':
            mezz1_design(engine)
        elif choice == '3':
            mezz1_user_reviews(engine)
        elif choice == '4':
            break
        else:
            print_and_speak("Invalid choice, please try again.", engine)

def df21_technology(engine):
    display_image("df21_technology")
    root.update_idletasks()
    technology_text = (
        "Our Founder is Bill Presse, who is a former mini-tour player, had the idea to create a putter that would allow him to drastically simplify his stroke. He wanted to be able to count on a square putter face every time, which led him to invent Lie Angle Balance.  "
        "This technology simplifies the putting stroke by eliminating torque, allowing the putter to stay square to the path.")
    print_and_speak(technology_text, engine)
    

def df21_design(engine):
    display_image("df21_design")
    root.update_idletasks()
    design_text = (
        "Bill wanted to create a putter head that would give him as much forgiveness as possible, so he developed the radical shape of the DF 2 point 1 as a way to maximize consistency on off-center hits. Yes, it looks like a branding iron… but it works!"
        "The head is made from sixty sixty aircraft aluminum, heat-treated for consistency. ")
    print_and_speak(design_text, engine)
    

def df21_user_reviews(engine):
    display_image("df21_user_review")
    root.update_idletasks()
    review_text = (
        "User Reviews of DF 2.1: Golfers appreciate its exceptional balance and smooth swing. "
        "The design is tailored to reduce effort in controlling the putter head, promoting a natural pendulum-like motion.")    
    print_and_speak(review_text, engine)


def explore_df21(engine):
    while True:
       display_image("caddie2")
       root.update_idletasks()
       print_and_speak("\n Direct Force 2 point 1", engine)
       print("    ________________________________________")
       print("    | Profile: Justin St-Laurent     U.K.  |")
       print("    |--------------------------------------|")
       print("    |   Direct Force 2.1  | 1. Technology  |")
       print("    |         ---         |----------------|")
       print("    |                     | 2.   Design    |")
       print("    |    The Original     |----------------|")
       print("    |        L.A.B.       | 3.   User      |")
       print("    |        Putter       |     Review     |")   
       print("    |---------------------|----------------|")
       print("    |                     | 4.   Back      |")
       print("    |_Caddy_By_S_I_Labs___|________________|")
       print(" ")
       choice = input("       Enter your choice (1-4): ")

       if choice == '1':
            df21_technology(engine)
       elif choice == '2':
            df21_design(engine)
       elif choice == '3':
            df21_user_reviews(engine)
       elif choice == '4':
            break
       else:
            print_and_speak("Invalid choice, please try again.", engine)

def link1_technology(engine):
    display_image("link1_technology")
    root.update_idletasks()
    technology_text = (
        " What we did with LINK.1 was to honor the shape of legendary putters and make them dramatically easier to use.  "
        " The LINK.1 putter ensures the putter head stays square to the stroke path. "
        " Our goal with LINK.1 was to make it a no-brainer for blade users to make the switch. That starts with a simple blade head shape and extends to the grip, too. LINK.1 is made to be used with normal grips like our new Simple Rubber and Simple Cord. ")
    print_and_speak(technology_text, engine)
    

def link1_design(engine):
    display_image("link1_design")
    root.update_idletasks()
    design_text = (
        " We created LINK.1 for every golfer that loves the idea of using this timeless putter shape but doesn't make enough putts with it.... like yourself, justin........ "
        " It resembles a satin, Anser. with distinct heel and  toe weights and a center shaft placement. "
        " To bring Lie Angle Balance to LINK.1, we hyper-engineered it from 303 Stainless Steel. The putter head is 100% CNC Milled in the USA, and there are four screws on the heel side and six on the toe side so we can offer a wide range of length and lie angle options. ")  
    print_and_speak(design_text, engine)

def link1_user_reviews(engine):
    display_image("link1_user_review")
    root.update_idletasks()
    review_text = (
        " Golfers praise the LINK.1 for its impressive Lie Angle Balance technology. "
        " Its solid low-pitched sound and firm yet smooth feel have been highlighted, "
        " enhancing the golfer's experience on short to medium-range putts.")
    
    print_and_speak(review_text, engine)


def explore_link1(engine):
    while True:
        display_image("caddie2")
        root.update_idletasks()
        print_and_speak("\n Link 1", engine)
        print("    ________________________________________")
        print("    | Profile: Justin St-Laurent   -  U.K. |")
        print("    | -------------------------------------|")
        print("    |       Link  1       | 1. Technology  |")
        print("    |         ---         |----------------|")
        print("    |      Linking        | 2.   Design    |")
        print("    |        Past         |----------------|")
        print("    |        and          | 3.   User      |")
        print("    |       Future        |     Review     |")   
        print("    |---------------------|----------------|")
        print("    |                     | 4.   Back      |")
        print("    |_Caddy_By_S_I_Labs___|________________|")
        print(" ")
        choice = input("          Enter your choice (1-4): ")

        if choice == '1':
            link1_technology(engine)
        elif choice == '2':
            link1_design(engine)
        elif choice == '3':
            link1_user_reviews(engine)
        elif choice == '4':
            break
        else:
            print_and_speak("Invalid choice, please try again. ", engine)


def fitter(engine):
    intro_text = (
        " Justin.. now that you know what you're options might be, let's get you fitted for a putter. "
        " Now, let's embark on a simple yet crucial fitting journey. Just a few minutes and a bit of cooperation are all we need. "
        " Now I'll walk you through the process... since I doubt you can follow simple instructions....? Sim, what do you think. Ok, you may help him then.")
    display_image("caddie2")
    root.update_idletasks()
    print_and_speak(intro_text, engine)
    input("Press the Enter to continue...")
    
    # Step 2: Shoes and Putter
    shoes_putter = (
        "Next, gear up in your golf shoes for consistency. "
        "Then, grab your go-to putter ... the one that feels just right in your hands. If Sim says it's ok, of course. ")
    print_and_speak(shoes_putter, engine)
    input("Press the Enter to continue...")

    # Step 3: Find a Straightedge
    straightedge_text = (
        "Now, go stand infront of those cupboards over there, by the tv. "
        "Remember, it should be 90 degrees upright.")
    print_and_speak(straightedge_text, engine)
    input("Press the Enter to continue...")
    # Step 4: Record a Video
    video_instructions = (
        "Here's the fun part! Ask that handsome brother of yours to film you. "
        "His perfect hair should stand about five or ten feet away, down the line of the putt. "
        "Hot stuff, Make sure the camera is around hand level, and the video captures your whole body. But you knew that already didn't you? Of course you did. ")
    print_and_speak(video_instructions, engine)
    # User's Action
    input("Press Enter after you've recorded the video... ")
    # Step 5: Measure the Putter
    measure_putter = (
        "Almost there! Now, measure your putter length. "
        "Lay it flat, measure from the center of the face to the top of the grip, and jot down the length. ")
    print_and_speak(measure_putter, engine)
    input("Enter the length of your putter in inches: ")
    thank_you = ("Fantastic! You've completed the fitting process. I am mildly impressed you could keep up. Congrats! ")
    
    print_and_speak(thank_you, engine)
    input("Press the Enter to continue...")  

def lab_golf(engine):
    lab_golf_text = (
        "L A B Golf was founded in twenty fourteen by Sam Hann. a former, aerospace engineer. "
        "Sam's passion for golf, and engineering, led him to create a putter, that would help him improve his game and develop Lie Angle Balance technology. "
        "Lie Angle Balance or L A B  Technology makes it effortless for golfers to deliver a square putter face at impact because, unlike other putters, it keeps the putter face square to the arc throughout the stroke. It makes putting as easy as picking the right line, the right speed, and making your natural stroke. ")
    display_image("caddie2")
    root.update_idletasks()
    print_and_speak(lab_golf_text, engine)

def er2(engine):
    display_image("er2")
    root.update_idletasks()
    er2_text = (
        "Precision milled from 3 oh 3 stainless steel, the E V2 boasts a new streamlined design to create a premium low profile look at address. "
        "A thinned out topline, squared off rear bumpers and redesigned sole create a modern, sleek looking blade that seemingly blends into the putting surface, while the redistribution of mass behind the hitting area provides optimal sound and feel feedback. "
        "The addition of two deep seated, rear multi material weights help increase em oh eye to provide added stability to Even roll's most successful blade model ever. ")
    print_and_speak(er2_text, engine)

def px5(engine):
    display_image("phantom")
    root.update_idletasks()
    px5_text = (
        "The updated Phantom X 5, provides the performance and alignment benefits of a mallet, with the feel of a blade. "
        "This Tour-proven, almost face balanced model, returns with a solid precision milled 303 stainless steel face carried through to the body and wings integrated with an aluminum sole plate and stainless steel sole weights. "
        "Equipped with a refined Pistolero Plus grip, the single mid-bend of the stepless steel shaft is aimed directly down the target line and provides one shaft of offset for Scotty's most modern Phantom X 5 yet. ")
    print_and_speak(px5_text, engine)

def la_mal(engine):
    display_image("malibu")
    root.update_idletasks()
    la_mal_text = (
        "The Malebu By L.A. Golf. It features a matte carbon head. The all-carbon construction, a material 5 times less dense than solid steel, allows for a much larger area of forgiveness for off-center hits... "
        "L.A. GOLF's patented, Descending Loft Face technology. features four descending degrees of loft, to solve for consistency with launch angles and yields more predictable rolls. "
        "The P-Series SoHo shaft comes standard, produces unmatched stability, and features anti-vibration material to create the signature feel L.A. GOLF is known for. ")
    print_and_speak(la_mal_text, engine)

def other_options(engine):
     while True:
        display_image("caddie2")
        root.update_idletasks()
        print_and_speak("\n Other Brands", engine)
        print("    ________________________________________")
        print("    | Profile: Justin St-Laurent  -  U.K.  |")
        print("    |--------------------------------------|")
        print("    |   1.   Evnroll      |                |")
        print("    |          ER2        |  3.  Scotty    |")
        print("    |---------------------|      Cameron   |")
        print("    |---------------------|                |")
        print("    |   2.   La GOLF      |      Phantom   |")
        print("    |        Malibu       |        x-5     |")   
        print("    |---------------------|----------------|")
        print("    |                     | 4.   Back      |")
        print("    |_Caddy_By_S_I_Labs___|________________|")
        print(" ")
        choice = input("          Enter your choice (1-4): ")

        

        if choice == '1':
            er2(engine)
        elif choice == '2':
           la_mal(engine) 
        elif choice == '3':
            px5(engine)
        elif choice == '4':
            break
        else:
            print_and_speak("Invalid choice, please try again.", engine)

def christmas(engine):
    christmas_text = (
        "Justin... Merry Christmas for us, S.I. Labs. "
        "We really wanted to show our appreciation for you, and all The support you've provided, to help get Sim to where he is today. "
        "To thank you, we've gone ahead and transfered 300 dollars from Sims account directly into yours, To put towards a new putter. "
        )
    print_and_speak(christmas_text, engine)

def play_video(video_path):
    try:
        os.startfile(video_path)
    except Exception as e:
        print(f"Error opening video: {e}")   

def christmas_submenu(engine):
    while True:
        display_image("christmas")
        root.update_idletasks()
        print_and_speak("\nChristmas Options", engine)
        print("    ________________________________________")
        print("    | Profile: Justin St-Laurent  -  U.K.  |")
        print("    |--------------------------------------|")
        print("    |   1  |        Reveal Gift            |")
        print("    |--------------------------------------|")
        print("    |      |        Play Custom            |")
        print("    |   2  |         Highlight             |")
        print("    |      |           Tape                |")
        print("    |--------------------------------------|")
        print("    |___Caddie_by_SI_Labs__|__3__Main Menu_|")
        print(" ")
        choice = input("          Enter your choice (1-3): ")

        if choice == '2':
            play_video(video_path)
        elif choice == '1':
            christmas(engine)
        elif choice == '3':
            break
        else:
            print_and_speak("Invalid choice, please try again.", engine)

def main():
    input("Press Enter to start...") 
    print("")
    type_out("Welcome to  'Caddie' - Putter Fitter and Expert")
    print( )
    type_out("powered by S.I. (Simon Intelligence) Labs")
    print( )
    type_out("Please wait while the program loads...")

    # Personalized Introduction
    introduction = (
        "Scanning User........ Profile Secured... "
        "Justin Saint Laurent, Nickname Shit Head, Age twenty eight. Residence Brighton, U.K.. Occupation Not actually sure. and finally, Natural Putting Talent. Three, out of Ten. " 
        "Good Morning and Merry Christmas, Justin. I am Caddie, Created by Ess I, or, Simon Intelligence Labs. " 
        "Let us begin our journey, into the new age of putters. ")
    display_image("caddie2")
    root.update_idletasks()
    print_and_speak(introduction, engine)

    christmas_submenu(engine)
   # Introduction
    while True:
       display_image("caddie2")
       root.update_idletasks()
       
       print_and_speak("Main Menu",engine)
       print("    ________________________________________")
       print("    | Profile: Justin St-Laurent  -  U.K.  |")
       print("    |---------------------|----------------|")
       print("    |  1. DF 2.1 (L.A.B.) | 5. About L.A.B |")
       print("    |---------------------|----------------|")
       print("    |  2. Link 1 (L.A.B.) | 6. Home Style  |")
       print("    |---------------------|     Fitting    |")
       print("    |  3. MEZZ.1 (L.A.B.) |----------------|")
       print("    |---------------------| 0.  REVEAL     |")   
       print("    |  4.   Other Brand   |      YOUR      |")
       print("    |---------------------|      GIFT      |")
       print("    |_Caddy_By_S_I_Labs___|________________|")
       print(" ")
       choice = input("         Enter your choice (1-6): ")


       # Execute the corresponding function based on user choice
       if choice == '1':
           explore_df21(engine)
       elif choice == '2':
           explore_link1(engine)
       elif choice == '3':
           explore_mezz1(engine)   
       elif choice == '4':
           other_options(engine)
       elif choice == '5':
           lab_golf(engine)    
       elif choice == '6':
           fitter(engine)
       elif choice == '0':
           christmas_submenu(engine)     
       elif choice == '7':
           print_and_speak("Thank you for exploring the elle eh bee putters with me. Goodbye!", engine)
           break
       else:
           print_and_speak("Invalid choice, please try again.", engine)

# Run the program
if __name__ == "__main__":
   main()
   root.mainloop()
