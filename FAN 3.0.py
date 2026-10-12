import json
import math
import os
import sys
import html
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkfont
from datetime import datetime
from pathlib import Path

# --- THEME CONFIGURATION ---
COLORS = {
    "bg": "#0E1116",
    "sidebar": "#141820",
    "card": "#181D26",
    "card_hover": "#212835",
    "input_bg": "#10141B",
    "border": "#262D3A",
    "border_hover": "#3B475C",
    "btn": "#202734",
    "btn_hover": "#2B3547",
    "text_main": "#E6E9EF",
    "text_sub": "#9BA4B5",
    "text_dim": "#667085",
    "accent_blue": "#2F8CFF",
    "accent_grad": "#8B5CF6",
    "success": "#34D399",
    "danger": "#F87171",
    "warning": "#FBBF24",
    "selected": "#23426E",
    "toggle_off": "#3A4354",
}

FONTS = {}  # filled by init_fonts() once a Tk root exists

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
SNAPSHOT_DIR = os.path.join(SCRIPT_DIR, "snapshots")
IS_MAC = sys.platform == "darwin"

FAMOUS_ACCOUNTS = {
     'donbrutar', 'hyperkong_', 'fen.sektor', '4a1axd', 'bobby',
    'taylorswift', 'arianagrande', 'justinbieber', 'selenagomez', 'rihanna',
    'beyonce', 'drake', 'billieeilish', 'edsheeran', 'theweeknd',
    'ladygaga', 'shakira', 'dualipa', 'brunomars', 'adele',
    'cardib', 'nickiminaj', 'mileycyrus', 'katyperry', 'shawnmendes',
    'eminem', 'coldplay', 'postmalone', 'lizzobeeating', 'demilovato',
    'harrystyles', 'niallhoran', 'liampayne', 'louist91', 'zayn',
    'badbunnypr', 'jbalvin', 'maluma', 'daddy_yankee', 'karolg', 'anitta',
    'rosalia.vt', 'sabrinacarpenter', 'oliviarodrigo', 'sza', 'dojacat',
    'travisscott', 'kendricklamar', 'megan_thee_stallion', 'jackharlow',
    'camilacabello', 'khalid', 'halsey', 'imagine_dragons', 'maroon5',
    'samsmith', 'eltonofficial', 'madonna', 'cher', 'celinedion',
    'jenniferlopez', 'mariah_carey', 'britneyspears', 'pink', 'aliciakeys',
    'lilnasx', 'charlieputh', 'jonasbrothers', 'nickjonas', 'joejonas',
    'future', 'lilbaby', 'gunna', 'playboicarti', 'liluzivert', '21savage',
    'asaprocky', 'tylerthecreator', 'frankocean', 'weeknd', 'lanadelrey',
    'blackpinkofficial', 'roses_are_rosie', 'jennierubyjane', 'lalalalisa_m', 'sooyaaa__',
    'bts.bighitofficial', 'jin', 'agustd', 'jm', 'thv', 'jungkook.97', 'rkive', 'uarmyhope',
    'twicetagram', 'got7.with.igot7', 'straykids_official', 'skzoo_official',
    'aespa_official', 'redvelvet.smtown', 'nct', 'nct127', 'txt_bighit',
    'enhypen', 'itzy.all.in.us', 'newjeans_official', 'ivestarship',
    'therock', 'vindiesel', 'kevinhart4real', 'willsmith', 'chrishemsworth',
    'robertdowneyjr', 'tomholland2013', 'zendaya', 'timotheechalamet',
    'ryanreynolds', 'blakelively', 'gal_gadot', 'wonderwoman',
    'scarlettjohanssonworld', 'jasonmomoa', 'hughjackman', 'prattprattpratt',
    'leonardodicaprio', 'tomcruise', 'markruffalo', 'chrisevans', 'paulrudd',
    'milliebobbybrown', 'finnwolfhardofficial', 'sadiesink_', 'noahschnapp',
    'gatenm123', 'calebmclaughlin', 'jennaortega', 'florencepugh',
    'anyataylorjoy', 'henrycavill', 'austinbutler', 'margotrobbie',
    'jenniferaniston', 'courteneycoxofficial', 'lisakudrow', 'mleblanc',
    'mattyperry4', 'davidschwimmer', 'reeseaterspoon', 'nicolekidman',
    'priyankachopra', 'deepikapadukone', 'akshaykumar', 'amitabhbachchan',
    'shahrukhkhan', 'ranveersingh', 'katrinakaif', 'aliaabhatt', 'shraddhakapoor',
    'kendalljenner', 'gigihadid', 'bellahadid', 'caradelevingne',
    'emrata', 'irinashayk', 'romeestrijd', 'winnieharlow', 'elsahosk',
    'haileybieber', 'ashleygraham', 'naomicampbell', 'tyrabanks', 'cindycrawford',
    'heidiklum', 'adrianalima', 'gisele', 'mirandakerr', 'rosiehw',
    'karliekloss', 'candicesswanepoel', 'taylor_hill', 'josephineskriver',
    'sarasampaio', 'laisribeiro', 'jastookes', 'marthahunt',
    'victoriassecret', 'voguemagazine', 'harpersbazaarus', 'elleusa',
    'gucci', 'louisvuitton', 'chanelofficial', 'dior', 'prada',
    'versace', 'balenciaga', 'ysl', 'fendi', 'givenchy',
    'burberry', 'hermes', 'valentino', 'armani', 'dolcegabbana',
    'calvinklein', 'tomford', 'ralphlauren', 'michaelkors', 'off____white',
    'kimkardashian', 'khloekardashian', 'kourtneykardash', 'krisjenner',
    'kyliejenner', 'scottdisick', 'robkardashianofficial',
    'kyliecosmetics', 'kkwbeauty', 'skims', 'goodamerican', 'poosh',
    'cristiano', 'leomessi', 'neymarjr', 'k.mbappe', 'paulpogba',
    'davidbeckham', 'sergioramos', 'toni.kr8s', 'hazardeden_10',
    'garethbale11', 'mosalah', 'luissuarez9', 'lewandowski',
    'erling.haaland', 'vinijr', 'pedri', 'judebellingham', 'ziyech',
    'zlatanibrahimovic',
    'kingjames', 'stephencurry30', 'kevindurant', 'giannis_an34',
    'russwest44', 'jameshardenstore', 'kawhileonard', 'kyrieirving',
    'lameloball', 'klaythompson', 'damianlillard', 'lukadoncic',
    'tom_brady', 'odell', 'patrickmahomes', 'traviskelce',
    'serenawilliams', 'rogerfederer', 'rafaelnadal', 'djokernole',
    'usainbolt', 'simonebiles', 'tigerwoods', 'michaelphelps',
    'lewishamilton', 'maxverstappen1', 'charles_leclerc', 'landonorris',
    'danielricciardo', 'carlossainz55', 'georgerussell63', 'schecoperez',
    'conormcgregor', 'khabib_nurmagomedov', 'floydmayweather', 'canelo',
    'miketyson', 'jakepaul', 'loganpaul', 'francisngannou', 'adesanya',
    'fcbarcelona', 'realmadrid', 'psg', 'manchesterunited', 'manchestercity',
    'liverpoolfc', 'chelseafc', 'arsenal', 'juventus', 'acmilan', 'fcbayern',
    'inter', 'atleticodemadrid', 'borussiadortmund', 'galatasaray',
    'championsleague', 'fifaworldcup', 'premierleague', 'laliga', 'nba', 'nfl', 'ufc', 'f1',
    '433', 'goal', 'espnfc', 'brfootball', 'houseofhighlights', 'sportscenter',
    '9gag', 'fuckjerry', 'daquan', 'memezar', 'pubity', 'sarcasm_only',
    'ladbible', 'barstoolsports', 'worldstar', 'hoodclips', 'epicfunnypage',
    'tank.sinatra', 'thefatjewish', 'beige.cardigan', 'dudewithsign',
    'shitheadsteve', 'middleclassfancy', 'betches', 'mytherapistsays',
    'so.shauna', 'crazybitchprobs', 'bitch', 'trevornoah', 'kalesalad',
    'subwaycreatures', 'kidsgettinghurt', 'influencersinthewild',
    'jiffpom', 'nala_cat', 'itsdougthepug', 'marutaro', 'realgrumpycat',
    'tuckerbudzyn', 'juniperfoxx', 'venustwofacecat', 'tunameltsmyheart',
    'pumpkintheraccoon', 'loki', 'hamlet_the_piggy', 'iamlilbub',
    'smoothiethecat', 'marniethedog', 'norbertthedog', 'tecuaniventura',
    'dean.schneider', 'blackjaguarwhitetiger', 'natgeowild', 'animalplanet',
    'mrbeast', 'pewdiepie', 'ksi', 'ishowspeed', 'kaicenat', 'adinross',
    'pokimanelol', 'xqc', 'ninja', 'dream', 'tommyinnit', 'markiplier',
    'jacksepticeye', 'miniminter', 'wroetoshaw', 'zerkaa', 'behzinga', 'vikkstagram',
    'khaby00', 'charlidamelio', 'addisonraee', 'jamescharles', 'emmachamberlain',
    'daviddobrik', 'zachking', 'camerondallas', 'nashgrier', 'lelepons',
    'hannahstocking', 'brentrivera', 'larray', 'avani', 'dixiedamelio',
    'noahbeck', 'brycehall', 'joshuariau', 'nessabarrett', 'bellapoarch',
    'inanna',
    'apple', 'google', 'microsoft', 'samsung', 'sony', 'playstation', 'xbox', 'nintendo',
    'tesla', 'spacex', 'nasa', 'natgeo', 'nationalgeographic', 'discovery',
    'netflix', 'hulu', 'disneyplus', 'hbomax', 'primevideo', 'disney',
    'marvel', 'starwars', 'pixar', 'warnerbros', 'universalpictures',
    'spotify', 'applemusic', 'tiktok', 'instagram', 'youtube', 'twitter', 'facebook',
    'nike', 'adidas', 'puma', 'reebok', 'underarmour', 'newbalance', 'jordan',
    'vans', 'converse', 'supremenewyork', 'stussy', 'kith',
    'cocacola', 'pepsi', 'redbull', 'monsterenergy', 'starbucks',
    'mcdonalds', 'burgerking', 'kfc', 'subway', 'tacobell', 'chipotle',
    'wendys', 'dunkin', 'pizzahut', 'dominos', 'nutella', 'oreo',
    'sephora', 'maccosmetics', 'maybelline', 'lorealparis', 'nyxcosmetics',
    'fentybeauty', 'hudabeauty', 'anastasiabeverlyhills', 'morphebrushes',
    'urbandecaycosmetics', 'narsissist', 'tartecosmetics', 'benefitcosmetics',
    'colourpopcosmetics', 'jeffreestarcosmetics', 'nikkietutorials', 'mannymua733',
    'billgates', 'elonmusk', 'jeffbezos', 'markzuckerberg', 'richardbranson',
    'oprah', 'barackobama', 'michelleobama', 'dalailama', 'malala',
    'gordonramsay', 'jamieoliver', 'nusr_et', 'saltbae', 'foodgod',
    'garyvee', 'grantcardone', 'tonyrobbins', 'daveramsey',
    'beautifuldestinations', 'earth', 'earthpix', 'passionpassport',
    'travelandleisure', 'condenasttraveler', 'lonelyplanet',
    'muradosmann', 'chrisburkard', 'brandonwoelfel', 'humansofny',
    'fortnite', 'callofduty', 'minecraft', 'leagueoflegends', 'valorant',
    'apexlegends', 'pubg', 'roblox', 'gta5', 'rockstargames',
    'easportsfifa', 'nba2k', 'fazeclan', 'tsm', '100thieves', 'cloud9'
}

