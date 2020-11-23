import json
import pandas as pd
from pathlib import Path

'''
Preserved for posterity as code has no longer any function after source of error was discovered and data had to be omitted
anyways. Fixes missing "list selectef from" by taking a set of movies to use as keys when browsing through json files.
Yeh it's pretty dumb.
'''


test =  [ "Baseline",
        {
          "0": {
            "Title": "Meet the Parents",
            "Lang": "en",
            "Cover_Path": "/wVjtQtzv9IcNRGnOOdcK797Sdxx.jpg",
            "Overview": "Greg Focker is ready to marry his girlfriend, Pam, but before he pops the question, he must win over her formidable father, humorless former CIA agent Jack Byrnes, at the wedding of Pam's sister. As Greg bends over backward to make a good impression, his visit to the Byrnes home turns into a hilarious series of disasters, and everything that can go wrong does, all under Jack's critical, hawklike gaze.",
            "Actors": "Ben Stiller, Robert De Niro, Teri Polo, Blythe Danner, Owen Wilson, Nicole DeHuff, Jon Abrahams, James Rebhorn, Tom McCarthy, Phyllis George, Kali Rocha, Bernie Sheredy, Judah Friedlander, Peter Bartlett, John Elsen, Mark Hammer, Amy Hohn, William Severs, John Fiore",
            "Genres": "Comedy, Romance",
            "Release": "2000-10-06",
            "Runtime": 108,
            "Directors": "Jay Roach",
            "MovieLensID": 3948
          },
          "1": {
            "Title": "Cars",
            "Lang": "en",
            "Cover_Path": "/5damnMcRFKSjhCirgX3CMa88MBj.jpg",
            "Overview": "Lightning McQueen, a hotshot rookie race car driven to succeed, discovers that life is about the journey, not the finish line, when he finds himself unexpectedly detoured in the sleepy Route 66 town of Radiator Springs. On route across the country to the big Piston Cup Championship in California to compete against two seasoned pros, McQueen gets to know the town's offbeat characters.",
            "Actors": "Owen Wilson, Paul Newman, Bonnie Hunt, Larry the Cable Guy, Tony Shalhoub, Cheech Marin, Michael Wallis, George Carlin, Paul Dooley, Jenifer Lewis, Guido Quaroni, Richard Petty, Michael Keaton, Katherine Helmond, John Ratzenberger, Joe Ranft, Jeremy Piven, Jeremy Clarkson, Dale Earnhardt Jr., Mario Andretti, Michael Schumacher, Jay Leno, Tom Hanks, Tim Allen, Billy Crystal, John Goodman, Dave Foley, Bob Costas, Darrell Waltrip, Richard Kind, Edie McClurg, Humpy Wheeler, Tom Magliozzi, Ray Magliozzi, Lynda Petty, Andrew Stanton, Sarah Clark, Mike Nelson, Joe Ranft, Jonas Rivera, Lou Romano, Adrian Ochoa, E.J. Holowicki, Elissa Knight, Lindsey Collins, Larry Benton, Douglas Keever, Sherry Lynn",
            "Genres": "Animation, Adventure, Comedy, Family",
            "Release": "2006-06-08",
            "Runtime": 117,
            "Directors": "John Lasseter, Joe Ranft",
            "MovieLensID": 45517
          },
          "2": {
            "Title": "Rise of the Planet of the Apes",
            "Lang": "en",
            "Cover_Path": "/ddWSWgAjAhksNhMeeBTSqY6otIA.jpg",
            "Overview": "Scientist Will Rodman is determined to find a cure for Alzheimer's, the disease which has slowly consumed his father. Will feels certain he is close to a breakthrough and tests his latest serum on apes, noticing dramatic increases in intelligence and brain activity in the primate subjects – especially Caesar, his pet chimpanzee.",
            "Actors": "James Franco, Freida Pinto, John Lithgow, Brian Cox, Tom Felton, Andy Serkis, David Oyelowo, Tyler Labine, Jamie Harris, Ty Olsson, David Hewlett, Chelah Horsdal, Jesse Reid, Joey Roche, Madison Bell, Makena Joy, B.J. Harrison, Mattie Hawkinson, Karin Konoval, Terry Notary, Richard Ridings, Christopher Gordon, Devyn Dalton, Jay Caputo, Leah Gibson, Tracy Spiridakos, Chris Shields, Lauren Watson",
            "Genres": "Thriller, Action, Drama, Science Fiction",
            "Release": "2011-08-03",
            "Runtime": 105,
            "Directors": "Rupert Wyatt",
            "MovieLensID": 88744
          },
          "3": {
            "Title": "Strictly Ballroom",
            "Lang": "en",
            "Cover_Path": "/ulA2RUGNvrwxbLDVUwxyB2eBl6P.jpg",
            "Overview": "Brave new steps put Scott's career in jeopardy. With a new partner and determination, can he still succeed?",
            "Actors": "Paul Mercurio, Tara Morice, Bill Hunter, Barry Otto, Pat Thomson, Gia Carides, Kris McQuade, Peter Whitford, John Hannan, Kerry Shrimpton, Sonia Kruger, Todd McKenney, Pip Mushin, Steve Grace",
            "Genres": "Comedy, Drama, Romance",
            "Release": "1992-08-20",
            "Runtime": 94,
            "Directors": "Baz Luhrmann",
            "MovieLensID": 1188
          },
          "4": {
            "Title": "Beneath the Planet of the Apes",
            "Lang": "en",
            "Cover_Path": "/pWXyweaAoFoprRHm9Ft33JakiQB.jpg",
            "Overview": "Astronaut Brent is sent to rescue Taylor but crash lands on the Planet of the Apes, just like Taylor did in the original film. Taylor has disappeared into the Forbidden Zone so Brent and Nova try to follow and find him. He discovers a cult of humans that fear the Apes' latest military movements and finds himself in the middle. Tension mounts to a climactic battle between ape and man deep in the bowels of the planet.",
            "Actors": "James Franciscus, Kim Hunter, Maurice Evans, Linda Harrison, Charlton Heston, Paul Richards, David Watson, Thomas Gomez, Victor Buono, James Gregory, Jeff Corey, Natalie Trundy, Don Pedro Colley, Tod Andrews, Gregory Sierra, Eldon Burke",
            "Genres": "Adventure, Science Fiction, Mystery",
            "Release": "1970-05-01",
            "Runtime": 95,
            "Directors": "Ted Post",
            "MovieLensID": 2530
          }
        } ]
