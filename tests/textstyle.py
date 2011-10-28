"""
:mod:`ansicolors`
==========================

.. moduleauthor:: Dillon Hicks <hhicks@ittc.ku.edu>

"""

"""
Changelog 
=============

* (YYYY-MM-DD) : <change>

* (2009-12-07) : Original code

"""


class FontAttributes:
    """
    Holds all of the ANSI Escapes for styling console text.
    """
    class FontStyle:
        """
        More useful than a dictionary, since each value holds its name
        and escape value.  While the string method always returns the
        value for the color escape.
        """
        def __init__(self, name, value):
            self.name = name
            self.value = value
 
        def __str__(self):
            return self.value

    __PREFIX = '\x1b[%sm'
    
    RESET              = FontStyle('RESET', __PREFIX % '0')
    
    # reset; clears all colors and styles (to white on black)
    BOLD               = FontStyle('BOLD',__PREFIX % '1')
    ITALIC            = FontStyle('ITALIC',__PREFIX % '3')
    UNDERLINE          = FontStyle('UNDERLINE',__PREFIX % '5')
    # Inverses background and foreground
    INVERSE            = FontStyle('INVERSE',__PREFIX % '7')
    STRIKETHROUGH      = FontStyle('STRIKETHROUGH',__PREFIX % '9')
    BOLD_OFF           = FontStyle('BOLD_OFF',__PREFIX % '22')
    ITALIC_OFF        = FontStyle('ITALIC_OFF',__PREFIX % '23')
    UNDERLINE_OFF      = FontStyle('UNDERLINE_OFF',__PREFIX % '24')
    INVERSE_OFF        = FontStyle('INVERSE_OFF',__PREFIX % '27')
    STRIKETHROUGH_OFF  = FontStyle('STRIKETHROUGH_OFF',__PREFIX % '29')
    # Text Colors
    BLACK              = FontStyle('BLACK',__PREFIX % '30')
    RED                = FontStyle('RED',__PREFIX % '31')
    GREEN              = FontStyle('GREEN',__PREFIX % '32')
    YELLOW             = FontStyle('YELLOW',__PREFIX % '33')
    BLUE               = FontStyle('BLUE',__PREFIX % '34')
    PURPLE             = FontStyle('PURPLE',__PREFIX % '35')
    CYAN               = FontStyle('CYAN',__PREFIX % '36')
    WHITE              = FontStyle('WHITE',__PREFIX % '37')

    INTENSE_BLACK      = FontStyle('INTENSE_BLACK',__PREFIX % '90')
    INTENSE_RED        = FontStyle('INTENSE_RED',__PREFIX % '91')
    INTENSE_GREEN      = FontStyle('INTENSE_GREEN',__PREFIX % '92')
    INTENSE_YELLOW     = FontStyle('INTENSE_YELLOW',__PREFIX % '93')
    INTENSE_BLUE       = FontStyle('INTENSE_BLUE',__PREFIX % '94')
    INTENSE_PURPLE     = FontStyle('INTENSE_PURPLE',__PREFIX % '95')
    INTENSE_CYAN       = FontStyle('INTENSE_CYAN',__PREFIX % '96')
    INTENSE_WHITE      = FontStyle('INTENSE_WHITE',__PREFIX % '97')

    # Backgroup colors 
    BG_WHILE           = FontStyle('BG_WHITE',__PREFIX % '39')
    BG_BLACK           = FontStyle('BG_BLACK',__PREFIX % '40')
    BG_RED             = FontStyle('BG_RED',__PREFIX % '41')
    BG_GREEN           = FontStyle('BG_GREEN',__PREFIX % '42')
    BG_YELLOW          = FontStyle('BG_YELLOW',__PREFIX % '43')
    BG_BLUE            = FontStyle('BG_BLUE',__PREFIX % '44')
    BG_PURPLE          = FontStyle('BG_PURPLE',__PREFIX % '45')
    BG_CYAN            = FontStyle('BG_CYAN',__PREFIX % '46')
    BG_WHITE           = FontStyle('BG_WHITE',__PREFIX % '47')
    BG_BLACK           = FontStyle('BG_BLACK',__PREFIX % '49')
    
    
    BG_INTENSE_WHILE     = FontStyle('BG_INTENSE_WHITE',__PREFIX % '99')
    BG_INTENSE_BLACK     = FontStyle('BG_INTENSE_BLACK',__PREFIX % '100')
    BG_INTENSE_RED       = FontStyle('BG_INTENSE_RED',__PREFIX % '101')
    BG_INTENSE_GREEN     = FontStyle('BG_INTENSE_GREEN',__PREFIX % '102')
    BG_INTENSE_YELLOW    = FontStyle('BG_INTENSE_YELLOW',__PREFIX % '103')
    BG_INTENSE_BLUE      = FontStyle('BG_INTENSE_BLUE',__PREFIX % '104')
    BG_INTENSE_PURPLE    = FontStyle('BG_INTENSE_PURPLE',__PREFIX % '105')
    BG_INTENSE_CYAN      = FontStyle('BG_INTENSE_CYAN',__PREFIX % '106')
    BG_INTENSE_WHITE     = FontStyle('BG_INTENSE_WHITE',__PREFIX % '107')
    BG_INTENSE_BLACK     = FontStyle('BG_INTENSE_BLACK',__PREFIX % '109')
   
    NO_STYLE           = FontStyle('NO_STYLE', '')


    ALL_FONT_ATTRIBUTES = [ NO_STYLE,
                            BOLD, 
                            ITALIC,            
                            UNDERLINE, 
                            INVERSE, 
                            STRIKETHROUGH,
                            BLACK,              
                            RED,                
                            GREEN,              
                            YELLOW,             
                            BLUE,               
                            PURPLE,             
                            CYAN,               
                            WHITE,             
                            BG_WHILE,           
                            BG_BLACK,           
                            BG_RED,             
                            BG_GREEN,           
                            BG_YELLOW,          
                            BG_BLUE,            
                            BG_PURPLE,          
                            BG_CYAN,            
                            BG_WHITE,           
                            BG_BLACK,
                            
                            INTENSE_BLACK,              
                            INTENSE_RED,                
                            INTENSE_GREEN,              
                            INTENSE_YELLOW,             
                            INTENSE_BLUE,               
                            INTENSE_PURPLE,             
                            INTENSE_CYAN,               
                            INTENSE_WHITE,             
                            BG_INTENSE_WHILE,           
                            BG_INTENSE_BLACK,           
                            BG_INTENSE_RED,             
                            BG_INTENSE_GREEN,           
                            BG_INTENSE_YELLOW,          
                            BG_INTENSE_BLUE,            
                            BG_INTENSE_PURPLE,          
                            BG_INTENSE_CYAN,            
                            BG_INTENSE_WHITE,           
                            BG_INTENSE_BLACK,           
                           
                            ]    
    

    

def style_text(text, *styles):
    """
    Apply the styles to the text.
    :param styles: List of FontStyles
    """
    return "%s%s%s" % (''.join(map(lambda s: str(s),styles)), text, FontAttributes.RESET)


def bold_text(text):
    return "%s%s%s" % (FontAttributes.BOLD, text, FontAttributes.RESET)

def italic_text(text):
    return "%s%s%s" % (FontAttributes.ITALIC, text, FontAttributes.RESET)

def underline_text(text):
    return "%s%s%s" % (FontAttributes.UNDERLINE, text, FontAttributes.RESET)

############################################################
# COLORED TEXT
############################################################
def red_text(text):
    return "%s%s%s" % (FontAttributes.RED, text, FontAttributes.RESET)

def blue_text(text):
    return "%s%s%s" % (FontAttributes.BLUE, text, FontAttributes.RESET)

def green_text(text):
    return "%s%s%s" % (FontAttributes.GREEN, text, FontAttributes.RESET)

def cyan_text(text):
    return "%s%s%s" % (FontAttributes.CYAN, text, FontAttributes.RESET)

def purple_text(text):
    return "%s%s%s" % (FontAttributes.PURPLE, text, FontAttributes.RESET)

def yellow_text(text):
    return "%s%s%s" % (FontAttributes.YELLOW, text, FontAttributes.RESET)

def black_text(text):
    return "%s%s%s" % (FontAttributes.BLACK, text, FontAttributes.RESET)

def white_text(text):
    return "%s%s%s" % (FontAttributes.WHITE, text, FontAttributes.RESET)



def intense_red_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_RED, 
                         text, FontAttributes.RESET)

def intense_blue_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_BLUE, 
                         text, FontAttributes.RESET)

def intense_green_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_GREEN, 
                         text, FontAttributes.RESET)

def intense_cyan_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_CYAN, 
                         text, FontAttributes.RESET)

def intense_purple_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_PURPLE, 
                         text, FontAttributes.RESET)

def intense_yellow_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_YELLOW, 
                         text, FontAttributes.RESET)

def intense_black_text(text):
    return "%s%s%s" % (FontAttributes.INTENSE_BLACK, 
                         text, FontAttributes.RESET)



############################################################
# BOLDED and COLORED TEXT
############################################################
def bold_red_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.RED, 
                         text, FontAttributes.RESET)

def bold_blue_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.BLUE, 
                         text, FontAttributes.RESET)

def bold_green_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.GREEN, 
                         text, FontAttributes.RESET)

def bold_cyan_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.CYAN, 
                         text, FontAttributes.RESET)

def bold_purple_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.PURPLE, 
                         text, FontAttributes.RESET)

def bold_yellow_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.YELLOW, 
                         text, FontAttributes.RESET)

def bold_black_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.BLACK, 
                         text, FontAttributes.RESET)


def bold_intense_red_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_RED, 
                         text, FontAttributes.RESET)

def bold_intense_blue_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_BLUE, 
                         text, FontAttributes.RESET)

def bold_intense_green_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_GREEN, 
                         text, FontAttributes.RESET)

def bold_intense_cyan_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_CYAN, 
                         text, FontAttributes.RESET)

def bold_intense_purple_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_PURPLE, 
                         text, FontAttributes.RESET)

def bold_intense_yellow_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_YELLOW, 
                         text, FontAttributes.RESET)

def bold_intense_black_text(text):
    return "%s%s%s%s" % (FontAttributes.BOLD, FontAttributes.INTENSE_BLACK, 
                         text, FontAttributes.RESET)



############################################################
# ITALICED and COLORED TEXT
############################################################
def italic_red_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.RED, 
                         text, FontAttributes.RESET)

def italic_blue_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.BLUE, 
                         text, FontAttributes.RESET)

def italic_green_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.GREEN, 
                         text, FontAttributes.RESET)

def italic_cyan_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.CYAN, 
                         text, FontAttributes.RESET)

def italic_purple_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.PURPLE, 
                         text, FontAttributes.RESET)

def italic_yellow_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.YELLOW, 
                         text, FontAttributes.RESET)

def italic_black_text(text):
    return "%s%s%s%s" % (FontAttributes.ITALIC, FontAttributes.BLACK, 
                         text, FontAttributes.RESET)


############################################################
# UNDERLINED and COLORED TEXT
############################################################
def underline_red_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.RED, 
                         text, FontAttributes.RESET)

def underline_blue_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.BLUE, 
                         text, FontAttributes.RESET)

def underline_green_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.GREEN, 
                         text, FontAttributes.RESET)

def underline_cyan_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.CYAN, 
                         text, FontAttributes.RESET)

def underline_purple_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.PURPLE, 
                         text, FontAttributes.RESET)

def underline_yellow_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.YELLOW, 
                         text, FontAttributes.RESET)

def underline_black_text(text):
    return "%s%s%s%s" % (FontAttributes.UNDERLINE, FontAttributes.BLACK, 
                         text, FontAttributes.RESET)




if __name__ == '__main__':
        
    def gen_tests():
        for fa0 in FontAttributes.ALL_FONT_ATTRIBUTES:
            for fa1 in FontAttributes.ALL_FONT_ATTRIBUTES:
                yield (fa0, fa1)
    
    test_string = "This is the color module test string."
    for test_style in gen_tests():
        print style_text(test_string, *test_style)