# --- HELPERS ---

def fmt_ts(ts):
    """Unix timestamp -> 'YYYY-MM-DD' (or 'unknown')."""
    try:
        return datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d") if ts else "unknown"
    except (ValueError, OSError, OverflowError):
        return "unknown"


def profile_url(user):
    return f"https://www.instagram.com/{user}/?hl=en"


def read_names(path, lower=False):
    """Read usernames from a txt file. Accepts plain names, '@name',
    or exported lines like 'name | 2024-01-01 | https://...'."""
    names = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name = line.split("|")[0].split()[0].lstrip("@") if line.split("|")[0].split() else ""
            if name:
                names.add(name.lower() if lower else name)
    return names


def init_fonts(root):
    available = set(tkfont.families(root))

    def pick(candidates, fallback):
        for c in candidates:
            if c in available:
                return c
        return fallback

    ui = pick(["Segoe UI Variable Text", "Segoe UI", "SF Pro Text", "Helvetica Neue",
               "Inter", "Ubuntu", "Cantarell", "DejaVu Sans"], "Helvetica")
    FONTS.update({
        "title": (ui, 16, "bold"),
        "h1": (ui, 20, "bold"),
        "h2": (ui, 12, "bold"),
        "body": (ui, 10),
        "body_bold": (ui, 10, "bold"),
        "small": (ui, 9),
        "small_bold": (ui, 9, "bold"),
        "caps": (ui, 8, "bold"),
        "stat": (ui, 24, "bold"),
        "icon": (ui, 13),
    })


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def blend(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(a[i] + (b[i] - a[i]) * t)))) for i in range(3))


def rounded_rect_points(x1, y1, x2, y2, r):
    r = max(0, min(r, (x2 - x1) / 2, (y2 - y1) / 2))
    return [x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r,
            x2, y2 - r, x2, y2 - r, x2, y2, x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2,
            x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1, y1]


def draw_gradient_rect(canvas, w, h, radius, c1, c2, mix=None, mix_amt=0.0):
    """Horizontal gradient with rounded corners, drawn column by column."""
    w, h = max(2, int(w)), max(2, int(h))
    r = min(radius, w / 2, h / 2)
    for x in range(w):
        color = blend(c1, c2, x / (w - 1))
        if mix:
            color = blend(color, mix, mix_amt)
        inset = 0.0
        if r > 0 and x < r:
            dx = r - x - 0.5
            inset = r - math.sqrt(max(0.0, r * r - dx * dx))
        elif r > 0 and x >= w - r:
            dx = x + 0.5 - (w - r)
            inset = r - math.sqrt(max(0.0, r * r - dx * dx))
        y1 = int(round(inset))
        canvas.create_line(x, y1, x, h - y1, fill=color)


def inside(widget, ancestor):
    while widget is not None:
        if widget is ancestor:
            return True
        widget = getattr(widget, "master", None)
    return False


def pointer_inside(widget):
    try:
        x, y = widget.winfo_pointerxy()
        return inside(widget.winfo_containing(x, y), widget)
    except (KeyError, tk.TclError):
        return False


def shorten_middle(text, limit=28):
    if len(text) <= limit:
        return text
    keep = limit - 1
    head = keep - keep // 2
    tail = keep // 2
    return text[:head] + "…" + (text[-tail:] if tail else "")


# --- CUSTOM UI WIDGETS ---

class RoundButton(tk.Canvas):
    """Rounded button. variants: primary (gradient), secondary, ghost."""

    def __init__(self, parent, text, command=None, variant="secondary", font=None,
                 padx=16, pady=8, radius=8, fill_width=False):
        self._font = tkfont.Font(font=font or FONTS["body_bold"])
        self.text = text
        self.command = command
        self.variant = variant
        self.padx, self.pady, self.radius = padx, pady, radius
        self.fill_width = fill_width
        self.enabled = True
        self._hover = False
        self._pressed = False
        self._parent_bg = parent.cget("bg")
        self._cw = self._font.measure(text) + 2 * padx
        self._ch = self._font.metrics("linespace") + 2 * pady
        super().__init__(parent, width=self._cw, height=self._ch, highlightthickness=0, bd=0,
                         bg=self._parent_bg, cursor="hand2")
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        if fill_width:
            self.bind("<Configure>", self._on_configure)
        self._draw()

    # -- public --
    def set_text(self, text):
        self.text = text
        if not self.fill_width:
            self._cw = self._font.measure(text) + 2 * self.padx
            self.configure(width=self._cw)
        self._draw()

    def set_enabled(self, enabled):
        self.enabled = bool(enabled)
        self.configure(cursor="hand2" if self.enabled else "arrow")
        self._hover = self._pressed = False
        self._draw()

    # -- events --
    def _on_configure(self, event):
        if event.width > 1:
            self._cw = event.width
            self._draw()

    def _on_enter(self, _e):
        self._hover = True
        self._draw()

    def _on_leave(self, _e):
        self._hover = False
        self._pressed = False
        self._draw()

    def _on_press(self, _e):
        if self.enabled:
            self._pressed = True
            self._draw()

    def _on_release(self, e):
        if not self.enabled:
            return
        was_pressed = self._pressed
        self._pressed = False
        self._draw()
        if was_pressed and 0 <= e.x <= self._cw and 0 <= e.y <= self._ch and self.command:
            self.command()

    # -- drawing --
    def _draw(self):
        self.delete("all")
        w, h = self._cw, self._ch
        fg = COLORS["text_main"]
        if not self.enabled:
            fill, outline, fg = COLORS["card"], COLORS["border"], COLORS["text_dim"]
            self._flat(w, h, fill, outline)
        elif self.variant == "primary":
            fg = "white"
            if self._pressed:
                draw_gradient_rect(self, w, h, self.radius, COLORS["accent_blue"], COLORS["accent_grad"], "#000000", 0.18)
            elif self._hover:
                draw_gradient_rect(self, w, h, self.radius, COLORS["accent_blue"], COLORS["accent_grad"], "#ffffff", 0.14)
            else:
                draw_gradient_rect(self, w, h, self.radius, COLORS["accent_blue"], COLORS["accent_grad"])
        elif self.variant == "ghost":
            fill, outline, fg = self._parent_bg, "", COLORS["text_sub"]
            if self._hover:
                fill, fg = COLORS["card_hover"], COLORS["text_main"]
            self._flat(w, h, fill, outline)
        else:
            fill, outline = COLORS["btn"], COLORS["border"]
            if self._hover:
                fill, outline = COLORS["btn_hover"], COLORS["border_hover"]
            if self._pressed:
                fill = blend(fill, "#000000", 0.2)
            self._flat(w, h, fill, outline)
        self.create_text(w / 2, h / 2, text=self.text, fill=fg, font=self._font)

    def _flat(self, w, h, fill, outline):
        self.create_polygon(rounded_rect_points(0.5, 0.5, w - 0.5, h - 0.5, self.radius),
                            smooth=True, fill=fill, outline=outline, width=1)


