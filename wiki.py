# This is a program to pull information from Wikipedia

import wikipedia
import pyttsx3
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# When we "init the converter" what we are doing is telling Python to load the tts (text to speech module) so for those who may be more auditory learners or perhaps a person
# could potentially have vision problems which would hinder them from reading the screen this would take the output of their inquiry and speak it to them. But will also
# save the output to an output.txt file which will have all the information they searched ready for later use.
engine = pyttsx3.init()

# This next parameter will tell the tts converter how fast or how slow we want the information read back to us, depending on preferences this can be adjusted to the
# individuals liking.
engine.setProperty('rate', 150)

# This next parameter will tell the tts converter how load or soft we want the playback volume set, again depending on the individual user preference this can be adjusted as
# well.
engine.setProperty('volume', 2)



inquiry_list = []


def main():

    # This function along with the loop enables the program to take 3 different inputs from the User, Parse (Sort through), and summarize making it that much easier to digest     # a large amount of information in smaller pieces.
        # So with the way this is written if you wanted to append to this and print out even more information related to the topic you're researching then you'll be able too
        # without much trouble.



    print('''\n\n\n\t\t*** This AI is designed to take multiple pieces of information & summarizes them into something that can be used immediately and anyone can grab the gist 
         of the search ***\n\n''')
    ''' The main function is the brain of the function, it's what gives everything else the signal to do what it needs to do'''
    print("_" * 100, "\n")
    for i in range(0,3):
        inquiry = input("\n\n\n*** What would you like to know ***\n\n")
        inquiry_list.append(inquiry)
    for inquiry in inquiry_list:
        print("Inforation for {}".format(inquiry))
        print("-" * 100, "\n")


        # Now we will create a variable that will interact with the Wikipedia module in order for us to pull all the information that we need or are requesting
        pandoras_box = wikipedia.page(inquiry)

    
        # Now we will use our object to push out and display the data on the user's inquiry to the screen
        print("\n\n\n** Here's what you ordered " + inquiry + "***\n\n")
        print("_" * 100, "\n")


        print("\n\n\t\t*** SUMMARY ***\n\n")
        engine.say(pandoras_box.summary)
        print("_" * 100, "\n")
        # The parameter will speak the given information and then pause before continuing so everything doesn't just run one right into the other.
        engine.runAndWait()

        print("\n\n\t\t*** CONTENT ***\n\n")
        engine.say(pandoras_box.content)
        print("_" * 100, "\n")
        engine.runAndWait()


        print("\n\n\t\t*** REFERENCES ***\n\n")
        engine.say(pandoras_box.references)
        print("_" * 100, "\n")
        engine.runAndWait()

        # Now we till take all that information and save it to a file that we can use to file away for our records or set to the side for later use in another program
        file = open('output.txt', 'a')
        file.write(str(pandoras_box.summary))
        file.write(str(pandoras_box.content))
        file.write(str(pandoras_box.references))
        file.close()


if __name__ == "__main__":
        ''' If you see the main funtion, you know to let it ride!'''
        main()





