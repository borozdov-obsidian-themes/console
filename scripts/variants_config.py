"""Which sibling themes become Style Settings variants of this one."""

ID = "borozdov-console"  # Style Settings section id and the body-class prefix
NAME = "Borozdov Console"
DEFAULT_LABEL = "Console"

# (repository folder next to this one, label in the Variant menu)
MEMBERS = [
    ("signal", "Signal"),
    ("beacon", "Beacon"),
    ("neon", "Neon"),
    ("phosphor", "Phosphor"),
    ("cockpit", "Cockpit"),
    ("cathode", "Cathode"),
    ("deck", "Deck"),
    ("stage", "Stage"),
    ("claret", "Claret"),
    ("ticker", "Ticker"),
    ("forge", "Forge"),
    ("nebula", "Nebula"),
    ("velvet", "Velvet"),
]

# Palette names of this theme that no Obsidian variable reads in section 3:
# which of the sibling's resolved variables to take for them instead.
ALIASES = {
    "--on-wash": "--tag-color",
    "--pulse-light": "--interactive-accent-hover",
}

# The palette name the highlight rule colours its text with: the generator
# picks whichever of the sibling's text and canvas reads on its highlight.
MARK_TEXT = "--on-mark"
