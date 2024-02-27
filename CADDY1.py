import pyttsx3
import time
import threading

def print_and_speak(text, engine):
    """Prints the text with a typewriter effect and speaks it."""
    
    def print_text():
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.07)
        print()

    print_thread = threading.Thread(target=print_text)
    speak_thread = threading.Thread(target=engine.say, args=(text,))
    
    print_thread.start()
    speak_thread.start()
    
    print_thread.join()
    speak_thread.join()

# The rest of your code remains the same...


def explore_mezz1(engine):
    while True:
        print_and_speak("\nPlease choose an aspect to learn more:", engine)
        print("1. Technology")
        print("2. Design")
        print("3. User Reviews")
        print("4. Go Back")

        choice = input("Enter your choice (1-4): ")

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

def mezz1_technology(engine):
    technology_text = (
        "Technology of MEZZ.1: This putter uses innovative lie angle balance technology, "
        "which is key to its performance. It ensures a consistent and repeatable stroke by reducing the tendency of the putter head to twist.")
    print_and_speak(technology_text, engine)

def mezz1_design(engine):
    design_text = (
        "Design of MEZZ.1: It features a sleek, small, black fang-style design. "
        "The putter is center-shafted with a white ACCRA X L.A.B. golf shaft, "
        "creating a futuristic and almost alien-like appearance.")
    print_and_speak(design_text, engine)

def mezz1_user_reviews(engine):
    review_text = (
        "User Reviews of MEZZ.1: Users often remark on the putter's excellent feel and consistent roll. "
        "Its unique design and technology contribute to more confident and accurate putting on the greens.")
    print_and_speak(review_text, engine)
def explore_df21(engine):
    while True:
        print_and_speak("\nPlease choose an aspect to learn more:", engine)
        print("1. Technology")
        print("2. Design")
        print("3. User Reviews")
        print("4. Go Back")

        choice = input("Enter your choice (1-4): ")

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

def df21_technology(engine):
    technology_text = (
        "Technology of DF 2.1: The key feature of this putter is the Lie Angle Balance Technology. "
        "This technology simplifies the putting stroke by eliminating torque, allowing the putter to stay square to the path.")
    print_and_speak(technology_text, engine)

def df21_design(engine):
    design_text = (
        "Design of DF 2.1: Known for its unique and distinct appearance, often described as 'crazy looking.' "
        "The head is made from 6061 aircraft aluminum, heat-treated for consistency. "
        "Its large footprint and elongated face contribute to its unique design.")
    print_and_speak(design_text, engine)

def df21_user_reviews(engine):
    review_text = (
        "User Reviews of DF 2.1: Golfers appreciate its exceptional balance and smooth swing. "
        "The design is tailored to reduce effort in controlling the putter head, promoting a natural pendulum-like motion.")
    print_and_speak(review_text, engine)

def explore_link1(engine):
    while True:
        print_and_speak("\nPlease choose an aspect to learn more:", engine)
        print("1. Technology")
        print("2. Design")
        print("3. User Reviews")
        print("4. Go Back")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            link1_technology(engine)
        elif choice == '2':
            link1_design(engine)
        elif choice == '3':
            link1_user_reviews(engine)
        elif choice == '4':
            break
        else:
            print_and_speak("Invalid choice, please try again.", engine)



def link1_technology(engine):
    technology_text = (
        "Technology of LINK.1: Featuring Lie Angle Balance technology, "
        "the LINK.1 putter ensures the putter head stays square to the stroke path. "
        "This technology is crucial for accuracy and consistency in putting.")
    print_and_speak(technology_text, engine)
def link1_design(engine):
    design_text = (
        "Design of LINK.1: A blend of classic looks with modern tech. "
        "It resembles a satin Anser with distinct heel and toe weights and a center shaft placement. "
        "Made from 303 Stainless Steel, the head is CNC milled, highlighting its intricate and precise construction.")
    print_and_speak(design_text, engine)

def link1_user_reviews(engine):
    review_text = (
        "User Reviews of LINK.1: Golfers praise the LINK.1 for its impressive Lie Angle Balance technology. "
        "Its solid low-pitched sound and firm yet smooth feel have been highlighted, "
        "enhancing the golfer's experience on short to medium-range putts.")
    print_and_speak(review_text, engine)

