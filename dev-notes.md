# Raspberry Pi Workshop

## Supplies

- Raspberry Pi Zero W
  - Either WITH pin headers pre-soldered, otherwise we need to buy pin headers and I would be able to solder them before the workshop
- RGB LEDs (2)
- Red LEDs (3)
- 2 push buttons (preferably 1 red and 1 green, but colour is not necessarily important)
- 4x4 keypad
- 360 degree Servo Motor
- Popsicle sticks (at least 1 per person)
- General crafting supplies
  - Construction paper (all sorts!)
  - other stuff e.g. googly eyes, ribbon, glue, scissors, glitter, etc.
- everyone needs a laptop, Mac preferred (have not yet tested on Windows)
- (optional) Buzzer
- Breadboard (medium size)
- DHT 11 temperature sensor
- Resistors (220 ohms) <-- I can buy these
- Jumper wires (assorted: Male-Female, Male-Male, Female-Female) <-- I can buy these
  - Honestly it's worth buying a bunch of these since they're really cheap

## Unplugged Activity - Doing the Robot

## What is Code?

- instructions! tie this back to the unplugged activity

## Getting familiar with the Raspberry Pi and Learning Python - Code along

- Learn some commands using Python
  - print numbers, strings
  - variables
  - functions
  - loops
  - conditionals <--- haven't hit this yet...

- REFLECT AT THE END: How is this like the doing the robot activity?

"First, we need to turn the Raspberry Pi on. Start by plugging it in."

- Plug Raspberry Pi in, it'll blink for a little bit as it boots up
- Open up a terminal on your computer (Terminal on Mac, other terminal on Linux, PuTTY for windows)
- `ssh pi@_______` <-- the IP address of the Pi will be provided to you
  
"Welcome to the terminal! We are now connected to the Raspberry Pi. We can use the terminal to talk to the Pi, so we can ask it to do things. For example, let's ask it what the date is:"

`date` -> prints out the date
`cowsay hello!` -> prints out a cow to greet us

If we want to get our Pi to do really complex things, we can write "scripts" using a programming language. Then, we'll be able to use the terminal to tell the Pi to run all of the instructions in the script. The programming language that we'll use today is called Python.

For example, there's already a script loaded up in our Pi. Run `ls` to see what script we already have.

`ls` -> prints out `hello.py`

Hmm... I wonder what the hello.py script does? Since it's a `.py` script, that means we can "run" it using Python.

`python3 hello.py` -> "Hello! Welcome to the Raspberry Pi workshop!"

Neat! I'd like to see how this script was written. 

`rsubl hello.py` -> open up the script in Sublime

This script has some code written in the Python programming language. It lets us `print` some text to the screen. Edit the code a bit, save the page, and then run `python3 hello.py` in your terminal again.

Depending on the commands that we write in our Python script, we can make different things happen.

For example, we can print all kinds of things:

`print(1 + 1)` -> Wow, math!

Sometimes we want to save some values, so that we can deal with them later.

```py
name = "Nima"

print(name)

big_number = 1 + 4 + 5 + 10000 + 4

print(big_number)
```

When we save values like that, it's called a _variable_. We can do fun stuff with variables! For example, we can use them to fill in blanks, sort of like Madlibs!

```py
name = "Nima"
ice_cream = "Salted Caramel"

print("My name is " + name + ", and I like " + ice_cream)
```

## NEEDED: How to make a function?

We can use Python to do more than simple math and printing out values. In fact...

We can use Python to control the physical world!

## Turn on an LED

- Turn LED on and off

Our first goal today is to turn a small LED light on and off.

We'll begin by wiring up the LED to our Raspberry Pi using a breadboard.

*PICTURE OF HOW TO WIRE + EXPLANATION FOR WIRING*

Then, we'll need a new Python script called `led_on.py`. In your terminal, write `touch led_on.py` to create a new script. Then open it in your editor with `rsubl led_on.py`.

Here's what we'll write:

```py
from gpiozero import LED
from time import sleep

led = LED(17)

led.on()
sleep(2)
led.off()
```

*Explanation of how we're importing pre-built code to play with LEDs, etc*
*Sleep function is being used to make our program wait for 2 seconds*

Time to test it out! Run `python3 led_on.py`.

## Turn multiple LEDs on and off in a loop

Wire up two more LEDs (INCLUDE PICTURE)

In the terminal, create a new script with `touch led_loop.py`. Then open it with `rsubl led_loop.py`.

```py
from gpiozero import LED
from signal import pause
from time import sleep

led_1 = LED(17)
led_2 = LED(18)
led_3 = LED(19)

for i in range(3)
  led_1.on()
  sleep(1)
  led_1.off()
  led_2.on()
  sleep(1)
  led_2.off()
  led_3.on()
  sleep(1)
  led_3.off()

pause()
```

What we're using here is a "for loop". A loop allows us to run code multiple times. In this example, we're making the three lights blink on and off 3 times. Run `python3 led_loop.py` to see it happen!

## What is Physical Computing?

*Note: this is a good place to take a break from coding and have a bit of a discussion*

- what  does physical computing mean?
- why is it important?

## What EXACTLY is Raspberry Pi?

- history and use
- example projects:
  - temperature sensor, internet in a box, smart mirror
- PAIR activity: go online and do some research, then present to the class

## Project 1: Scavenger Hunt - Somewhat code along / Self-guided work session

Goal: Scavenger hunt to become familiar with Python, Raspberry Pi wiring, I/O, some HTTP requests

(This is sort of like an escape room situation)

Scenario!! We're looking for the location of a secret stash of dog pictures (or some other treasure), and we have a clue that will begin to show us the way! We'll need TWO secret codes. We need to make a button that will download the first of the secret codes, and then we'll need to that FIRST secret code to access the second code.

