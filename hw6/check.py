from datetime import time


def test_dark_theme():
    a = [time(hour=0),
         time(hour=1),
         time(hour=2),
         time(hour=3),
         time(hour=4),
         time(hour=5),
         time(hour=6),
         time(hour=7),
         time(hour=8),
         time(hour=9),
         time(hour=10),
         time(hour=11),
         time(hour=12),
         time(hour=13),
         time(hour=14),
         time(hour=15),
         time(hour=16),
         time(hour=17),
         time(hour=18),
         time(hour=19),
         time(hour=20),
         time(hour=21),
         time(hour=22),
         time(hour=23)]

    current_time = time(hour=23)
    dark_theme_enabled = False
    is_dark_theme = True

    print('')
    for t in a:

        if dark_theme_enabled == True:
            is_dark_theme = True
        elif 5 < t.hour < 22:
            is_dark_theme = False
        else:
            is_dark_theme = True

        print(str(t.hour) + ': ' + str(is_dark_theme))