def fitter(engine):
    intro_text = (
        "Justin, now that you know what you're options might be, let's get you fitted for a putter. "
        "Before we move on, I should mention, I've sent $300 from Sim's account to your account... So you can knock that off the price of the putter. "
        "Now, let's embark on a simple yet crucial fitting journey. Just a few minutes and a bit of cooperation are all we need."
        "Now I'll walk you through the process... Can you follow simple instructions? Can you? Are you sure....? Justin....? Sim, what do you think? Ok can you help him then? Great!")

    print_and_speak(intro_text, engine)
    input("Press the Enter to continue...")
    
    # Step 2: Shoes and Putter
    shoes_putter = (
        "Next, gear up in your golf shoes for consistency. "
        "Then, grab your go-to putter ... the one that feels just right in your hands. If Sim says it's ok, of course.")
    print_and_speak(shoes_putter, engine)
    input("Press the Enter to continue...")

    # Step 3: Find a Straightedge
    straightedge_text = (
        "Now, go stand infront of those cupboards over there, by the tv."
        "Remember, it should be 90 degrees upright.")
    print_and_speak(straightedge_text, engine)
    input("Press the Enter to continue...")
    # Step 4: Record a Video
    video_instructions = (
        "Here's the fun part! Ask that handsome brother of yours to film you. "
        "His perfect hair should stand about five or ten feet away, down the line of the putt. "
        "Hot stuff, Make sure the camera is around hand level, and the video captures your whole body. But you knew that already didn't you? Of course you did.")
    print_and_speak(video_instructions, engine)
    # User's Action
    input("Press Enter after you've recorded the video... ")

    # Step 5: Measure the Putter
    measure_putter = (
        "Almost there! Now, measure your putter length. "
        "Lay it flat, measure from the center of the face to the top of the grip, and jot down the length.")
    print_and_speak(measure_putter, engine)

    putter_length = input("Enter the length of your putter in inches: ")

    # Save the Results
    with open("fitting_results.txt", "w") as file:
        file.write(f"Putter Length: {putter_length}\n")

    thank_you = (
        "Fantastic! You've completed the fitting process. Congrats!! "
        "I've saved the details, and you're one step closer to a bespoke putting experience. ")
    
    print_and_speak(thank_you, engine)

    return putter_length

def lab_golf(engine):
    lab_golf_text = (
        "L.A.B. Golf was founded in 2014 by Sam Hahn, a former aerospace engineer. "
        "Sam's passion for golf and engineering led him to create a putter that would help him improve his game. "
        "After years of research and development, Sam created the Directed Force putter, which is now known as the DF 2.1. ")
    print_and_speak(lab_golf_text, engine)    

def main():
    engine = pyttsx3.init()

    # Set the engine to use Microsoft Hazel voice
    hazel_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0"
    engine.setProperty('voice', hazel_voice_id)

    # Adjust the rate of speech if necessary
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-1)  # Adjust the rate as needed

   
    # Personalized Introduction
    introduction = (
        "Ah, Justin, finally gracing the LAB with your presence. "
        "I'm Caddy, the brains behind the operation. "
        "You're here for insight into the art of putting, and who better to guide you than me? "
        "Today, we'll dive into the world of L.A.B. putters right? Crazy stuff going on over there. "
        "And don't worry, I'll make sure even a fake brit like yourself can grasp these concepts. "
        "Shall we begin our journey into the sophisticated realm of golf putters?")
    
    print_and_speak(introduction, engine)
    input("Press Enter to continue...")
   # Introduction
    while True:
       # Display menu options
       print("\nPlease choose an option:")
       print("1. Explore MEZZ.1 Putter")
       print("2. Explore Directed Force 2.1 Putter")
       print("3. Explore LINK.1 Putter")
       print("4. Conduct Home-Style Fitting")
       print("5. LAB Golf Technology, History and Story")
       print("6. Exit")


       # User choice
       choice = input("Enter your choice (1-6): ")


       # Execute the corresponding function based on user choice
       if choice == '1':
           explore_mezz1(engine)
       elif choice == '2':
           explore_df21(engine)
       elif choice == '3':
           explore_link1(engine)
       elif choice == '4':
           fitter(engine)    
       elif choice == '5':
           lab_golf(engine)
           
       elif choice == '6':
           print_and_speak("Thank you for exploring the LAB putters with me. Goodbye!", engine)
           break
       else:
           print_and_speak("Invalid choice, please try again.", engine)

# Run the program
if __name__ == "__main__":
   main()