verify = ["Baseline", {"53123.json": {"Title": "Once", "Lang": "en", "Cover_Path": "/fEjwJfeDxgsRBlYgEWMgvrKQ6VB.jpg", "Overview": "A vacuum repairman moonlights as a street musician and hopes for his big break. One day a Czech immigrant, who earns a living selling flowers, approaches him with the news that she is also an aspiring singer-songwriter. The pair decide to collaborate, and the songs that they compose reflect the story of their blossoming love.", "Actors": "Glen Hansard, Mark\u00e9ta Irglov\u00e1, Hugh Walsh, Gerard Hendrick, Alaistair Foley, Geoff Minogue, Bill Hodnett, Danuse Ktrestova, Darren Healy, Mal Whyte, Marcella Plunkett", "Genres": "Drama, Music, Romance", "Release": "2007-03-23", "Runtime": 85.0, "Directors": "John Carney", "MovieLensID": 53123}, "316.json": {"Title": "Stargate", "Lang": "en", "Cover_Path": "/39WsfbB5BshvdbPAYRFXdsjC481.jpg", "Overview": "An interstellar teleportation device, found in Egypt, leads to a planet with humans resembling ancient Egyptians who worship the god Ra.", "Actors": "Kurt Russell, James Spader, Jaye Davidson, Viveca Lindfors, Alexis Cruz, Mili Avital, Leon Rippy, John Diehl, French Stewart, Carlos Lauchu, Djimon Hounsou, Erick Avari, Derek Webster, Christopher John Fields, Gianin Loffler", "Genres": "Action, Adventure, Science Fiction", "Release": "1994-10-27", "Runtime": 121.0, "Directors": "Roland Emmerich", "MovieLensID": 316}, "1244.json": {"Title": "Manhattan", "Lang": "en", "Cover_Path": "/k4eT3EvfxW1L9Wmt04UqJqCvCR6.jpg", "Overview": "The life of a divorced television writer dating a teenage girl is further complicated when he falls in love with his best friend's mistress.", "Actors": "Woody Allen, Diane Keaton, Michael Murphy, Mariel Hemingway, Meryl Streep, Anne Byrne Hoffman, Karen Ludwig, Michael O'Donoghue, Wallace Shawn, Tisa Farrow, Charles Levin, Karen Allen, David Rasche, Mark Linn-Baker, Frances Conroy", "Genres": "Comedy, Drama, Romance", "Release": "1979-04-25", "Runtime": 96.0, "Directors": "Woody Allen", "MovieLensID": 1244}, "2355.json": {"Title": "A Bug's Life", "Lang": "en", "Cover_Path": "/u9qGMRwcPwP0WETxulS5hKUsEum.jpg", "Overview": "On behalf of oppressed bugs everywhere, an inventive ant named Flik hires a troupe of warrior bugs to defend his bustling colony from a horde of freeloading grasshoppers led by the evil-minded Hopper.", "Actors": "Dave Foley, Kevin Spacey, Julia Louis-Dreyfus, Hayden Panettiere, Phyllis Diller, Richard Kind, David Hyde Pierce, Joe Ranft, Denis Leary, Jonathan Harris, Madeline Kahn, Bonnie Hunt, Michael McShane, John Ratzenberger, Brad Garrett, Roddy McDowall, Edie McClurg, Alex Rocco, David Ossman, Sherry Lynn", "Genres": "Adventure, Animation, Comedy, Family", "Release": "1998-11-25", "Runtime": 95.0, "Directors": "John Lasseter", "MovieLensID": 2355}, "27706.json": {"Title": "Lemony Snicket's A Series of Unfortunate Events", "Lang": "en", "Cover_Path": "/dHQMAj9E2G2ewjN1aCOPubsZaj1.jpg", "Overview": "Three wealthy children's parents are killed in a fire. When they are sent to a distant relative, they find out that he is plotting to kill them and seize their fortune.  This movie is extremely alarming, an expression which here means a thrilling misadventure involving three ingenious orphans and a villainous actor named Count Olaf (Jim Carrey) who wants their enormous fortune.  It includes a suspicious fire, delicious pasta, Jim Carrey, poorly behaved looches, Billy Connolly, an incredibly deadly viper, Meryl Streep, and the voice of an imposter named Jude Law.", "Actors": "Jim Carrey, Meryl Streep, Jude Law, Emily Browning, Liam Aiken, Kara Hoffman, Shelby Hoffman, Timothy Spall, Billy Connolly, Luis Guzm\u00e1n, Jennifer Coolidge, Jane Adams, Craig Ferguson, Jamie Harris, Catherine O'Hara, Cedric the Entertainer, Dustin Hoffman, Bob Clendenin, Lenny Clarke, Fred Gallo, Amy Brenneman", "Genres": "Adventure, Comedy, Family", "Release": "2004-12-16", "Runtime": 108.0, "Directors": "Brad Silberling", "MovieLensID": 27706}, "370.json": {"Title": "The Naked Gun 33\u2153: The Final Insult", "Lang": "en", "Cover_Path": "/k3F8N3jeqXOpm1qjY7mL8O6vdx.jpg", "Overview": "Frank Drebin is persuaded out of retirement to go undercover in a state prison. There he is to find out what top terrorist, Rocco, has planned for when he escapes. Frank's wife, Jane, is desperate for a baby.. this adds to Frank's problems. A host of celebrities at the Academy awards ceremony are humiliated by Frank as he blunders his way trying to foil Rocco.", "Actors": "Leslie Nielsen, Priscilla Presley, George Kennedy, O.J. Simpson, Fred Ward, Kathleen Freeman, Anna Nicole Smith, Doris Belack, Nigel Gibbs, Andre Rosey Brown, James Earl Jones, Pia Zadora, Ellen Greene, Raye Birk, Wylie Small, Randall 'Tex' Cobb, Ann B. Davis, Vanna White, Weird Al Yankovic, Mary Lou Retton, David Zucker, Julie Strain, Florence Henderson, Elisa Gabrielli, Shannen Doherty, Morgan Fairchild, Elliott Gould, Mariel Hemingway, James Earl Jones, Raquel Welch, Symba, R. Lee Ermey", "Genres": "Comedy, Crime", "Release": "1994-03-18", "Runtime": 83.0, "Directors": "Peter Segal", "MovieLensID": 370}, "7.json": {"Title": "Sabrina", "Lang": "en", "Cover_Path": "/jQh15y5YB7bWz1NtffNZmRw0s9D.jpg", "Overview": "An ugly duckling having undergone a remarkable change, still harbors feelings for her crush: a carefree playboy, but not before his business-focused brother has something to say about it.", "Actors": "Harrison Ford, Julia Ormond, Greg Kinnear, Angie Dickinson, Nancy Marchand, John Wood, Richard Crenna, Lauren Holly, Dana Ivey, Fanny Ardant, Patrick Bruel, Paul Giamatti, Miriam Col\u00f3n, Elizabeth Franz, Val\u00e9rie Lemercier, Becky Ann Baker, John C. Vennema, Margo Martindale, J. Smith-Cameron, Christine Luneau-Lipton, Michael Dees, Denis Holmes, Jo-Jo Lowe, Ira Wheeler, Philippa Cooper, Ayako Kawahara, Fran\u00e7ois Genty, Guillaume Gallienne, In\u00e9s Sastre, Phina Oruche, Andrea Behalikova, Jennifer Herrera, Kristina Kumlin, Eva Linderholm, Carmen Chaplin, Micheline Van de Velde, Joanna Rhodes, Alan Boone, Patrick Forster-Delmas, Kentaro Matsuo, Peter McKernan, Ed Connelly, Ronald L. Schwary, Alvin Lum, Siching Song, Phil Nee, Randy Becker, Susan Browning, Anthony Mondal, Peter Parks, Woodrow Asai, Eric Bruno Borgman, Michael Cline, Christopher Del Gaudio, Philippe Hartmann, Jerry Quinn, Dori Rosenthal", "Genres": "Comedy, Romance", "Release": "1995-12-15", "Runtime": 127.0, "Directors": "Sydney Pollack", "MovieLensID": 7}, "1097.json": {"Title": "E.T. the Extra-Terrestrial", "Lang": "en", "Cover_Path": "/8htLKK03TJjKZOXJgihZCu8v0P.jpg", "Overview": "After a gentle alien becomes stranded on Earth, the being is discovered and befriended by a young boy named Elliott. Bringing the extraterrestrial into his suburban California house, Elliott introduces E.T., as the alien is dubbed, to his brother and his little sister, Gertie, and the children decide to keep its existence a secret. Soon, however, E.T. falls ill, resulting in government intervention and a dire situation for both Elliott and the alien.", "Actors": "Henry Thomas, Drew Barrymore, Robert MacNaughton, Dee Wallace, Peter Coyote, Erika Eleniak, Sean Frye, C. Thomas Howell, K. C. Martel, David M. O'Dell, Richard Swingler, Frank Toth, Pat Welsh", "Genres": "Science Fiction, Adventure, Family, Fantasy", "Release": "1982-04-03", "Runtime": 115.0, "Directors": "Steven Spielberg", "MovieLensID": 1097}, "1251.json": {"Title": "8\u00bd", "Lang": "it", "Cover_Path": "/5pQlc8dp5dXzWg1yM70DZrsDpOl.jpg", "Overview": "With 8 \u00bd Frederico Fellini leaves a self-portrait where dreams and reality are a mix. With help from a most excellent cast and unique scenery this self reflecting film is one of his master works.", "Actors": "Marcello Mastroianni, Claudia Cardinale, Anouk Aim\u00e9e, Sandra Milo, Rossella Falk, Barbara Steele, Madeleine Lebeau, Caterina Boratto, Eddra Gale, Guido Alberti, Mario Conocchia, Bruno Agostini, Cesarino Miceli Picardi, Jean Rougeul, Mario Pisu, Yvonne Casadei, Ian Dallas", "Genres": "Fantasy, Drama", "Release": "1963-02-14", "Runtime": 138.0, "Directors": "Federico Fellini", "MovieLensID": 1251}, "46578.json": {"Title": "Little Miss Sunshine", "Lang": "en", "Cover_Path": "/5ZuviyEOkelod8x5j5CWa45jsw2.jpg", "Overview": "A family loaded with quirky, colorful characters piles into an old van and road trips to California for little Olive to compete in a beauty pageant.", "Actors": "Greg Kinnear, Alan Arkin, Toni Collette, Steve Carell, Paul Dano, Abigail Breslin, Bryan Cranston, Beth Grant, Wallace Langham, Matt Winston, Julio Oscar Mechoso, Marc Turtletaub, Jill Talley, Brenda Canela, Chuck Loring, Justin Shilton, Gordon Thomson, Steven Christopher Parker, John Walcutt, Paula Newsome, Dean Norris, Lauren Shiohama, Mary Lynn Rajskub, Jerry Giles, Geoff Meed, Joan Scheckel, Mel Rodriguez, Casandra Ashe", "Genres": "Comedy, Drama", "Release": "2006-07-26", "Runtime": 102.0, "Directors": "Jonathan Dayton, Valerie Faris", "MovieLensID": 46578}} ]
genpath = "C:\\Output\\"
potentialMatch = []
#174056
fullpath = genpath + "1.json"
with open(fullpath) as f:
    checkdata = json.load(f)
print(test[1][str(1)]["MovieLensID"])
print(checkdata['Similarities']['Baseline'])

for x in range (1,174056):
    print(str(x) + "/174056")
    currentfile = str(x) + ".json"
    fullpath = Path(genpath + currentfile)
    if fullpath.is_file():
        with open(fullpath) as f:
            checkdata = json.load(f)
        '''
        for y in range(0, 5):
            print(matching[1][str(y)])
            print(str(checkdata['Similarities']['Baseline']))
            if str(test[1][str(y)]) in str(checkdata['Similarities']['Baseline']):
                print("match")
            else:
                break
            print("******************************************")
            potentialMatch.append(y)
        '''
        if str(test[1]["0"]["MovieLensID"]) in str(checkdata['Similarities']['Baseline']) and str(test[1]["1"]["MovieLensID"]) in str(checkdata['Similarities']['Baseline']) and str(test[1]["2"]["MovieLensID"]) in str(checkdata['Similarities']['Baseline']) and str(test[1]["3"]["MovieLensID"]) in str(checkdata['Similarities']['Baseline']) and str(test[1]["4"]["MovieLensID"]) in str(checkdata['Similarities']['Baseline']):
            potentialMatch.append(x)
    else:
        continue

print(potentialMatch)