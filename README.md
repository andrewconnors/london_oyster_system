# London Tube Code Challenge
## Andrew Connors
## Jul 02, 2023

**Summary**: Mock of the London Oyster Train System


## How to run
I ran this with python3.11 installed via homebrew on a mac. I'm guessing it will work with anything >= python3.8. I made a concious effort to build this with only the standard library where possible to make it easy to run on any machine. If I had more time, I would have set this up with a setup.py file but because of the simplicity of the libraries, you should be able to run this with vanilla python. The only non-vanilla package in here is sqlite3 but the database isn't used in the code, the reason it is there is explained in "Design Choices" below.

1. Clone this repository
2. `cd` into the 'app' folder
3. run the tests in the test folder with `python3 -m unittest test/tests.py`

## Design
This is a very limited mock implementation of the London Oyster system. I spent about 3 hours on the code and then an extra little bit packaging it up and writing this description. Due to time constraints and guidance, I opted to convey that the system works through tests. You can find them in the `app/test/tests.py` file. The example trip given in the doc is coded into the final test case along with a few edge cases I thought would be cool to test.

### Explanation of Design Choices
I just want to call out a couple of choices I made when designing the program in case there are outstanding questions.

**ICard** - The idea here was to create an interface so that multiple types of cards can be easily added as needed. We could
have internet enabled cards, phones that act as cards, and test cards (like the MockCard class implemented in the code). As
long as they implement the ICard interface, the code will support it.

**locations.db** - I have a storage folder that doesn't really get used. The idea here was that in practice, we would be looking
up available locations in some sort of storage system. I opted to use an sqlite db because they're small, efficient, and can live alongside a small program. In this limited implementation it isn't used, as I just pass hardcoded locations in through the 
test file but it's there to show how I was thinking it might work in production.

### Changes I would make if I had more time

**Terminal** - There's really no distinction in my code between an "in" terminal and an "out" terminal, this was an oversight on
my end. The representation I have makes sense in this limited system but in prod, we would want a way to differentiate between the two

**UI** - I know I wasn't supposed to write a UI so I opted to show the code works through tests. If I had more time, I would have added a small CLI to interact with the program

**Logging**- I'm interested to see how a logging system would look on my implementation. We would need telemetry to be able to analyze usage patterns, dig into bugs, and audit transactions. I'm not sure how much would live in the card and how much would live in the terminal but if I was working on this for longer I'd be interested to dig into that.
