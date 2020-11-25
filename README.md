# reverse_shell_it
(ITA) Reverse shell molto semplice, scritta sfruttando le librerie socket e subprocess di python, da utilizzare in LAN.

Permette al client, la macchina che ha in esecuzione il file client.py, di scrivere e inviare comandi alla macchina “vittima”, che ha quindi in esecuzione il file server.py, che saranno poi interpretati da quest’ultima. Il client riceverà poi, dalla macchina “attaccata”, l’output del comando precedentemente inviato.

Si tratta di script molto semplici che funzionano esclusivamente in LAN, ma che permettono di eseguire qualsiasi tipo di comando e di ricevere il relativo output anche se quest'ultimo non dovesse supportare la codifica UTF-8.

Puoi guardare lo speed coding di questo script (in italiano) a questo link: https://youtu.be/36bqbftsU7Y
