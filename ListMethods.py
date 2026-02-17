dna = ['AUG', 'AUC', 'UCG']

# .append() method adds an item to the end of the list.
# .insert() method adds an item to a specific index.
# .remove() method removes an item from a list based on the value.
# .pop() method removes the item at a particular index.

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']

print(dna)

# .append()	Add an item to the end of the list
# .clear()	Remove all items from the list
# .copy()	Return a shallow copy of the list
# .count()	Return the number of times the value appears in the list
# .extend()	Appends another list to the current list by extending it
# .index()	Returns the index of a value inside the list
# .insert()	Insert an item at a specified position in the list
# .pop()	Remove an item from a specified position in the list
# .remove()	Remove an item from the list based on the value of the item
# .reverse()	Reverses the list in place
# .sort()	Sorts the list in place

books = ["Harry Potter",
         "1984",
         "The Fault in Our Stars",
         "The Mom Test",
         "Life in Code"]

books.append("Pachinko")
books.remove("The Fault in Our Stars")
books.pop(1) # Doesn't require " " because it is removing a certain index, not value.

print(books)

playlist = ['Porches - rangerover',
            'Mount Eerie - You Swan, Go On',
            'Carolyn Polachek - Look at Me Now',
            'Pinegrove - Darkness',
            'LVL UP - Spirit Was',
            'Mitski - First Love / Late Spring']

# Loop through and simply print every value.

for i in playlist:
  print(i)

# Loop through and print every value at every index in the list.

for i in range(len(playlist)):
  print(playlist[i])

# List of achievements for the year, example:

things_to_do = [
  "🐍 Learn Python to an employable level",
  "💻 Begin to learn HTML, CSS and JavaScript",
  "🏫 Graduate with an exceptional grade in my degree",
  "🏖️ Treat myself to a nice holiday abroad",
  "💪 Get back into exercising more frequently",
  "🍕 Eat more food I've never tried before",
  "🏡 Make more effort to see family more frequently",
  "🎥 Finish my LetterBoxd list of films",
  "🇪🇸 Further my understanding of the Spanish language"
]

# I can structure a list like this with the [] OR as previously structured.

for i in things_to_do:
  print(i)

# print(things_to_do) would print the list as it is, all in one line with the [] and " ".
# for i in things_to_do would print each item on a new line without the [] and " ", because it is a loop.