Since we'll be dealing with buttons, let's learn about to hook up buttons to our Pi first.

Create a new script (like we did before) called `button.py`. Open it up!

- Hook up a button to print "hello world"

*IMAGE OF HOW TO WIRE BUTTON TO PI*

```py
from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello world!")

button = Button(2)

button.when_pressed = say_hello

pause()
```

- speak to each point in the code above, specifically the function, and the when_pressed listener. We can hand-wave the pause() function a bit.

We can connect many buttons to our Pi, and each one can do something different.

- Hook up a second button to print something else

```py
from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Bye!")

button1 = Button(2)
button2 = Button(3)

button1.when_pressed = say_hello
button2.when_pressed = say_goodbye

pause()
```

For a bit more fun, let's connect a button to control something physical, like an LED. One way to do this is with this special `source` syntax.

- Hook up a button to control simple LED
- In a new file, `button_led.py`

```py
from gpiozero import Button, LED
from signal import pause

led = LED(17)
button = Button(2)

led.source = button # this line of code says "let the LED be controlled by the button"

pause()
```

- Use a button to make a GET request to the morse code server
- new file: `scavenger.py`

```py
import requests
from gpiozero import Button

button = Button(2)

def getSignal():
  response = requests.get('https://INSERTHEROKUAPPHERE.com/signal')
  message = response.json()
  print(message)

button.when_pressed = getSignal
```

- After retrieving morse code info, display it with blinking LED and buzzer
- Replace `print(message)` with `morse(message)`
  - loop needed, with translating functions

```py
import requests
from gpiozero import Button

button = Button(2)

# For reference, see morse_parse.py
# This would be split over a couple steps.

def morse(message):
  for letter in message:
    if letter == "0":
      beep()
    elif letter == "1":
      long_beep()
    else:
      space()

def getSignal():
  response = requests.get('https://INSERTHEROKUAPPHERE.com/signal')
  message = response.json()
  morse(message)

button.when_pressed = getSignal
```

Now press the button... and let's see what happens!

*Stretch Option, can also connect the buzzer to this*

Now that we have our signal being performed, we can translate to see what the signal means!

- D... O... G... S... (or something similar haha)
- Or maybe just a number (1... 3... 3... 7...) (10 digits)

- I'll have morse code sheets printed out for learners

- Translating the morse code message gives you a secret "phone number" to call. Wire up the key pad and use it to "call" the number, and then print out the result.

Our last step is to use the funky 4x4 keypad to to call the secret number.

- Note to Kass/Myself: this code is still being worked on to make it nice
- It is very similar to the previous exercise, but with a special kind of listener + fancy wiring for the number pad

## Project 2: Robot Buddy

Goal: Create your own robot with RGB LED eyes (controllable with key pad) and a waving arm (controllable with RED/GREEN buttons)

- Note to self... code for this is also still being worked on, but almost complete

- crafting time
  - design your robot!
  - construction paper to fit over the breadboard

The steps we'll go through for making our robot buddy are:

- Connect the eyes
- Set up a little waving arm
- STRETCH: Control the eyes with the key pad
- Demo!

We've seen how to connect a regular LED to our Raspberry Pi, but we'll be using special LEDs for our Robot Buddy's eyes. A regular LED only needs one input wire to let it know whether it should be ON or OFF. The LEDs that we'll use for the eyes are RGB LEDs. What does RGB mean?

These will need 3 input wires:

- 1 wire for the Red signal
- 1 wire for the Green signal
- 1 wire for the Blue signal

These LEDs will still have 1 ground wire.

-- Wire up first RGB LED, with graphic.

Great, now that this LED is wired up we'll want to pick what colour should be displayed.

Create a new script called `robot_buddy.py`.

We can control this first eye by picking how _red_, _green_, and _blue_ it should be.

```py
left_eye = RGBLED(red=9, green=10, blue=11)

left_eye.red = 1  # full red
sleep(1)
left_eye.red = 0.5  # half red
sleep(1)

left_eye.color = (0, 1, 0)  # full green
```

The second eye will be wired up similarly, but we'll connect it to different pins on the Pi.

```py
right_eye = RGBLED(red=9, green=10, blue=11)

right_eye.red = 1  # full red
sleep(1)
right_eye.red = 0.5  # half red
sleep(1)

right_eye.color = (0, 1, 0)  # full green
```

- What does RGB mean? How do we wire up an RGB LED?
  - use RGB LEDs to make eyes
    
- STRETCH: control eyes with key pad (Maybe not stretch!)
  - col 1, 2, 3: R, G, B
  - row 1, 2, 3, 4: off, 1/3, 2/3, 1
  - col 4: left, right, both, neither

Our Robot Buddy is going to have a waving arm! To control this arm we'll need to use a little servo motor.

## SLIDE: - What is a servo motor?

## SLIDE: WIRING FOR THE SERVO MOTOR

-- this actually depends on what servo Kass bought

1st step: move servo slightly in one direction, then stop. then move sero in opposite direction, and stop.

2nd step: hook up a button to control servo going in one direction (hold + release)
3rd step: hook up another button to control for the opposite direction

- use servo motor to make popsicle stick arm wave

## Reflection

Goal: Reflect on what we built today, and extend the reach of your knowledge by making connections to the outside world.

- What can we use sensors for?
- What does "Internet of Things" mean?
- How can we use LEDs, servos, and sensors to make our classrooms smart?

## Teacher Takeaways

- Similar to already existing workshops

## Two hour variation

Likely do part of the Python content and the Robot Buddy content.