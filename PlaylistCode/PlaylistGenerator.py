"""The user is prompted to choose their desired music genre and number of songs(up to 12)
A playlist is then generated from a stored selection of songs"""
import tkinter as tk
from tkinter import ttk, messagebox
import random

class PlaylistGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Playlist Generator")
        self.master.geometry("400x350")

        # Define genres and associated songs and images
        self.genres = {
            "Pop": {
                "songs": ["Barbie Girl", "Genie in a Bottle", "Everybody", "Wannabe", "Believe", "I want it that way", "Diamonds","Locked Out of Heaven","See You Again", "Mirrors", "Last Friday Night", "Wake Me Up"],
                "image": "pop.jpeg",
                "alt_text": " "
            },
            "Rock": {
                "songs": ["Going Under", "Chop Suey!", "Lost In Hollywood", "Last Resort", "Numb", "I Write Sins Not Tragedies", "Kryptonite","The Kill","Mr. Brightside", "The Pretender","I Hate Everything About You", "Dance, Dance"],
                "image": "rock.jpeg",
                "alt_text": ""
            },
            "Jazz": {
                "songs": ["Fly Me To The Moon", "Dream A Little Dream of Me", "Stormy Weather", "Blue Moon", "Summertime", "My Favorite Things","Blue Train", "Autumn Leaves","Gary's Theme","Lullaby Of Birdland","St. Thomas", "Lover Man"],
                "image": "jazz.jpeg",
                "alt_text": " "
            },
            "Classical": {
                "songs": ["St Matthew Passion", "Otello", "The Marriage of Figaro", "The Well-Tempered Clavier", "Aida", "The Nutcracker", "Pictures at an Exhibition", "La boheme", "The Four Seasons","Requiem","Symphony No.5","Madama Butterfly"],
                "image": "classical.jpeg",
                "alt_text": " "
            }
        }

        self.create_widgets()

    def create_widgets(self):
        #Create the main window
        self.label1 = tk.Label(self.master, text="Playlist Generator", font=("Arial", 18))
        self.label1.pack(pady=10)

        #Create the genre selection dropdown
        self.genre_label = tk.Label(self.master, text="Select Genre:")
        self.genre_label.pack()
        self.genre_combobox = ttk.Combobox(self.master, values=list(self.genres.keys()), state="readonly")
        self.genre_combobox.pack()

        #Create the number of songs dropdown
        self.num_songs_label = tk.Label(self.master, text="Number of Songs:")
        self.num_songs_label.pack()
        self.num_songs_combobox = ttk.Combobox(self.master, values=[str(i) for i in range(1, 13)], state="readonly")
        self.num_songs_combobox.pack()

        #Create buttons
        self.generate_button = ttk.Button(self.master, text="Generate Playlist", command=self.generate_playlist)
        self.generate_button.pack(pady=10)
        self.exit_button = ttk.Button(self.master, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

        #REMOVE MAYBE
        self.image_label = tk.Label(self.master, text="Playlist Image", font=("Arial", 12))
        self.image_label.pack()

    def generate_playlist(self):
        #Retrieve the selected genre and number of songs
        genre = self.genre_combobox.get()
        if not genre:
            messagebox.showerror("Error", "Please select a genre.")
            return

        num_songs = self.num_songs_combobox.get()
        if not num_songs.isdigit() or int(num_songs) <= 0:
            messagebox.showerror("Error", "Please enter a valid number of songs.")
            return
        #Limit to 12 or fewer songs
        num_songs = min(int(num_songs), 12)

        #Create a new windoe for the generated playlist
        playlist_window = tk.Toplevel(self.master)
        playlist_window.title("Generated Playlist")
        playlist_window.geometry("400x350")

        #Display the playlist label
        playlist_label = ttk.Label(playlist_window, text=f"Your Random {genre} Playlist:")
        playlist_label.pack(pady=10)

        # Retrieve the list of songs for the selected genre and the associated image
        genre_data = self.genres.get(genre, {})
        songs = genre_data.get("songs", [])
        genre_image = genre_data.get("image", "")
        alt_text = genre_data.get("alt_text", " ")

        #Display error message if no genre is selected
        if not songs:
            messagebox.showerror("Error", "No songs found for the selected genre.")
            return

        #Shuffle the list of songs
        random.shuffle(songs)

        # Display the selected number of songs
        for idx, song in enumerate(songs[:num_songs], start=1):
            song_label = ttk.Label(playlist_window, text=f"{idx}. {song}")
            song_label.pack()

        # Display genre image with the alt text
        if genre_image:
            img = tk.PhotoImage(file=genre_image)
            image_label = tk.Label(playlist_window, image=img)
            image_label.image = img
            image_label.pack()

    def exit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = PlaylistGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()   