class ModernToggle(tk.Canvas):
    """Animated on/off switch bound to a BooleanVar."""

    def __init__(self, parent, variable, command=None, width=42, height=22):
        super().__init__(parent, width=width, height=height, highlightthickness=0, bd=0,
                         bg=parent.cget("bg"), cursor="hand2")
        self.variable = variable
        self.command = command
        self._cw, self._ch = width, height
        self._pos = 1.0 if variable.get() else 0.0
        self._after = None
        self.bind("<Button-1>", lambda _e: self.invoke())
        variable.trace_add("write", self._on_var)
        self._draw()

    def invoke(self):
        self.variable.set(not self.variable.get())
        if self.command:
            self.command()

    def _on_var(self, *_):
        if not self.winfo_exists():
            return
        if self._after:
            self.after_cancel(self._after)
        self._step()

    def _step(self):
        target = 1.0 if self.variable.get() else 0.0
        if abs(target - self._pos) < 0.05:
            self._pos = target
            self._after = None
        else:
            self._pos += (target - self._pos) * 0.45
            self._after = self.after(14, self._step)
        self._draw()

    def _draw(self):
        self.delete("all")
        w, h = self._cw, self._ch
        track = blend(COLORS["toggle_off"], COLORS["accent_blue"], self._pos)
        self.create_polygon(rounded_rect_points(0.5, 0.5, w - 0.5, h - 0.5, h / 2),
                            smooth=True, fill=track, outline="")
        pad = 3
        knob = h - 2 * pad
        x = pad + self._pos * (w - h)
        self.create_oval(x, pad, x + knob, pad + knob, fill="white", outline="")


class ScrollFrame(tk.Frame):
    """Vertically scrollable container; the scrollbar only appears when needed."""

    def __init__(self, parent, bg, scroll_style=None):
        super().__init__(parent, bg=bg)
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0, yscrollincrement=16)
        kw = {"style": scroll_style} if scroll_style else {}
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview, **kw)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.inner = tk.Frame(self.canvas, bg=bg)
        self._win = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.inner.bind("<Configure>", self._on_inner)
        self.canvas.bind("<Configure>", self._on_canvas)
        for seq in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.bind_all(seq, self._on_wheel, add="+")

    def _on_inner(self, _e=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self._update_scrollbar()

    def _on_canvas(self, e):
        self.canvas.itemconfigure(self._win, width=e.width)
        self._update_scrollbar()

    def _update_scrollbar(self):
        need = self.inner.winfo_reqheight() > self.canvas.winfo_height()
        shown = bool(self.scrollbar.winfo_manager())
        if need and not shown:
            self.scrollbar.pack(side="right", fill="y", before=self.canvas)
        elif not need and shown:
            self.scrollbar.pack_forget()

    def _on_wheel(self, event):
        try:
            w = self.winfo_containing(event.x_root, event.y_root)
        except (KeyError, tk.TclError):
            return
        if w is None or not inside(w, self):
            return
        if self.inner.winfo_reqheight() <= self.canvas.winfo_height():
            return
        if getattr(event, "num", None) == 4:
            step = -1
        elif getattr(event, "num", None) == 5:
            step = 1
        else:
            step = -1 if event.delta > 0 else 1
        self.canvas.yview_scroll(step * 2, "units")


def bind_tree(widget, sequence, func, skip=()):
    if isinstance(widget, skip):
        return
    widget.bind(sequence, func, add="+")
    for child in widget.winfo_children():
        bind_tree(child, sequence, func, skip)


class ModeSelector(tk.Frame):
    """Two selectable cards bound to a BooleanVar (False = left, True = right)."""

    def __init__(self, parent, variable, options, command=None):
        super().__init__(parent, bg=parent.cget("bg"))
        self.variable = variable
        self.command = command
        self.cards = []
        for i, (value, title, sub) in enumerate(options):
            self.columnconfigure(i, weight=1, uniform="mode")
            card = tk.Frame(self, bg=COLORS["card"], highlightthickness=1,
                            highlightbackground=COLORS["border"], cursor="hand2")
            card.grid(row=0, column=i, sticky="nsew", padx=(0, 5) if i == 0 else (5, 0))
            t = tk.Label(card, text=title, font=FONTS["body_bold"], bg=COLORS["card"],
                         fg=COLORS["text_main"], anchor="w", cursor="hand2")
            t.pack(fill="x", padx=12, pady=(10, 0))
            s = tk.Label(card, text=sub, font=FONTS["small"], bg=COLORS["card"], fg=COLORS["text_sub"],
                         anchor="w", justify="left", wraplength=140, cursor="hand2")
            s.pack(fill="x", padx=12, pady=(2, 10))
            bind_tree(card, "<Button-1>", lambda _e, v=value: self._choose(v))
            self.cards.append((value, card, t, s))
        variable.trace_add("write", lambda *_: self._refresh())
        self._refresh()

    def _choose(self, value):
        self.variable.set(value)
        if self.command:
            self.command()

    def _refresh(self):
        current = self.variable.get()
        for value, card, t, s in self.cards:
            on = (bool(value) == bool(current))
            bg = blend(COLORS["card"], COLORS["accent_blue"], 0.14) if on else COLORS["card"]
            card.config(bg=bg, highlightbackground=COLORS["accent_blue"] if on else COLORS["border"])
            t.config(bg=bg)
            s.config(bg=bg, fg=COLORS["text_main"] if on else COLORS["text_sub"])


class FileRow(tk.Frame):
    """A file picker row: status icon, title, filename/hint and a Browse button."""

    def __init__(self, parent, title, hint, on_browse, bg=None):
        self._bg = bg or COLORS["card"]
        super().__init__(parent, bg=self._bg, highlightthickness=1,
                         highlightbackground=COLORS["border"], cursor="hand2")
        self._hint = hint
        self._loaded = False
        self.icon = tk.Label(self, text="○", font=FONTS["icon"], bg=self._bg, fg=COLORS["text_dim"],
                             width=2, cursor="hand2")
        self.icon.grid(row=0, column=0, rowspan=2, padx=(10, 2), pady=10)
        self.title_lbl = tk.Label(self, text=title, font=FONTS["body_bold"], bg=self._bg,
                                  fg=COLORS["text_main"], anchor="w", cursor="hand2")
        self.title_lbl.grid(row=0, column=1, sticky="sw", pady=(8, 0))
        self.sub_lbl = tk.Label(self, text=hint, font=FONTS["small"], bg=self._bg, fg=COLORS["text_dim"],
                                anchor="w", justify="left", wraplength=190, cursor="hand2")
        self.sub_lbl.grid(row=1, column=1, sticky="nw", pady=(0, 8))
        self.btn = RoundButton(self, "Browse", on_browse, variant="secondary",
                               font=FONTS["small_bold"], padx=12, pady=5, radius=7)
        self.btn.grid(row=0, column=2, rowspan=2, padx=(6, 10))
        self.columnconfigure(1, weight=1)
        bind_tree(self, "<Button-1>", lambda _e: on_browse(), skip=(RoundButton,))
        bind_tree(self, "<Enter>", lambda _e: self._set_border(True), skip=(RoundButton,))
        bind_tree(self, "<Leave>", self._on_leave, skip=(RoundButton,))

    def _rest_border(self):
        return blend(COLORS["success"], self._bg, 0.65) if self._loaded else COLORS["border"]

    def _set_border(self, hovering):
        self.config(highlightbackground=COLORS["border_hover"] if hovering else self._rest_border())

    def _on_leave(self, _e):
        if not pointer_inside(self):
            self._set_border(False)

    def set_file(self, name):
        self._loaded = True
        self.icon.config(text="✓", fg=COLORS["success"])
        self.sub_lbl.config(text=shorten_middle(name), fg=COLORS["success"])
        self.btn.set_text("Change")
        self._set_border(False)

    def flash_error(self):
        self.config(highlightbackground=COLORS["danger"])
        self.after(2200, lambda: self._set_border(False))


class ToggleRow(tk.Frame):
    def __init__(self, parent, title, desc, variable, command=None):
        bg = parent.cget("bg")
        super().__init__(parent, bg=bg)
        self.toggle = ModernToggle(self, variable, command)
        self.toggle.pack(side="right", padx=(14, 0))
        text = tk.Frame(self, bg=bg)
        text.pack(side="left", fill="x", expand=True)
        t = tk.Label(text, text=title, font=FONTS["body_bold"], bg=bg, fg=COLORS["text_main"],
                     anchor="w", cursor="hand2")
        t.pack(fill="x")
        d = tk.Label(text, text=desc, font=FONTS["small"], bg=bg, fg=COLORS["text_sub"], anchor="w",
                     justify="left", wraplength=235, cursor="hand2")
        d.pack(fill="x", pady=(2, 0))
        for w in (t, d, text):
            w.bind("<Button-1>", lambda _e: self.toggle.invoke())


class StatCard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["card"], highlightthickness=1, highlightbackground=COLORS["border"])
        self.bar = tk.Frame(self, height=3, bg=COLORS["accent_blue"])
        self.bar.pack(fill="x")
        inner = tk.Frame(self, bg=COLORS["card"])
        inner.pack(fill="both", expand=True, padx=16, pady=(10, 12))
        self.title = tk.Label(inner, text="", font=FONTS["small_bold"], bg=COLORS["card"],
                              fg=COLORS["text_sub"], anchor="w")
        self.title.pack(fill="x")
        self.value = tk.Label(inner, text="0", font=FONTS["stat"], bg=COLORS["card"],
                              fg=COLORS["text_main"], anchor="w")
        self.value.pack(fill="x")
        self.sub = tk.Label(inner, text="\u00a0", font=FONTS["small"], bg=COLORS["card"],
                            fg=COLORS["text_dim"], anchor="w")
        self.sub.pack(fill="x")

    def set(self, title, value, color=None, sub=""):
        color = color or COLORS["text_main"]
        self.title.config(text=title)
        self.value.config(text=str(value), fg=color)
        self.sub.config(text=sub or "\u00a0")
        self.bar.config(bg=color)


