

if __name__ == "__main__":

    print(
        '''
        ** Welcome to Madlib game! **
        ** Process.. **
        1. You have to enter these variable..
            - Adjective.
            - A First Name.
            - Past Tense Verb.
            - Plural Noun.
            - Large Animal.
            - Small Animal.
            - A Girl's Name.
            - Number 1-50.
            - Number.
        2. The App. will replace the inputs with words that between curly brackets:
        `Make Me A Video Game!
        I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!
        What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find. `
        '''
    )


    def write_madlib_file():
        with open("./assets/madlib.txt","w") as f:
            f.write(
                "Make Me A Video Game!\nI the {Adjective} and {Adjective} {A_First_Name} have {Past_Tense_Verb}{A_First_Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural_Noun}!\nWhat are a {Large_Animal} and backpacking {Small_Animal} to do? Before you can help {A_Girl_Name}, you'll have to collect the {Adjective} {Plural_Noun} and {Adjective} {Plural_Noun} that open up the {Number_1to50} worlds connected to A {A_First_Name} Lair. There are {Number} {Plural_Noun} and {Number} {Plural_Noun} in the game, along with hundreds of other goodies for you to find."
                )
    
    def modify_madlib_content():
        write_madlib_file()
        try:
            f = open("./assets/madlib.txt")
        except FileNotFoundError:
            print("file doesn't exist")
        else:
            content = f.read()
            f.close()
            with open("./assets/madlib.txt","w") as f:
                f.write(
                    content.format(
                        Adjective = input("Enter an Adjective.. "),
                        A_First_Name = input("Enter an A First Name.. "),
                        Past_Tense_Verb = input("Enter an Past Tense Verb.. "),
                        Plural_Noun = input("Enter an Plural Noun.. "),
                        Large_Animal = input("Enter an Large Animal.. "),
                        Small_Animal = input("Enter an Small Animal.. "),
                        A_Girl_Name = input("Enter an A Girl's Name.. "),
                        Number_1to50 = input("Enter an Number 1-50.. "),
                        Number = input("Enter an Number.. ")
                    )
                )
        finally:
            with open("./assets/madlib.txt","r") as f:
                content = f.read()
            return content
    print(modify_madlib_content())



def read_template(path):
    try:
        f = open(f'madlib_cli/{path}')
    except:
        raise FileNotFoundError
    else:
        content = f.read()
        f.close()
        return content



def parse_template(str):

        stripped = str.format(Adjective = "{}", Noun = "{}")
        split_parts = str.split()
        parts = ()
        for i in split_parts:
            if i == "{Adjective}":
                parts = parts + ("Adjective",)
            elif i == "{Noun}" or i =='{Noun}.':
                parts = parts + ("Noun",)
        return stripped,parts


def merge(str,words):
        return str.format(*words)












