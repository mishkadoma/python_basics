class Song(object):

    def __init__(self, lyrics):
        self.text = lyrics

    def sing_me_a_song(self):
        for line in self.text:
            print line

happy_bday = Song(["happy birthday to you",
                   "I don't want to be sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "=" * 15
class Animal(object):

    def __init__(self, tale, color, sound):
        self.tale = tale
        self.color = color
        self.sound = sound

    def show_yourself(self, height):
        self.height = height
        print "I can catch a ball at the height of %d" % self.height
        print "Also! Tale: %s, Color: %s, Sound = %s" % (self.tale, self.color, self.sound)
        print "=" * 10

cat = Animal("yes", "brown", "meow")
dog = Animal("yes", "white", "woof")
turtle = Animal("nope", "green", "nope")

cat.show_yourself(24)
dog.show_yourself(100)
turtle.show_yourself(10)