class SearchEntry(tk.Frame):
    def __init__(self, parent, placeholder, command):
        super().__init__(parent, bg=COLORS["input_bg"], highlightthickness=1,
                         highlightbackground=COLORS["border"])
        self.placeholder = placeholder
        self.command = command
        self._ph = False
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var, font=FONTS["body"], bg=COLORS["input_bg"],
                              fg=COLORS["text_main"], insertbackground=COLORS["text_main"],
                              relief="flat", bd=0, highlightthickness=0)
        self.entry.pack(side="left", fill="x", expand=True, padx=(12, 4), pady=8)
        self.clear_btn = tk.Label(self, text="✕", font=FONTS["small"], bg=COLORS["input_bg"],
                                  fg=COLORS["text_dim"], cursor="hand2", padx=8)
        self.clear_btn.bind("<Button-1>", lambda _e: self.clear(focus=True))
        self.var.trace_add("write", self._on_change)
        self.entry.bind("<FocusIn>", self._focus_in)
        self.entry.bind("<FocusOut>", self._focus_out)
        self._show_placeholder()

    def get(self):
        return "" if self._ph else self.var.get()

    def focus(self):
        self.entry.focus_set()

    def clear(self, focus=False):
        self._ph = False
        self.var.set("")
        self.entry.config(fg=COLORS["text_main"])
        if focus:
            self.entry.focus_set()
        else:
            try:
                focused = self.focus_get() is self.entry
            except (KeyError, tk.TclError):
                focused = False
            if not focused:
                self._show_placeholder()

    def _show_placeholder(self):
        self._ph = True
        self.var.set(self.placeholder)
        self.entry.config(fg=COLORS["text_dim"])

    def _focus_in(self, _e):
        self.config(highlightbackground=COLORS["accent_blue"])
        if self._ph:
            self._ph = False
            self.var.set("")
            self.entry.config(fg=COLORS["text_main"])

    def _focus_out(self, _e):
        self.config(highlightbackground=COLORS["border"])
        if not self.var.get():
            self._show_placeholder()

    def _on_change(self, *_):
        if self._ph:
            return
        text = self.var.get()
        if text and not self.clear_btn.winfo_manager():
            self.clear_btn.pack(side="right")
        elif not text and self.clear_btn.winfo_manager():
            self.clear_btn.pack_forget()
        self.command(text)


class TabBar(tk.Frame):
    def __init__(self, parent, on_select):
        self._bg = parent.cget("bg")
        super().__init__(parent, bg=self._bg)
        self._on_select = on_select
        self._tabs = {}
        self.active = None

    def set_tabs(self, tabs):
        for t in self._tabs.values():
            t["frame"].destroy()
        self._tabs = {}
        self.active = None
        for key, title, count, color in tabs:
            frame = tk.Frame(self, bg=self._bg, cursor="hand2")
            frame.pack(side="left", padx=(0, 24))
            row = tk.Frame(frame, bg=self._bg, cursor="hand2")
            row.pack(fill="x")
            lbl = tk.Label(row, text=title, font=FONTS["body_bold"], bg=self._bg, fg=COLORS["text_sub"],
                           cursor="hand2")
            lbl.pack(side="left")
            badge = tk.Label(row, text=str(count), font=FONTS["small_bold"], bg=COLORS["card_hover"],
                             fg=COLORS["text_sub"], padx=7, pady=1, cursor="hand2")
            badge.pack(side="left", padx=(8, 0))
            line = tk.Frame(frame, height=2, bg=self._bg)
            line.pack(fill="x", pady=(8, 0))
            for w in (frame, row, lbl, badge, line):
                w.bind("<Button-1>", lambda _e, k=key: self._on_select(k))
            self._tabs[key] = {"frame": frame, "label": lbl, "badge": badge, "line": line, "color": color}

    def select(self, key):
        self.active = key
        for k, t in self._tabs.items():
            on = (k == key)
            t["label"].config(fg=COLORS["text_main"] if on else COLORS["text_sub"])
            t["badge"].config(fg=t["color"] if on else COLORS["text_sub"],
                              bg=blend(t["color"], self._bg, 0.82) if on else COLORS["card_hover"])
            t["line"].config(bg=t["color"] if on else self._bg)

    def set_count(self, key, n):
        if key in self._tabs:
            self._tabs[key]["badge"].config(text=str(n))


# --- MAIN APP ---

class InstagramCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Follower Analyzer 3.0 by Noriuko")
        self.root.configure(bg=COLORS["bg"])
        self.root.minsize(980, 660)
        init_fonts(root)
        self._scroll_style = "Vertical.TScrollbar"
        self._init_styles()

        # --- DATA & VARS ---
        self.famous_accounts = FAMOUS_ACCOUNTS
        self.following_path = ""
        self.followers_path = ""
        self.old_followers_path = ""
        self.previous_path = ""
        self.ignore_list_path = ""
        self._last_dir = ""

        self.ignore_famous_var = tk.BooleanVar(value=True)
        self.show_fans_var = tk.BooleanVar(value=True)
        self.use_ignore_list_var = tk.BooleanVar(value=False)
        self.track_unfollowers_var = tk.BooleanVar(value=False)
        self.compare_mode_var = tk.BooleanVar(value=False)

        # results state
        self.tabs = []
        self.active_key = None
        self._filter = ""
        self._sort_state = (None, False)
        self.visited = set()
        self._export_payload = None
        self._status_link_target = None

        self._build_ui()
        self._center(1200, 780)

        self.root.bind("<Control-Return>", lambda _e: self.process_files())
        self.root.bind("<F5>", lambda _e: self.process_files())
        self.root.bind("<Control-f>", lambda _e: self.search.focus())

    # --- STYLES ---

    def _init_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        rowh = max(30, tkfont.Font(font=FONTS["body"]).metrics("linespace") + 14)
        card = COLORS["card"]
        style.configure("Modern.Treeview", background=card, fieldbackground=card,
                        foreground=COLORS["text_main"], rowheight=rowh, borderwidth=0, relief="flat",
                        font=FONTS["body"], bordercolor=card, lightcolor=card, darkcolor=card)
        style.map("Modern.Treeview", background=[("selected", COLORS["selected"])],
                  foreground=[("selected", "#ffffff")])
        style.configure("Modern.Treeview.Heading", background=COLORS["sidebar"],
                        foreground=COLORS["text_sub"], relief="flat", borderwidth=0,
                        font=FONTS["small_bold"], padding=(10, 8))
        style.map("Modern.Treeview.Heading", background=[("active", COLORS["card_hover"])],
                  foreground=[("active", COLORS["text_main"])])
        try:
            name = "Modern.Vertical.TScrollbar"
            style.layout(name, [("Vertical.Scrollbar.trough", {
                "sticky": "ns",
                "children": [("Vertical.Scrollbar.thumb", {"expand": "1", "sticky": "nswe"})]})])
            style.configure(name, troughcolor=COLORS["sidebar"], background=COLORS["border_hover"],
                            bordercolor=COLORS["sidebar"], lightcolor=COLORS["border_hover"],
                            darkcolor=COLORS["border_hover"], gripcount=0, relief="flat", width=10)
            style.map(name, background=[("active", COLORS["text_dim"])])
            self._scroll_style = name
        except tk.TclError:
            style.configure("Vertical.TScrollbar", gripcount=0, background=COLORS["card"],
                            darkcolor=COLORS["bg"], lightcolor=COLORS["bg"], troughcolor=COLORS["bg"],
                            bordercolor=COLORS["bg"], arrowcolor="white")

    def _center(self, w, h):
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = min(w, sw - 80), min(h, sh - 120)
        x, y = (sw - w) // 2, max(0, (sh - h) // 3)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # --- UI CONSTRUCTION ---

    def _build_ui(self):
        self.sidebar = tk.Frame(self.root, bg=COLORS["sidebar"], width=400)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        tk.Frame(self.root, width=1, bg=COLORS["border"]).pack(side="left", fill="y")
        self.content = tk.Frame(self.root, bg=COLORS["bg"])
        self.content.pack(side="left", fill="both", expand=True)
        self._build_sidebar()
        self._build_content()

    def _section_label(self, parent, text):
        tk.Label(parent, text=text.upper(), font=FONTS["caps"], bg=parent.cget("bg"),
                 fg=COLORS["text_dim"]).pack(anchor="w", pady=(18, 8))

    def _build_sidebar(self):
        sb = self.sidebar
        bg = COLORS["sidebar"]

        strip = tk.Canvas(sb, height=3, bg=bg, highlightthickness=0, bd=0)
        strip.pack(fill="x")

        def draw_strip(e):
            strip.delete("all")
            if e.width > 2:
                draw_gradient_rect(strip, e.width, 3, 0, COLORS["accent_blue"], COLORS["accent_grad"])
        strip.bind("<Configure>", draw_strip)

        header = tk.Frame(sb, bg=bg)
        header.pack(fill="x", padx=20, pady=(18, 4))
        logo = tk.Canvas(header, width=40, height=40, bg=bg, highlightthickness=0, bd=0)
        logo.pack(side="left")
        draw_gradient_rect(logo, 40, 40, 12, COLORS["accent_blue"], COLORS["accent_grad"])
        logo.create_text(20, 20, text="F", fill="white", font=FONTS["title"])
        titles = tk.Frame(header, bg=bg)
        titles.pack(side="left", padx=12)
        tk.Label(titles, text="Follower Analyzer", font=FONTS["title"], bg=bg,
                 fg=COLORS["text_main"]).pack(anchor="w")
        tk.Label(titles, text="v3.0  •  by noriuko", font=FONTS["small"], bg=bg,
                 fg=COLORS["text_dim"]).pack(anchor="w")

        # pinned bottom: run button
        bottom = tk.Frame(sb, bg=bg)
        bottom.pack(side="bottom", fill="x")
        tk.Frame(bottom, height=1, bg=COLORS["border"]).pack(fill="x")
        binner = tk.Frame(bottom, bg=bg)
        binner.pack(fill="x", padx=20, pady=16)
        self.run_btn = RoundButton(binner, "Run analysis", self.process_files, variant="primary",
                                   fill_width=True, pady=13, radius=10)
        self.run_btn.pack(fill="x")
        tk.Label(binner, text="Shortcut: Ctrl + Enter", font=FONTS["small"], bg=bg,
                 fg=COLORS["text_dim"]).pack(pady=(8, 0))

        # scrollable middle
        self.scroll = ScrollFrame(sb, bg, self._scroll_style)
        self.scroll.pack(fill="both", expand=True)
        body = tk.Frame(self.scroll.inner, bg=bg)
        body.pack(fill="x", padx=20, pady=(0, 12))

        self._section_label(body, "Analysis mode")
        ModeSelector(body, self.compare_mode_var, [
            (False, "Standard check", "Who doesn't follow me back?"),
            (True, "Compare snapshots", "What changed since an older export?"),
        ], command=self.toggle_compare_mode_ui).pack(fill="x")

        self._section_label(body, "Data files")
        self.files_box = tk.Frame(body, bg=bg)
        self.files_box.pack(fill="x")
        self.row_following = FileRow(self.files_box, "Following", "following.json from your export",
                                     self.load_following)
        self.row_following.pack(fill="x", pady=4)
        self.row_followers = FileRow(self.files_box, "Followers", "followers_1.json from your export",
                                     self.load_followers)
        self.row_followers.pack(fill="x", pady=4)
        self.row_old = FileRow(self.files_box, "Older followers", "An earlier followers export",
                               self.load_old_followers)  # shown in compare mode only

        # options (standard mode only)
        self.options_box = tk.Frame(body, bg=bg)
        self.options_box.pack(fill="x")
        self._section_label(self.options_box, "Options")
        card = tk.Frame(self.options_box, bg=COLORS["card"], highlightthickness=1,
                        highlightbackground=COLORS["border"])
        card.pack(fill="x")
        inner = tk.Frame(card, bg=COLORS["card"])
        inner.pack(fill="x", padx=14, pady=2)

        self._add_option(inner, "Hide famous accounts",
                         "Skip celebrities, brands and big pages in the results.",
                         self.ignore_famous_var, divider=False)
        self._add_option(inner, "Show fans",
                         "List people who follow you that you don't follow back.",
                         self.show_fans_var)
        slot_ignore = self._add_option(inner, "Use ignore list",
                                       "Hide usernames listed in your own ignore_list.txt.",
                                       self.use_ignore_list_var, self.toggle_ignore_list_ui)
        slot_prev = self._add_option(inner, "Spot new unfollowers",
                                     "Compare against your previous non_follow.txt export.",
                                     self.track_unfollowers_var, self.toggle_previous_file_ui)
        self.row_ignore = FileRow(slot_ignore, "Ignore list", "ignore_list.txt (one name per line)",
                                  self.load_ignore_list, bg=COLORS["input_bg"])
        self.row_prev = FileRow(slot_prev, "Previous export", "non_follow.txt from last time",
                                self.load_previous, bg=COLORS["input_bg"])

    def _add_option(self, parent, title, desc, var, command=None, divider=True):
        bg = parent.cget("bg")
        if divider:
            tk.Frame(parent, height=1, bg=COLORS["border"]).pack(fill="x")
        wrap = tk.Frame(parent, bg=bg)
        wrap.pack(fill="x", pady=11)
        ToggleRow(wrap, title, desc, var, command).pack(fill="x")
        slot = tk.Frame(wrap, bg=bg)
        slot.pack(fill="x")
        return slot

    def _build_content(self):
        main = tk.Frame(self.content, bg=COLORS["bg"])
        main.pack(fill="both", expand=True, padx=28, pady=22)
        main.columnconfigure(0, weight=1)
        main.rowconfigure(2, weight=1)

        header = tk.Frame(main, bg=COLORS["bg"])
        header.grid(row=0, column=0, sticky="ew")
        tk.Label(header, text="Results", font=FONTS["h1"], bg=COLORS["bg"],
                 fg=COLORS["text_main"]).pack(anchor="w")
        self.meta_lbl = tk.Label(header, text="No analysis yet", font=FONTS["small"], bg=COLORS["bg"],
                                 fg=COLORS["text_dim"])
        self.meta_lbl.pack(anchor="w", pady=(2, 0))

        self.stat_row = tk.Frame(main, bg=COLORS["bg"])
        self.stat_row.grid(row=1, column=0, sticky="ew", pady=(16, 0))
        self.stat_cards = []
        for i in range(4):
            self.stat_row.columnconfigure(i, weight=1, uniform="stat")
            c = StatCard(self.stat_row)
            c.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 6, 0 if i == 3 else 6))
            self.stat_cards.append(c)
        self.stat_row.grid_remove()

        self.body = tk.Frame(main, bg=COLORS["bg"])
        self.body.grid(row=2, column=0, sticky="nsew", pady=(16, 0))
        self.body.columnconfigure(0, weight=1)
        self.body.rowconfigure(0, weight=1)
        self._build_empty_state(self.body)
        self.results_panel = self._build_results_panel(self.body)
        self.results_panel.grid(row=0, column=0, sticky="nsew")
        self.results_panel.grid_remove()

        status = tk.Frame(main, bg=COLORS["bg"])
        status.grid(row=3, column=0, sticky="ew", pady=(12, 0))
        self.status_lbl = tk.Label(status, text="Ready.", font=FONTS["small"], bg=COLORS["bg"],
                                   fg=COLORS["text_sub"], anchor="w")
        self.status_lbl.pack(side="left")
        self.status_link = tk.Label(status, text="", font=FONTS["small_bold"], bg=COLORS["bg"],
                                    fg=COLORS["accent_blue"], cursor="hand2")
        self.status_link.bind("<Button-1>", self._open_status_link)

    def _build_empty_state(self, parent):
        es = tk.Frame(parent, bg=COLORS["card"], highlightthickness=1, highlightbackground=COLORS["border"])
        es.grid(row=0, column=0, sticky="nsew")
        self.empty_state = es
        center = tk.Frame(es, bg=COLORS["card"])
        center.place(relx=0.5, rely=0.5, anchor="center")
        self.es_title = tk.Label(center, text="Ready to analyze", font=FONTS["h1"], bg=COLORS["card"],
                                 fg=COLORS["text_main"])
        self.es_title.pack()
        self.es_sub = tk.Label(center, text="See who isn't following you back, and track how your "
                               "followers change over time.", font=FONTS["body"], bg=COLORS["card"],
                               fg=COLORS["text_sub"], wraplength=460, justify="center")
        self.es_sub.pack(pady=(6, 22))
        steps = [
            "Download your Instagram data in JSON format (Accounts Center → Export your information).",
            "Pick following.json and followers_1.json from the export on the left.",
            "Press Run analysis. Double-click any result to open that profile.",
        ]
        for n, text in enumerate(steps, 1):
            row = tk.Frame(center, bg=COLORS["card"])
            row.pack(fill="x", pady=5)
            tk.Label(row, text=str(n), font=FONTS["small_bold"], bg=blend(COLORS["accent_blue"], COLORS["card"], 0.8),
                     fg=COLORS["accent_blue"], width=3, pady=3).pack(side="left", anchor="n")
            tk.Label(row, text=text, font=FONTS["body"], bg=COLORS["card"], fg=COLORS["text_main"],
                     wraplength=400, justify="left", anchor="w").pack(side="left", padx=12)
        tk.Label(center, text="Tip: choose “Compare snapshots” to see who followed or unfollowed "
                 "since an older export.", font=FONTS["small"], bg=COLORS["card"], fg=COLORS["text_dim"],
                 wraplength=460, justify="center").pack(pady=(20, 0))

    def _build_results_panel(self, parent):
        panel = tk.Frame(parent, bg=COLORS["bg"])
        self.tabbar = TabBar(panel, self._select_tab)
        self.tabbar.pack(fill="x")
        tk.Frame(panel, height=1, bg=COLORS["border"]).pack(fill="x")

        toolbar = tk.Frame(panel, bg=COLORS["bg"])
        toolbar.pack(fill="x", pady=12)
        self.export_btn = RoundButton(toolbar, "Export list", self.export_current, variant="secondary")
        self.export_btn.pack(side="right", padx=(8, 0))
        self.copy_btn = RoundButton(toolbar, "Copy usernames", self.copy_visible, variant="secondary")
        self.copy_btn.pack(side="right")
        self.search = SearchEntry(toolbar, "Filter by username…", self._on_search)
        self.search.pack(side="left", fill="x", expand=True, padx=(0, 12))

        self.tree_holder = tk.Frame(panel, bg=COLORS["card"], highlightthickness=1,
                                    highlightbackground=COLORS["border"])
        self.tree_holder.pack(fill="both", expand=True)
        tk.Label(panel, text="Double-click a row to open the profile   •   Ctrl/Shift-click to select "
                 "several   •   Right-click for more", font=FONTS["small"], bg=COLORS["bg"],
                 fg=COLORS["text_dim"]).pack(anchor="w", pady=(8, 0))

        self.ctx_menu = tk.Menu(self.root, tearoff=0, bg=COLORS["card_hover"], fg=COLORS["text_main"],
                                activebackground=COLORS["accent_blue"], activeforeground="white",
                                bd=0, relief="flat")
        self.ctx_menu.add_command(label="Open profile(s)", command=lambda: self._open_selected())
        self.ctx_menu.add_command(label="Copy username(s)", command=lambda: self.copy_selected(False))
        self.ctx_menu.add_command(label="Copy profile link(s)", command=lambda: self.copy_selected(True))
        return panel

    # --- UI LOGIC HANDLERS ---

    def toggle_compare_mode_ui(self):
        if self.compare_mode_var.get():
            self.row_old.pack(fill="x", pady=4)
            self.options_box.pack_forget()
        else:
            self.row_old.pack_forget()
            self.options_box.pack(fill="x")

    def toggle_previous_file_ui(self):
        if self.track_unfollowers_var.get():
            self.row_prev.pack(fill="x", pady=(10, 0))
        else:
            self.row_prev.pack_forget()

    def toggle_ignore_list_ui(self):
        if self.use_ignore_list_var.get():
            self.row_ignore.pack(fill="x", pady=(10, 0))
        else:
            self.row_ignore.pack_forget()

    def _set_status(self, text, kind="info", link=None):
        color = {"info": COLORS["text_sub"], "success": COLORS["success"],
                 "warn": COLORS["warning"], "error": COLORS["danger"]}[kind]
        self.status_lbl.config(text=text, fg=color)
        if link:
            self.status_link.config(text=link[0])
            self._status_link_target = link[1]
            self.status_link.pack(side="right")
        else:
            self._status_link_target = None
            self.status_link.pack_forget()

    def _open_status_link(self, _e=None):
        if self._status_link_target:
            try:
                webbrowser.open(Path(self._status_link_target).resolve().as_uri())
            except Exception:
                pass

    def _show_empty_state(self, title, subtitle):
        self.es_title.config(text=title)
        self.es_sub.config(text=subtitle)
        self.stat_row.grid_remove()
        self.results_panel.grid_remove()
        self.empty_state.grid()
        self.meta_lbl.config(text="No analysis yet")
        self._export_payload = None

    # --- FILE LOADING ---

    def _pick_file(self, title, filetypes):
        kwargs = {"title": title, "filetypes": filetypes}
        if self._last_dir and os.path.isdir(self._last_dir):
            kwargs["initialdir"] = self._last_dir
        path = filedialog.askopenfilename(**kwargs)
        if path:
            self._last_dir = os.path.dirname(path)
        return path

    def load_following(self):
        path = self._pick_file("Select following.json", [("JSON", "*.json")])
        if path:
            if "following" not in os.path.basename(path).lower():
                messagebox.showerror("Error", "Select 'following.json'")
                return
            self.following_path = path
            self.row_following.set_file(os.path.basename(path))

    def load_followers(self):
        path = self._pick_file("Select followers.json", [("JSON", "*.json")])
        if path:
            if "followers" not in os.path.basename(path).lower():
                messagebox.showerror("Error", "Select 'followers.json'")
                return
            self.followers_path = path
            self.row_followers.set_file(os.path.basename(path))

    def load_old_followers(self):
        path = self._pick_file("Select the older followers file", [("JSON", "*.json")])
        if path:
            self.old_followers_path = path
            self.row_old.set_file(os.path.basename(path))

    def load_previous(self):
        path = self._pick_file("Select your previous non_follow.txt", [("Text", "*.txt")])
        if path:
            self.previous_path = path
            self.row_prev.set_file(os.path.basename(path))

    def load_ignore_list(self):
        path = self._pick_file("Select your ignore list", [("Text", "*.txt")])
        if path:
            self.ignore_list_path = path
            self.row_ignore.set_file(os.path.basename(path))

    # --- DATA EXTRACTION ---

    def extract_users(self, filepath):
        """Returns {username: follow_timestamp}. Timestamp is 0 if missing."""
        users = {}
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            items = []
            if isinstance(data, dict):
                if 'relationships_following' in data: items = data['relationships_following']
                elif 'relationships_followers' in data: items = data['relationships_followers']
            elif isinstance(data, list): items = data

            for item in items:
                title = item.get('title')
                entries = item.get('string_list_data') or [{}]
                for entry in entries:
                    name = title or entry.get('value')
                    if not name and 'instagram.com/' in entry.get('href', ''):
                        name = entry['href'].rstrip('/').split('/')[-1]
                    if name:
                        users.setdefault(name.strip(), entry.get('timestamp') or 0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{str(e)}")
        return users

    # --- SNAPSHOT ARCHIVE ---

    def save_snapshot(self, following, followers):
        """Store each run in snapshots/ (skipped if identical to the latest one)."""
        try:
            os.makedirs(SNAPSHOT_DIR, exist_ok=True)
            payload = {"following": following, "followers": followers}
            existing = sorted(f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json"))
            if existing:
                with open(os.path.join(SNAPSHOT_DIR, existing[-1]), "r", encoding="utf-8") as f:
                    last = json.load(f)
                if last.get("following") == following and last.get("followers") == followers:
                    return
            name = datetime.now().strftime("%Y-%m-%d_%H%M%S") + ".json"
            payload["taken"] = datetime.now().isoformat(timespec="seconds")
            with open(os.path.join(SNAPSHOT_DIR, name), "w", encoding="utf-8") as f:
                json.dump(payload, f)
        except Exception:
            pass  # archive failure must never block the analysis

    # --- RENAME DETECTION ---

    @staticmethod
    def detect_renames(lost, gained, old_ts, new_ts):
        """Pair lost/gained users sharing the same follow timestamp.
        Only unambiguous 1:1 matches are reported. Heuristic, not proof."""
        lost_by_ts, gained_by_ts = {}, {}
        for u in lost:
            if old_ts.get(u): lost_by_ts.setdefault(old_ts[u], []).append(u)
        for u in gained:
            if new_ts.get(u): gained_by_ts.setdefault(new_ts[u], []).append(u)
        pairs = []
        for ts, l_users in lost_by_ts.items():
            g_users = gained_by_ts.get(ts, [])
            if len(l_users) == 1 and len(g_users) == 1:
                pairs.append((l_users[0], g_users[0], ts))
        return sorted(pairs)

    # --- RESULT MODEL HELPERS ---

    @staticmethod
    def _row(user, ts, group="", gorder=0, label=None, open_user=None, copy=None):
        label = label or f"@{user}"
        return {"label": label, "open": open_user or user, "copy": copy or user,
                "group": group, "gorder": gorder, "ts": ts or 0, "search": label.lower()}

    @staticmethod
    def _tab(key, title, color, rows, date_heading, empty_msg, has_groups=False):
        return {"key": key, "title": title, "color": color, "rows": rows,
                "date_heading": date_heading, "empty_msg": empty_msg, "has_groups": has_groups,
                "visible": [], "dirty": True, "frame": None, "tree": None, "empty_lbl": None}

    # --- ANALYSIS ---

    def process_files(self):
        if not self.following_path or not self.followers_path:
            if not self.following_path: self.row_following.flash_error()
            if not self.followers_path: self.row_followers.flash_error()
            messagebox.showwarning("Missing Files",
                                   "Please select at least the Following and Followers files.")
            return

        following_ts = self.extract_users(self.following_path)
        followers_ts = self.extract_users(self.followers_path)
        following = set(following_ts)
        followers = set(followers_ts)

        if not following and not followers:
            self._show_empty_state("No usernames found",
                                   "Check that you selected the JSON files from your Instagram export.")
            self._set_status("No usernames found in the selected files.", "error")
            return

        self.save_snapshot(following_ts, followers_ts)

        if self.compare_mode_var.get():
            self._analyze_compare(following, followers, followers_ts)
        else:
            self._analyze_standard(following, followers, following_ts, followers_ts)

    def _analyze_compare(self, following, followers, followers_ts):
        if not self.old_followers_path:
            self.row_old.flash_error()
            messagebox.showerror("Missing Old File", "Please select the OLD followers file.")
            return

        old_ts = self.extract_users(self.old_followers_path)
        old_followers = set(old_ts)
        if not old_followers:
            self.row_old.flash_error()
            messagebox.showwarning("Old file is empty", "No usernames were found in the old followers file.")
            return
        lost = old_followers - followers
        gained = followers - old_followers

        renames = self.detect_renames(lost, gained, old_ts, followers_ts)
        for old_name, new_name, _ in renames:
            lost.discard(old_name)
            gained.discard(new_name)

        net = len(followers) - len(old_followers)
        row = self._row
        tabs = []

        if renames:
            rows = [row(new, ts, label=f"@{old} → @{new}", open_user=new, copy=f"{old} -> {new}")
                    for old, new, ts in renames]
            tabs.append(self._tab("renames", "Probable renames", COLORS["accent_blue"], rows,
                                  "Followed since", "No renames detected."))

        gained_rows = []
        for u in gained:
            mutual = u in following
            gained_rows.append(row(u, followers_ts.get(u), "New mutual" if mutual else "New fan",
                                   0 if mutual else 1))
        gained_rows.sort(key=lambda r: (r["gorder"], -r["ts"], r["label"]))
        tabs.append(self._tab("gained", "Gained", COLORS["success"], gained_rows, "Followed since",
                              "No new followers since the old export.", has_groups=True))

        lost_rows = []
        for u in lost:
            snake = u in following
            lost_rows.append(row(u, old_ts.get(u), "Snake (you still follow)" if snake else "Clean break",
                                 0 if snake else 1))
        lost_rows.sort(key=lambda r: (r["gorder"], -r["ts"], r["label"]))
        tabs.append(self._tab("lost", "Lost", COLORS["danger"], lost_rows, "Had followed since",
                              "Nobody unfollowed you.", has_groups=True))

        net_color = COLORS["success"] if net > 0 else COLORS["danger"] if net < 0 else COLORS["text_main"]
        cards = [
            ("Net change", f"{net:+d}", net_color, f"{len(old_followers)} → {len(followers)} followers"),
            ("Gained", len(gained), COLORS["success"], ""),
            ("Lost", len(lost), COLORS["danger"], ""),
            ("Probable renames", len(renames), COLORS["accent_blue"], "same follow timestamp"),
        ]
        payload = None
        if gained or lost or renames:
            payload = {"mode": "compare", "gained": gained, "lost": lost, "renames": renames,
                       "new_ts": followers_ts, "old_ts": old_ts}
        self._show_results(tabs, cards, "Time machine report", payload, "Export report",
                           "Analysis complete.", "info")

    def _analyze_standard(self, following, followers, following_ts, followers_ts):
        not_following_back = following - followers
        fans = followers - following
        notes, warns = [], []

        if self.ignore_famous_var.get():
            kept = {u for u in not_following_back if u.lower() not in self.famous_accounts}
            hidden = len(not_following_back) - len(kept)
            not_following_back = kept
            if hidden:
                notes.append(f"{hidden} famous account{'s' if hidden != 1 else ''} hidden")

        if self.use_ignore_list_var.get():
            if self.ignore_list_path:
                try:
                    custom_ignores = read_names(self.ignore_list_path, lower=True)
                    kept = {u for u in not_following_back if u.lower() not in custom_ignores}
                    hidden = len(not_following_back) - len(kept)
                    not_following_back = kept
                    if hidden:
                        notes.append(f"{hidden} hidden by your ignore list")
                except Exception:
                    warns.append("couldn't read the ignore list")
            else:
                warns.append("ignore list is on but no file is selected")

        is_tracking = self.track_unfollowers_var.get()
        new_unfollowers = set()
        track_empty = "No new unfollowers since your previous export."
        if is_tracking:
            if self.previous_path:
                try:
                    old_non = read_names(self.previous_path, lower=True)
                    new_unfollowers = {u for u in not_following_back if u.lower() not in old_non}
                except Exception:
                    warns.append("couldn't read the previous non_follow.txt")
                    track_empty = "The previous non_follow.txt couldn't be read."
            else:
                warns.append("select your previous non_follow.txt to spot new unfollowers")
                track_empty = "Select your previous non_follow.txt to spot new unfollowers."

        # Sort newest follow first (oldest follows are the most "stale")
        by_new = lambda ts_map: (lambda u: (-ts_map.get(u, 0), u))
        nfb_sorted = sorted(not_following_back, key=by_new(following_ts))
        fans_sorted = sorted(fans, key=by_new(followers_ts))
        new_sorted = sorted(new_unfollowers, key=by_new(following_ts))

        row = self._row
        tabs = []
        if is_tracking:
            tabs.append(self._tab("new", "New unfollowers", COLORS["danger"],
                                  [row(u, following_ts.get(u)) for u in new_sorted],
                                  "You followed", track_empty))
        tabs.append(self._tab("nfb", "Not following back", COLORS["warning"],
                              [row(u, following_ts.get(u)) for u in nfb_sorted],
                              "You followed", "Everyone you follow follows you back."))
        if self.show_fans_var.get():
            tabs.append(self._tab("fans", "Fans", COLORS["success"],
                                  [row(u, followers_ts.get(u)) for u in fans_sorted],
                                  "They followed you", "No fans to show."))

        cards = [
            ("Following", len(following), COLORS["text_main"], ""),
            ("Followers", len(followers), COLORS["text_main"], ""),
            ("Not following back", len(nfb_sorted), COLORS["warning"], ""),
            ("Mutuals", len(following & followers), COLORS["success"], ""),
        ]
        payload = None
        if nfb_sorted:
            payload = {"mode": "standard", "rows": [(u, following_ts.get(u)) for u in nfb_sorted]}
        status = " • ".join(["Analysis complete"] + notes + warns)
        self._show_results(tabs, cards, "Standard check", payload, "Export list",
                           status, "warn" if warns else "info")

    # --- RESULTS DISPLAY ---

    def _show_results(self, tabs, cards, mode_label, payload, export_label, status, status_kind):
        for old in self.tabs:
            if old["frame"] is not None:
                old["frame"].destroy()
        self.tabs = []
        self.active_key = None
        self._filter = ""
        self._sort_state = (None, False)
        self.search.clear()  # may fire the filter callback, so do it while no tabs exist
        self.tabs = tabs

        self.tabbar.set_tabs([(t["key"], t["title"], len(t["rows"]), t["color"]) for t in tabs])
        for t in tabs:
            self._build_tab_view(t)
        self._update_all()
        first = next((t for t in tabs if t["rows"]), tabs[0])
        self._select_tab(first["key"])

        for card, (title, value, color, sub) in zip(self.stat_cards, cards):
            card.set(title, value, color, sub)
        self.meta_lbl.config(text=f"{mode_label}  •  updated {datetime.now():%H:%M}")

        self._export_payload = payload
        self.export_btn.set_text(export_label)
        self.export_btn.set_enabled(payload is not None)

        self.empty_state.grid_remove()
        self.stat_row.grid()
        self.results_panel.grid()
        self._set_status(status, status_kind)

    def _heading_text(self, tab, col):
        base = {"user": "Username", "group": "Type", "date": tab["date_heading"]}[col]
        sort_col, rev = self._sort_state
        if sort_col == col:
            base += " ▼" if rev else " ▲"
        return base

    def _build_tab_view(self, tab):
        frame = tk.Frame(self.tree_holder, bg=COLORS["card"])
        cols = ("user", "group", "date")
        tree = ttk.Treeview(frame, columns=cols, show="headings", selectmode="extended",
                            style="Modern.Treeview")
        tree.configure(displaycolumns=cols if tab["has_groups"] else ("user", "date"))
        tree.column("user", width=300, minwidth=160, stretch=True, anchor="w")
        tree.column("group", width=210, minwidth=120, stretch=False, anchor="w")
        tree.column("date", width=150, minwidth=100, stretch=False, anchor="w")
        for col in cols:
            tree.heading(col, text=self._heading_text(tab, col), anchor="w",
                         command=lambda c=col: self._sort_by(c))
        sb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview, style=self._scroll_style)
        tree.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        tree.tag_configure("visited", foreground=COLORS["text_dim"])
        empty = tk.Label(frame, text="", font=FONTS["body"], bg=COLORS["card"], fg=COLORS["text_sub"],
                         justify="center", wraplength=380)

        tree.bind("<Double-1>", lambda e, t=tab: self._on_double_click(e, t))
        tree.bind("<Return>", lambda _e, t=tab: self._open_selected(t))
        tree.bind("<Control-c>", lambda _e: (self.copy_selected(False), "break")[1])
        tree.bind("<Control-a>", lambda _e, tr=tree: (tr.selection_set(tr.get_children()), "break")[1])
        if IS_MAC:
            tree.bind("<Command-c>", lambda _e: (self.copy_selected(False), "break")[1])
            tree.bind("<Button-2>", lambda e, t=tab: self._show_context_menu(e, t))
            tree.bind("<Control-Button-1>", lambda e, t=tab: self._show_context_menu(e, t))
        else:
            tree.bind("<Button-3>", lambda e, t=tab: self._show_context_menu(e, t))
        tab.update(frame=frame, tree=tree, empty_lbl=empty)

    def _compute_visible(self, tab):
        rows = tab["rows"]
        if self._filter:
            rows = [r for r in rows if self._filter in r["search"]]
        col, rev = self._sort_state
        if col:
            if col == "user":
                key = lambda r: r["label"].lower()
            elif col == "group":
                key = lambda r: (r["gorder"], r["label"].lower())
            else:
                key = lambda r: (r["ts"], r["label"].lower())
            rows = sorted(rows, key=key, reverse=rev)
        return list(rows)

    def _update_all(self):
        for tab in self.tabs:
            tab["visible"] = self._compute_visible(tab)
            tab["dirty"] = True
            self.tabbar.set_count(tab["key"], len(tab["visible"]))
            for col in ("user", "group", "date"):
                tab["tree"].heading(col, text=self._heading_text(tab, col))
        active = self._active_tab()
        if active:
            self._render_tab(active)

    def _render_tab(self, tab):
        tree = tab["tree"]
        tree.delete(*tree.get_children())
        for i, r in enumerate(tab["visible"]):
            tags = ("visited",) if r["open"] in self.visited else ()
            tree.insert("", "end", iid=str(i), values=(r["label"], r["group"], fmt_ts(r["ts"])), tags=tags)
        tab["dirty"] = False
        if tab["visible"]:
            tab["empty_lbl"].place_forget()
        else:
            if self._filter and tab["rows"]:
                msg = f"No usernames match “{self._filter}”."
            else:
                msg = tab["empty_msg"]
            tab["empty_lbl"].config(text=msg)
            tab["empty_lbl"].place(relx=0.5, rely=0.4, anchor="center")
            tab["empty_lbl"].lift()

    def _active_tab(self):
        for t in self.tabs:
            if t["key"] == self.active_key:
                return t
        return None

    def _select_tab(self, key):
        for t in self.tabs:
            if t["frame"] is not None and t["frame"].winfo_manager():
                t["frame"].pack_forget()
        self.active_key = key
        tab = self._active_tab()
        if tab:
            tab["frame"].pack(fill="both", expand=True)
            self.tabbar.select(key)
            if tab["dirty"]:
                self._render_tab(tab)

    def _sort_by(self, col):
        cur, rev = self._sort_state
        rev = (not rev) if cur == col else (col == "date")  # date starts newest-first
        self._sort_state = (col, rev)
        self._update_all()

    def _on_search(self, text):
        self._filter = text.strip().lower().lstrip("@")
        self._update_all()

    # --- ROW ACTIONS ---

    def _on_double_click(self, event, tab):
        tree = tab["tree"]
        if tree.identify_region(event.x, event.y) != "cell":
            return
        self._open_selected(tab)

    def _show_context_menu(self, event, tab):
        tree = tab["tree"]
        iid = tree.identify_row(event.y)
        if not iid:
            return
        if iid not in tree.selection():
            tree.selection_set(iid)
        tree.focus(iid)
        try:
            self.ctx_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.ctx_menu.grab_release()

    def _selected_iids(self, tab):
        iids = list(tab["tree"].selection())
        if not iids:
            focus = tab["tree"].focus()
            iids = [focus] if focus else []
        return iids

    def _selected_rows(self, tab=None):
        tab = tab or self._active_tab()
        if not tab:
            return []
        rows = []
        for iid in self._selected_iids(tab):
            try:
                rows.append(tab["visible"][int(iid)])
            except (ValueError, IndexError):
                pass
        return rows

    def _open_selected(self, tab=None):
        tab = tab or self._active_tab()
        if not tab:
            return
        iids = self._selected_iids(tab)
        if not iids:
            return
        if len(iids) > 5 and not messagebox.askyesno(
                "Open profiles", f"Open {len(iids)} profiles in your browser?"):
            return
        for iid in iids:
            try:
                r = tab["visible"][int(iid)]
            except (ValueError, IndexError):
                continue
            webbrowser.open(profile_url(r["open"]))
            self.visited.add(r["open"])
            tab["tree"].item(iid, tags=("visited",))

    def _copy_text(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def copy_selected(self, as_links=False):
        rows = self._selected_rows()
        if not rows:
            return
        items = [profile_url(r["open"]) if as_links else r["copy"] for r in rows]
        self._copy_text("\n".join(items))
        self._set_status(f"Copied {len(items)} {'link' if as_links else 'username'}"
                         f"{'s' if len(items) != 1 else ''} to the clipboard.", "success")

    def copy_visible(self):
        tab = self._active_tab()
        if not tab or not tab["visible"]:
            self._set_status("Nothing to copy.", "warn")
            return
        self._copy_text("\n".join(r["copy"] for r in tab["visible"]))
        n = len(tab["visible"])
        self._set_status(f"Copied {n} username{'s' if n != 1 else ''} to the clipboard.", "success")

    # --- EXPORTS ---

    @staticmethod
    def _export_line(user, ts):
        return f"{user} | {fmt_ts(ts)} | {profile_url(user)}\n"

    def _write_html(self, filename, title, sections):
        """sections: [(heading, [(username, timestamp)])]. Writes real clickable links."""
        css = (
            ":root{color-scheme:dark}*{box-sizing:border-box}"
            "body{margin:0;padding:40px 16px;background:#0e1116;color:#e6e9ef;"
            "font-family:'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif}"
            ".wrap{max-width:720px;margin:0 auto}"
            "h1{font-size:28px;margin:0 0 4px;background:linear-gradient(90deg,#2f8cff,#8b5cf6);"
            "-webkit-background-clip:text;background-clip:text;color:transparent}"
            ".meta{color:#667085;font-size:13px;margin-bottom:28px}"
            "section{background:#181d26;border:1px solid #262d3a;border-radius:14px;"
            "padding:18px 20px;margin-bottom:18px}"
            "h2{font-size:15px;margin:0 0 12px;color:#9ba4b5;font-weight:600}"
            "h2 span{color:#e6e9ef;background:#262d3a;border-radius:999px;padding:2px 9px;"
            "font-size:12px;margin-left:8px}"
            "ul{list-style:none;margin:0;padding:0}"
            "li{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-top:1px solid #20262f}"
            "li:first-child{border-top:0}"
            "a{color:#4da3ff;text-decoration:none;font-weight:500}a:hover{text-decoration:underline}"
            "li span{color:#667085;font-size:13px;white-space:nowrap}"
        )
        out = ["<!DOCTYPE html><html><head><meta charset='utf-8'>",
               "<meta name='viewport' content='width=device-width,initial-scale=1'>",
               f"<title>{html.escape(title)}</title><style>{css}</style></head><body><div class='wrap'>",
               f"<h1>{html.escape(title)}</h1>",
               f"<div class='meta'>Generated {datetime.now():%Y-%m-%d %H:%M}</div>"]
        for heading, rows in sections:
            out.append("<section>")
            if heading: out.append(f"<h2>{html.escape(heading)}<span>{len(rows)}</span></h2>")
            out.append("<ul>")
            for u, ts in rows:
                out.append(f"<li><a href='{html.escape(profile_url(u))}' target='_blank'>@{html.escape(u)}</a>"
                           f"<span>{fmt_ts(ts)}</span></li>")
            out.append("</ul></section>")
        out.append("</div></body></html>")
        with open(os.path.join(SCRIPT_DIR, filename), "w", encoding="utf-8") as f:
            f.write("\n".join(out))

    def export_current(self):
        p = self._export_payload
        if not p:
            return
        if p["mode"] == "standard":
            self.export_list(p["rows"], "non_follow.txt")
        else:
            self.export_diff(p["gained"], p["lost"], p["renames"], p["new_ts"], p["old_ts"])

    def export_list(self, rows, filename):
        """rows: [(username, timestamp)]. Each line: user | date | profile link."""
        try:
            path = os.path.join(SCRIPT_DIR, filename)
            with open(path, "w", encoding="utf-8") as f:
                for u, ts in rows: f.write(self._export_line(u, ts))
            html_name = os.path.splitext(filename)[0] + ".html"
            self._write_html(html_name, "Not Following Back", [("", rows)])
            self._set_status(f"Saved to {filename} and {html_name}", "success",
                             link=("Open HTML report", os.path.join(SCRIPT_DIR, html_name)))
        except Exception as e: messagebox.showerror("Error", str(e))

    def export_diff(self, gained, lost, renames, new_ts, old_ts):
        try:
            path = os.path.join(SCRIPT_DIR, "diff_report.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("=== REPORT ===\n\nGAINED:\n")
                for u in sorted(gained): f.write(self._export_line(u, new_ts.get(u)))
                f.write("\nLOST:\n")
                for u in sorted(lost): f.write(self._export_line(u, old_ts.get(u)))
                f.write("\nPROBABLE RENAMES (old -> new):\n")
                for old_name, new_name, ts in renames:
                    f.write(f"{old_name} -> {new_name} | {fmt_ts(ts)} | {profile_url(new_name)}\n")
            self._write_html("diff_report.html", "Diff Report", [
                ("Gained", [(u, new_ts.get(u)) for u in sorted(gained)]),
                ("Lost", [(u, old_ts.get(u)) for u in sorted(lost)]),
                ("Probable renames (new name shown)", [(n, ts) for _, n, ts in renames]),
            ])
            self._set_status("Saved to diff_report.txt and diff_report.html", "success",
                             link=("Open HTML report", os.path.join(SCRIPT_DIR, "diff_report.html")))
        except Exception as e: messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    try: os.chdir(SCRIPT_DIR)
    except Exception: pass
    root = tk.Tk()
    app = InstagramCheckerApp(root)
    root.mainloop()
