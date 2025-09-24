import wikipedia
import urllib

def search_wikipedia():
    try:
        # Set the language for the Wikipedia search to Indonesian
        wikipedia.set_lang("id")
        
        # Define your search phrase
        search_phrase = input("Anda cari tahu apa? : ").strip()
        
        if not search_phrase:
            print("Error: Masukan tidak boleh kosong.")
            return
            
        # Search for the page and get a summary
        try:
            # Set the number of sentences for the summary
            summary = wikipedia.summary(search_phrase, sentences=2)
            print(f"\nRingkasan untuk '{search_phrase}':\n")
            print(summary)
            
        except wikipedia.exceptions.PageError:
            print(f"\nError: Halaman untuk '{search_phrase}' tidak ditemukan.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"\nError: '{search_phrase}' adalah halaman disambiguasi. Mohon lebih spesifik.")
            print("Pilihan yang tersedia:", ", ".join(e.options[:5]) + "...")
    
    except urllib.error.URLError:
        print("\nError: Tidak dapat terhubung ke Wikipedia. Mohon periksa koneksi internet Anda.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    search_wikipedia()