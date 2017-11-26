import os
#
# The notifier function
def notify(title, subtitle, message,execute,activate):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    e = '-execute {!r}'.format(execute)
    a = '-activate {!r}'.format(activate)

    os.system('terminal-notifier {}'.format(' '.join([m, t, s, e, a])))

# Calling the function
notify(title    = 'Big Brother',
       subtitle = 'Similar Project Charters',
       message  = 'Found project charters similar to what you are working on! Click here to find out more!',
       execute = 'python showDoc.py',
       activate = 'com.apple.Terminal')
# import os
#
# def notify(title, text):
#     os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title))
#
# notify("Big Brother", "Found project charters similar to what you are working on! Click here to find out more!")
