POSITION_NAMES = [
    "GK", 
    "CWP", 
    "CB",  
    "SB", 
    "DMF", 
    "WB", 
    "CMF", 
    "SMF", 
    "AMF", 
    "WF", 
    "SS", 
    "CF",
]

EDITED_TEAM_NAMES = [
    "<Edited> National 1",
    "<Edited> National 2",
    "<Edited> National 3",
    "<Edited> National 4",
    "<Edited> National 5",
    "<Edited> National 6",
    "<Edited> National 7",
    "<Edited>",
]


SHOP_TEAM_NAMES = [
    "<Shop 1>",
    "<Shop 2>",
    "<Shop 3>",
    "<Shop 4>",
    "<Shop 5>",
]

SHOP_TEAM_NAMES_5 = [
    "<Shop 1>",
    "<Shop 2>",
    "<Shop 3>",
    "<Shop 4>",
]

ML_TEAM_NAME = [
    "<ML Default>",
]
ML_TEAM_NAMES_EXTRAS = [
    "<ML Default Extra 1>", 
    "<ML Default Extra 2>",
]

PLAYER_FILTER_EXTRA = [
    "Free Agents",
    "ML Default", 
    "Shop", 
    "ML Youth", 
    "ML Old", 
    "Unused Players", 
    "Edited Players", 
    "All Players",
]

UTF_8 = "utf-8"

UTF_16_LE = "utf-16-le"

YES_NO = [
    "Yes", 
    "No",
]

NO_YES = [
    "No", 
    "Yes",
]

ON_OFF = [
    "On", 
    "Off",
]

OFF_ON = [
    "Off", 
    "On",
]

FONT_CURVE = [
    "Linear",
    "Light",
    "Medium",
    "Maximum",
]

OFF_LEFT_RIGHT = [
    "Off",
    "Left",
    "Right",
]

READ_MODE = "r"

WRITE_MODE = "w"

APPEND_MODE = "a"

NEWLINE = ""

COMMA_SEPARATOR = ","

CSV_COLUMNS=([
    # Player basic settings
    "ID","NAME","SHIRT_NAME", "CALLNAME ID", "NATIONALITY", 
    "AGE", "STRONG FOOT", "INJURY TOLERANCE", 
    "DRIBBLE STYLE", "FREE KICK STYLE", "PK STYLE", "DROP KICK STYLE", 
    "GOAL CELEBRATION 1", "GOAL CELEBRATION 2",
    "GROWTH TYPE",

    # Player position settings
    "FAVOURED SIDE", "REGISTERED POSITION", "GK  0", "CWP  1", "CBT  2", "SB  3", "DMF  4", "WB  5", "CMF  6", "SMF  7", "AMF  8", "WF 9","SS  10","CF  11",

    # Player ability settings
    "ATTACK", "DEFENSE", "BALANCE", "STAMINA", "TOP SPEED", "ACCELERATION", "RESPONSE", "AGILITY", "DRIBBLE ACCURACY", "DRIBBLE SPEED", "SHORT PASS ACCURACY",
    "SHORT PASS SPEED", "LONG PASS ACCURACY", "LONG PASS SPEED", "SHOT ACCURACY", "SHOT POWER", "SHOT TECHNIQUE", "FREE KICK ACCURACY", "SWERVE", "HEADING", "JUMP", "TECHNIQUE", 
    "AGGRESSION", "MENTALITY", "GOAL KEEPING", "TEAM WORK", "CONSISTENCY", "CONDITION / FITNESS", "WEAK FOOT ACCURACY", "WEAK FOOT FREQUENCY",

    # Player special abilities settings
    "DRIBBLING", "TACTICAL DRIBBLE", "POSITIONING", "REACTION", "PLAYMAKING", 
    "PASSING", "SCORING", "1-1 SCORING", "POST PLAYER",
    "LINES", "MIDDLE SHOOTING", "SIDE", "CENTRE", "PENALTIES", "1-TOUCH PASS", 
    "OUTSIDE", "MARKING", "SLIDING", "COVERING", "D-LINE CONTROL",
    "PENALTY STOPPER", "1-ON-1 STOPPER", "LONG THROW",

    # Player appearence settings
    # Head
    "FACE TYPE", "SKIN COLOUR", 
    "HEAD HEIGHT", "HEAD WIDTH", 
    "FACE ID", #"HEAD OVERALL POSITION",
    #"BROWS TYPE", "BROWS ANGLE", "BROWS HEIGHT", "BROWS SPACING",
    #"EYES TYPE", "EYES POSITION" , "EYES ANGLE", "EYES LENGTH", "EYES WIDTH", "EYES COLOUR 1", "EYES COLOUR 2",
    #"NOSE TYPE", "NOSE HEIGHT", "NOSE WIDTH",
    #"CHEECKS TYPE", "CHEECKS SHAPE",
    #"MOUTH TYPE", "MOUTH SIZE", "MOUTH POSITION",
    #"JAW TYPE", "JAW CHIN", "JAW WIDTH",
    # Hair
    "HAIR ID", "IS SPECIAL HAIRSTYLE 2",
    #"HAIR TYPE", "HAIR SHAPE", "HAIR FRONT", "HAIR VOLUME", "HAIR DARKNESS",
    #"HAIR COLOUR CONFIG", "HAIR COLOUR RGB R", "HAIR COLOUR RGB G", "HAIR COLOUR RGB B", 
    #"BANDANA", #"BANDANA COLOUR",
    #"CAP (ONLY GK)", "CAP COLOUR",
    #"FACIAL HAIR TYPE", "FACIAL HAIR COLOUR",
    #"SUNGLASSES TYPE", "SUNGLASSES COLOUR",

    # Physical
    "HEIGHT", "WEIGHT", #"BODY TYPE",
    #"NECK LENGTH", "NECK WIDTH", "SHOULDER HEIGHT", "SHOULDER WIDTH", "CHEST MEASUREMENT", "WAIST CIRCUMFERENCE", "ARM CIRCUMFERENCE", "LEG CIRCUMFERENCE", "CALF CIRCUMFERENCE", "LEG LENGTH", 

    # Boots/Acc.
    #"BOOT TYPE", "BOOT COLOUR",
    #"NECK WARMER", "NECKLACE TYPE", "NECKLACE COLOUR", "WISTBAND", "WISTBAND COLOUR", "FRIENDSHIP BRACELET", "FRIENDSHIP BRACELET COLOUR", "GLOVES",
    #"FINGER BAND", "SHIRT", "SLEEVES", "UNDER SHORT", "UNDER SHORT COLOUR", "SOCKS", "TAPE",

    "NATIONAL TEAM", "CLUB TEAM", 
    "FREE AGENT",
])


ALT_ITEMS = [
    "Normal",
    "Strategy Plan A",
    "Strategy Plan B",
]

INJURY_VALUES = [
    "C", 
    "B", 
    "A",
]

FOOT_FAV_SIDE = [
    "R", 
    "L", 
    "B",
]

FACE_TYPE = [
    "BUILD", 
    "ORIGINAL", 
    "PRESET",
]

BUILD = 0
ORIGINAL = 1
PRESET = 2

EYES_COLOURS = [
    "BLACK 1", 
    "BLACK 2", 
    "DARK GREY 1", 
    "DARK GREY 2", 
    "BROWN 1", 
    "BROWN 2", 
    "LIGHT BLUE 1", 
    "LIGHT BLUE 2", 
    "BLUE 1", 
    "BLUE 2", 
    "GREEN 1", 
    "GREEN 2",
]

GROWTH_TYPE_DEFAULT_VALUES = [
    9, 
    51, 
    55, 
    11, 
    8, 
    10,
]

GROWTH_TYPE_NAMES = [
    "Early Peak", 
    "Early/Lasting",
    "Standard", 
    "Std/Lasting", 
    "Late peak", 
    "Late/Lasting",
]

SUPP_COLOURS = [
    "Black", 
    "Dark Blue", 
    "Red", 
    "Pink", 
    "Lime", 
    "Light Blue", 
    "Yellow", 
    "White", 
    "Grey", 
    "Navy Blue", 
    "Maroon", 
    "Purple", 
    "Dark Green", 
    "Gold", 
    "Orange",
]

SUPP_COLOURS_HEX = [
    "#000000", "#0000ca", "#c20200", "#ffbfc5", "#acff2e", 
    "#aad6e6", "#fcff00", "#f7f8f5", "#7d7e7b", "#00047a", 
    "#870001", "#81007f", "#006100", "#fed500", "#fea500", 
]

KIT_TYPES = [
    "GA",
    "PA",
    "GB",
    "PB",
]

GA = 0
PA = 1
GB = 2
PB = 3


STATS_BG_COLOURS = (
    "SystemWindow", 
    "#3bb143", 
    "#ffff00", 
    "#fea500", 
    "#fe6666"
)

STATS_1_8_BG_COLOURS = (
    "SystemWindow", 
    "#fea500", 
    "#fe6666",
)


MIN_FACE_IDX = 1
MAX_FACE_IDX = 4096

MIN_HAIR_IDX = 1
MAX_HAIR_IDX = 4096

BODY_TYPES = (
    "1", 
    "2", 
    "3", 
    "4", 
    "5", 
    "6", 
    "7", 
    "8", 
    "Edit",
)

BODY_TYPES_VALUES = (
    (
        -1, 
        0, 
        -2, 
        -2, 
        -1, 
        0, 
        -1, 
        1, 
        0, 
        -2,
    ),
    (
        -2, 
        0, 
        1, 
        1, 
        2, 
        0, 
        1, 
        1, 
        0, 
        -1,
    ),
    (
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0, 
        0,
    ),
    (
        0, 
        0, 
        1, 
        1, 
        0, 
        0, 
        0, 
        -1, 
        -2, 
        2,
    ),
    (
        2,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        -2,
        4,
    ),
    (
        -3, 
        0, 
        3, 
        1, 
        0, 
        0, 
        2, 
        3, 
        2, 
        -2,
    ),
    (
        -1, 
        0, 
        0, 
        2, 
        0, 
        0, 
        0, 
        1, 
        0, 
        2,
    ),
    (
        -2, 
        0, 
        2, 
        2, 
        2, 
        0, 
        2, 
        2, 
        0,
        2,
    ),
)

MAIN_WINDOW_H = 700
MAIN_WINDOW_W = 800


