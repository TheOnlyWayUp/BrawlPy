import brawlpy
import asyncio

client = brawlpy.Client('your_token_here') # Enter your token here

async def brawlPy():
    club = await client.get_club("PVQ0RP90") # This gets the club, from the ID
    print(club) # Prints the club object
    print(club.description) # Prints the club description
    print('Attributes -', ', '.join(list(dir(club)))) # This prints all the attributes and methods, anything you can access with club.***
    print(club.name, club.tag, club.trophies) # Prints the club name, tag and trophies.
    
    for member in club.members:
        print(member) # Prints the name of every member in the club
    
    
asyncio.run(brawlPy())
