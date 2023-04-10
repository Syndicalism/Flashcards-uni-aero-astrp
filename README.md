
The setup instructions can be a bit annoying so I'll go through em here


# 1 Install Software

Install anki: https://apps.ankiweb.net/

Install obsidian: https://obsidian.md/

# 2 Obsidian

Clone this github repo to your local machine, then open it in obsidian as a vault.

Once opened trust the plugins.

# 3 Setup plugin

This link will explain how to setup obsidian to anki: https://github.com/Pseudonium/Obsidian_to_Anki

# 4 Clear old ID's and metadata

When the plugin generates anki flashcards from the obsidian text it will add a ID at the bottom:
![[]](https://cdn.discordapp.com/attachments/1061627987860140064/1094929014390538260/image.png)

Since your cloning my repositry it will come with my ID's which will not work on your local machine. So before you can generate flashcards you will have to remove all of these... luckily I made a bit of python code that will do that for you located at: Flashcards-uni-aero-astrp\Year 2\ClearIDs.py. Note that if you have already generated flashcards before you will have to delete all cards currently in Anki to re import them. AKA you will loose stored data on memorisation progress.

Beyond just clearing ID's the plugin also stores image data locally which is a pain in the ass, so you'll have to clear that too. So click these buttons:

![[]](https://cdn.discordapp.com/attachments/1061627987860140064/1094930248782581830/image.png)

# 5 Generating cards

For this stage you need to have anki open, in obsidian press the button: 

![[]](https://cdn.discordapp.com/attachments/1061627987860140064/1094930881237491752/image.png)

Now all cards should have an ID, like what was shown in step (4). If any pages don't then you'll have to flag the page as "changed" to do this add literally any random text at the 3rd line of a file. This flags the file as changed so when you press the export cards button again it will re evaluate that page.

Anki cards should look something like this once properly exported:

![[]](https://cdn.discordapp.com/attachments/1061627987860140064/1094930659010674758/image.png)

![[]](https://cdn.discordapp.com/attachments/1061627987860140064/1094932310081679410/image.png)

# 6 Study

Anki is highly customisable so if you want to get more out of it than the typical features look things up. It's designed to be used repeatedly over a while so to get best results use it daily.

I'll be adding new cards to the repo for a while so if I do you may have to repeat steps 4 -> 5 if you want the new cards.
