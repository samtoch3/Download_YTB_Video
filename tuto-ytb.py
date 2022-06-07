# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:09:25 2022

@author: Samson Thibaut
"""

from pytube import YouTube


print('Download started')

YouTube('https://www.youtube.com/watch?v=WXfTq4c9JmE').streams.filter(res='720p').first().download()

print('Download ended')




"""
https://www.youtube.com/watch?v=1o4oS8iTiyU -> KS BLOOM - C'EST DIEU 

https://www.youtube.com/watch?v=2B2UJvLFKok -> Le pouvoir de la confiance en soi. Brian Tracy. Livre audio

https://www.youtube.com/watch?v=MySVhNQgbQs -> Above All - Piano Instrumental

https://www.youtube.com/watch?v=cMOcgkkyOFw -> Tous les guitaristes ont déjà joué ça

https://www.youtube.com/watch?v=JVxwE31Z9As -> 3 effets faciles à jouer sur une guitare acoustique

https://www.youtube.com/watch?v=xGfbduLuZlo -> Bless the Lord o my soul song with Lyrics💘

https://www.youtube.com/watch?v=M2S9z33nH4g - https://www.youtube.com/watch?v=7lkc-023qTA -> Let it Shine | Clip musical

https://www.youtube.com/watch?v=vU-P-K5qtDM -> Darina Victry - Laisse moi t'aimer (Paroles)

https://www.youtube.com/watch?v=Ze5jSeX4Iws -> Père riche père pauvre. Robert T. Kiyosaki. Livre audio

https://www.youtube.com/watch?v=zUtv08k5u2E -> Un rien peut tout changer, Atomic Habits in French by James Clear with subtitles

https://www.youtube.com/watch?v=7-nFL84GfUA -> 7 Habitudes SUBTILES qui vous Rendent Mentalement Fort

https://www.youtube.com/watch?v=Gr3c3uQ5Pnw -> Atomic Habits (un rien peut tout changer) de James Clear (en 5 idées simples)

https://www.youtube.com/watch?v=c9fyV_lwQvE -> DEVENIR UN MAÎTRE DU PASSAGE À L'ACTION : LES BASES DE LA PROCRASTINATION

https://www.youtube.com/watch?v=IJquFNL5GYQ -> Le pouvoir des habitudes. Changer un rien pour tout changer. Charles Duhigg. Livre audio

https://www.youtube.com/watch?v=odKw-O_MVWY -> Réfléchissez et devenez riche: Les lois du succès de Napoleon Hill. Napoleon Hill. Livre audio

https://www.youtube.com/watch?v=TuQuFzktoB4 -> MANON VUOKO - "FRIENDZONER" LIVE SESSION

https://www.youtube.com/watch?v=4hRudtRmaqo -> ARRÊTEZ DE FAIRE PLAISIR AUX GENS - Meilleur Discours de Ed Mylett, Joel Osteen, Gary V en Français

https://www.youtube.com/watch?v=WXfTq4c9JmE -> La discipline personnelle. Développer sa personnalité. Michael Wilson. Livre audio complet



nhttps://www.youtube.com/watch?v=fxN5eY3rAf0 -> Livre audio-l' art d'avoir toujours raison-Arthur Schopenhauer-livre audio

https://www.youtube.com/watch?v=3rtPQRNoJ1o -> LA MAGIE DE VOIR GRAND : DAVID J. SCHWARTZ

"""