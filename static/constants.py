DEFAULT_COLUMN_COUNT = 26
DEFAULT_ROW_COUNT = 45

DEFAULT_COLUMN_WIDTH = 92
DEFAULT_ROW_HEIGHT = 24
DEFAULT_FONT_FAMILY = "Arial"
DEFAULT_FONT_SIZE = "12px"
DEFAULT_COLOR = "rgb(0, 0, 0)"
DEFAULT_FILL = "rgb(255, 255, 255)"
DEFAULT_STYLE = "normal"
DEFAULT_TEXT_ALIGN = "right"
DEFAULT_VERTICAL_ALIGN = "bottom"
DEFAULT_FONT_STYLE = "normal"
DEFAULT_FONT_WEIGHT = "normal"

DEFAULT_STYLE = {
    "font-family": DEFAULT_FONT_FAMILY,
    "font-size": DEFAULT_FONT_SIZE,
    "font-style": DEFAULT_FONT_STYLE,
    "color": DEFAULT_COLOR,
    "background-color": DEFAULT_FILL,
    "vertical-align": DEFAULT_VERTICAL_ALIGN,
    "font-weight": DEFAULT_FONT_WEIGHT,
    "text-align": DEFAULT_TEXT_ALIGN,
}

COMPLETION_KINDS_CHART = "charts"
COMPLETION_KINDS_IMPORT = "import"
COMPLETION_KINDS_LOAD = "load"
COMPLETION_KINDS_DATAFRAME = "dataframe"
COMPLETION_KINDS_NONE = ""

CLEAR_CHUNK_SIZE = 150
ANIMATION_DURATION_FAST = 250
ANIMATION_DURATION_MEDIUM = 500
ANIMATION_DURATION_SLOW = 1000
ANIMATION_DURATION = ANIMATION_DURATION_FAST

SHEET = "s"

ICON_HOUR_GLASS = "⏳"
ICON_DATAFRAME = "🐼"
ICON_STAR = "⭐"
ICON_JSON = "🔲"
ICON_PLOT = "📊"
ICON_LIST = "↕"

OTHER_EDITOR_TIMEOUT = 60

MODE_PRODUCTION = "prod"
MODE_DEVELOPMENT = "dev"
WORKER_LOADING = "Loading..."

MIN_PASSWORD_LENGTH = 8

PREVIEW_HEADER_WIDTH = 56
PREVIEW_HEADER_HEIGHT = 32

IMAGE_COLORS = [ "#3B71CA", "#9FA6B2", "#14A44D", "#DC4C64", "#E4A11B", "#54B4D3", "#FBFBFB", "#332D2D" ]

FONT_NAMES = [ "Arial", "Courier", "Roboto" ]
FONT_SIZES = list(range(6, 21)) + list(range(24, 73, 4))

SAVE_DELAY = 5

TOPIC_WORKER_PRINT = "worker.print"
TOPIC_WORKER_COMPLETION = "worker.completion"
TOPIC_WORKER_COMPLETE = "worker.complete"
TOPIC_WORKER_CODE_COMPLETE = "worker.code.complete"
TOPIC_WORKER_CODE_COMPLETION = "worker.code.completion"

DATA_KEY_VALUE = "V"
DATA_KEY_COLUMNS = "C"
DATA_KEY_CELLS = "D"
DATA_KEY_CELLS_ENCODED = "DE"
DATA_KEY_ROWS = "R"
DATA_KEY_IMAGES = "I"
DATA_KEY_NAME = "N"
DATA_KEY_TIMESTAMP = "T"
DATA_KEY_STATUS = "S"
DATA_KEY_STACK = "V"
DATA_KEY_UID = "U"
DATA_KEY_EDITS = "E"
DATA_KEY_ENTRIES = "F"
DATA_KEY_ERROR = "G"
DATA_KEY_SCREENSHOT = "X"
DATA_KEY_PASSWORD = "P"
DATA_KEY_URL = "u"
DATA_KEY_TOKEN = "t"
DATA_KEY_MESSAGE = "M"
DATA_KEY_WHEN = "W"
DATA_KEY_TITLE = "z"
DATA_KEY_IDS = "y"
DATA_KEY_WIDTH = "a"
DATA_KEY_HEIGHT = "b"
DATA_KEY_EMAIL = "c"
DATA_KEY_PASSWORD = "d"
DATA_KEY_EXPIRATION = "e"
DATA_KEY_RESULT = "g"
DATA_KEY_LOGS = "h"
DATA_KEY_PREVIEWS = "i"
DATA_KEY_EDITOR_HEIGHT = "j"
DATA_KEY_CELL = "k"
DATA_KEY_CURRENT = "l"
DATA_KEY_EDITOR_WIDTH = "m"
DATA_KEY_PACKAGES = "n"
DATA_KEY_BEFORE = "o"
DATA_KEY_AFTER = "p"
DATA_KEY_CODE = "q"
DATA_KEY_RUNTIME = "r"
DATA_KEY_CONSOLE_FILTER = "s"
DATA_KEY_PROMPT = "v"
DATA_KEY_COLUMN_COUNT = "w"
DATA_KEY_ROW_COUNT = "x"
DATA_KEY_USER = "y"
DATA_KEY_START = "z"

DATA_KEY_VALUE_FORMULA = "vf"
DATA_KEY_VALUE_KIND = "vk"
DATA_KEY_VALUE_PREVIEW = "vp"
DATA_KEY_VALUE_FONT_FAMILY = "vff"
DATA_KEY_VALUE_FONT_SIZE = "vfs"
DATA_KEY_VALUE_FONT_WEIGHT = "vfw"
DATA_KEY_VALUE_FONT_STYLE = "vfu"
DATA_KEY_VALUE_LAYOUT = "vl"
DATA_KEY_VALUE_COLOR = "vc"
DATA_KEY_VALUE_FILL = "vb"
DATA_KEY_VALUE_STYLE = "vs"
DATA_KEY_VALUE_EMBED = "ve"
DATA_KEY_VALUE_VERTICAL_ALIGN = "vva"
DATA_KEY_VALUE_TEXT_ALIGN = "vta"

PUBSUB_STATE_ID = "State"
PUBSUB_SHEET_ID = "Application"