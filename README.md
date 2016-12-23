# Pacman
# Final Project for UMBC CMSC 471 Artificial Intelligence
# Michael Kelbaugh, Matthew Landen, Celestine Wong
# UC Berkeley Pac-Man Projects
# http://ai.berkeley.edu/project_overview.html

# All you need to run the code is a standard Python 2.7 installation.
# If you get errors about not having the necessary Tkinter module (for graphics),
# you can install it from here: http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter

# Basic commands to get started:

# play the Pacman game manually:
cd Pacman/search
python pacman.py

# watch the Pacman reflex agent:
cd Pacman/multiagent
python pacman.py -p ReflexAgent --frameTime 0.1 -k 1

# watch the Pacman minimax agent:
cd Pacman/multiagent
python pacman.py -p MinimaxAgent --frameTime 0.1 -k 1

# watch Pacman train with reinforcement learning:
cd Pacman/reinforcement
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -n 60 -l mediumClassic 

# watch Pacman play after reinforcement learning:
cd Pacman/reinforcement
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic
