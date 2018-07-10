# Aaron Lichtman
# Displays a list box with a set of choices.

def menu(title, choices):
	"""
	Make a menu with choices displayed.
	"""
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c)
		urwid.connect_signal(button, 'click', item_chosen, c)
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def main():
    choices = ["Activate/Deactivate Automated Trading", "Deposit/Withdraw Money", "Place Your Own Trade"]
    menu("Options", choices)
