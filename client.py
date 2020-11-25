import socket, sys, time

def comandi(s):
    while(True):
        try:
            print('''

                Digita un qualsiasi comando.
                Per uscire dal server e dal progrmma premi "ctrl + c"

                ''')
            com = input("\n--> ")
            s.send(com.encode())
            dati = s.recv(1048000)
            print(str(dati, "utf-8"))
            continue    
        except KeyboardInterrupt:
            print("uscita dal server in corso...")
            s.close()
            time.sleep(4)
            sys.exit(0)

        except UnicodeDecodeError:
            print("ATTENZIONE\nil comando inserito non supporta la codifica utf-8, di conseguenza verrà ritornata la sua versione originale.")
            print(dati)

            
def conne_server(indirizzo):
    try:
        s = socket.socket()
        s.connect(indirizzo)
        print(f"conne stabilita con il server all'indirizzo: {indirizzo}")
    except socket.error as errore:
        print(f"qualcosa è andato storto durnte la connesione\n{errore}")
        retry = input("riprovare? Y/N: ")
        if retry == "Y" or retry == "y":
            conne_server(indirizzo)
        else:
            print("nessuna connessione stabilita. uscita..")
            sys.exit(0)
    comandi(s)


if __name__ == "__main__":
    
    print("Attesa di una connessione al server...")
    conne_server(("192.168.1.1", 15000))   # devi cambiare l'indirizzo ip se è differente
