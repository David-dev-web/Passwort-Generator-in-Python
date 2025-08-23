import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

# Funktion zum Generieren des Passworts
def passwort_generieren():
    try:
        laenge = int(entry_laenge.get())
        if laenge < 4:
            messagebox.showwarning("Fehler", "Passwort sollte mindestens 4 Zeichen lang sein.")
            return
        zeichen = string.ascii_letters + string.digits + string.punctuation
        passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
        entry_passwort.config(state=tk.NORMAL)
        entry_passwort.delete(0, tk.END)
        entry_passwort.insert(0, passwort)
        entry_passwort.config(state="readonly")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")

# Funktion zum Kopieren des Passworts
def passwort_kopieren():
    root.clipboard_clear()
    root.clipboard_append(entry_passwort.get())
    root.update()
    messagebox.showinfo("Kopiert", "Passwort wurde in die Zwischenablage kopiert!")

# GUI erstellen
root = tk.Tk()
root.title("Passwort-Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Stil setzen
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#2c3e50", foreground="white")

# Widgets erstellen
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Passwortlänge:").pack(pady=5)
entry_laenge = ttk.Entry(frame, justify="center")
entry_laenge.pack(pady=5)

btn_generieren = ttk.Button(frame, text="Passwort generieren", command=passwort_generieren)
btn_generieren.pack(pady=5)

entry_passwort = ttk.Entry(frame, justify="center", state="readonly", width=30)
entry_passwort.pack(pady=5)

btn_kopieren = ttk.Button(frame, text="Kopieren", command=passwort_kopieren)
btn_kopieren.pack(pady=5)

# GUI starten
def passwort_loeschen(event=None):
    entry_passwort.config(state=tk.NORMAL)  # Schreibschutz deaktivieren
    entry_passwort.delete(0, tk.END)  # Passwort löschen
    entry_passwort.config(state="readonly")  # Schreibschutz wieder aktivieren

# Keybinding für "Entf"-Taste
root.bind("<Delete>", passwort_loeschen)
root.mainloop()
