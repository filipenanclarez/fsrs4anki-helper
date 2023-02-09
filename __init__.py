from anki.lang import _
from aqt.gui_hooks import deck_browser_will_show_options_menu
from aqt import mw

from .reschedule import reschedule
from .postpone import postpone
from .advance import advance


def addToMain(fun, text, shortcut=None):
    """fun -- without argument
    text -- the text in the menu
    """
    action = mw.form.menuTools.addAction(text)
    action.triggered.connect(lambda b, did=None: fun(did))
    if shortcut:
        action.setShortcut(shortcut)


def addActionToGear(fun, text):
    """fun -- takes an argument, the did
    text -- what's written in the gear."""

    def aux(m, did):
        a = m.addAction(text)
        a.triggered.connect(lambda b, did=did: fun(did))

    deck_browser_will_show_options_menu.append(aux)


addToMain(reschedule, _("Reschedule all cards"), "CTRL+R")
addActionToGear(reschedule, "Reschedule cards in deck")

addToMain(postpone, _("Postpone all cards"))
addActionToGear(postpone, "Postpone cards in deck")

addToMain(advance, _("Advance all cards"))
addActionToGear(advance, "Advance cards in deck")
