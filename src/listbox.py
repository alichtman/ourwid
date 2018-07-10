# Aaron Lichtman
# Displays a list box with a set of choices.
import urwid

def item_chosen(button, choice):
	response = urwid.Text([u'You chose ', choice, u'\n'])
	done = urwid.Button(u'Ok')
	urwid.connect_signal(done, 'click', exit_program)
	main.original_widget = urwid.Filler(urwid.Pile([response, urwid.AttrMap(done, None, focus_map='reversed')]))


def exit_program(button):
	raise urwid.ExitMainLoop()


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


if __name__ == '__main__':
	choices = ["Choice 1", "Choice 2", "Choice 3"]
	main = urwid.Padding(menu(u'Options', choices), left=2, right=2)
	top = urwid.Overlay(main, urwid.SolidFill(u'\N{LIGHT SHADE}'),
	                    align='left', width=('relative', 0),
	                    valign='top', height=('relative', 0),
	                    min_width=20, min_height=7)
	urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
