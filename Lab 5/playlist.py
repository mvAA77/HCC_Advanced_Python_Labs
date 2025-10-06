### Tanya Kadiyala
### CMSY-257-300
### Lab 5
### Problem 4

def display_playlist(playlist):
    if not playlist:
        print("Playlist is empty.")
        return
    
    print("\n" + "="*60)
    print(f"{'#':<3} {'Title':<20} {'Artist':<20} {'Duration':<10}")
    print("="*60)
    
    for i, song in enumerate(playlist, 1):
        title, artist, duration = song
        print(f"{i:<3} {title:<20} {artist:<20} {duration:<10.2f} min")
    
    print("="*60)
    
    total_duration = sum(song[2] for song in playlist)
    print(f"Total playlist duration: {total_duration:.2f} minutes")
    print("="*60)

def add_song(playlist):
    print("\n--- Add New Song ---")
    title = input("Enter song title: ").strip()
    artist = input("Enter artist: ").strip()
    
    try:
        duration = float(input("Enter duration in minutes: "))
        if duration <= 0:
            print("Error: Duration must be positive.")
            return playlist
    except ValueError:
        print("Error: Duration must be a number.")
        return playlist
    
    playlist.append([title, artist, duration])
    print(f"Added '{title}' by {artist} to playlist")
    return playlist

def remove_song(playlist):
    if not playlist:
        print("Playlist is empty. Add songs first.")
        return playlist
    
    print("\n--- Remove Song ---")
    search_title = input("Enter song title to remove: ").strip().lower()
    
    for i, song in enumerate(playlist):
        if song[0].lower() == search_title:
            removed_song = playlist.pop(i)
            print(f"Removed '{removed_song[0]}' by {removed_song[1]} from playlist")
            return playlist
    
    print(f"Song '{search_title}' not found in playlist.")
    return playlist

def write_playlist_to_file(playlist, filename="playlist_output.txt"):
    try:
        with open(filename, 'w') as f:
            f.write("My Music Playlist\n")
            f.write("=" * 40 + "\n")
            
            for i, song in enumerate(playlist, 1):
                title, artist, duration = song
                f.write(f"{i}. {title} - {artist} ({duration:.2f} min)\n")
            
            total_duration = sum(song[2] for song in playlist)
            f.write("=" * 40 + "\n")
            f.write(f"Total: {len(playlist)} songs, {total_duration:.2f} minutes\n")
        
        print(f"Playlist written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    print("=== Music Playlist Manager ===")
    playlist = []
    
    while True:
        print("\n--- Playlist Menu ---")
        print("1. Display Playlist")
        print("2. Add Song")
        print("3. Remove Song")
        print("4. Save Playlist to File")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_playlist(playlist)
        elif choice == '2':
            playlist = add_song(playlist)
        elif choice == '3':
            playlist = remove_song(playlist)
        elif choice == '4':
            if playlist:
                filename = input("Enter output filename (or press Enter for default): ").strip()
                if not filename:
                    filename = "playlist_output.txt"
                write_playlist_to_file(playlist, filename)
            else:
                print("Playlist is empty. Add songs first.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()