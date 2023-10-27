import tkinter as tk
from tkinter import filedialog, messagebox


def create_gui(search_function):
    window = tk.Tk()
    window.title("ChatGPT Conversation Searcher")

    # Directory selection
    directory_label = tk.Label(window, text="Select directory containing ChatGPT conversations:")
    directory_label.pack(pady=10)

    directory_var = tk.StringVar()
    directory_entry = tk.Entry(window, textvariable=directory_var, width=50)
    directory_entry.pack(pady=5, padx=10, side=tk.LEFT)

    browse_button = tk.Button(window, text="Browse", command=lambda: browse_directory(directory_var))
    browse_button.pack(pady=5, side=tk.LEFT)

    # Search input
    search_label = tk.Label(window, text="Enter search term:")
    search_label.pack(pady=10)

    search_var = tk.StringVar()
    search_entry = tk.Entry(window, textvariable=search_var, width=60)
    search_entry.pack(pady=5, padx=10)

    search_button = tk.Button(window, text="Search",
                              command=lambda: perform_search(search_function, directory_var.get(), search_var.get(),
                                                             result_text))
    search_button.pack(pady=10)

    # Display results
    result_label = tk.Label(window, text="Search Results:")
    result_label.pack(pady=10)

    result_text = tk.Text(window, width=80, height=20, wrap=tk.WORD)
    result_text.pack(pady=10, padx=10)

    window.mainloop()


def browse_directory(directory_var):
    directory = filedialog.askdirectory()
    if directory:
        directory_var.set(directory)


def perform_search(search_function, directory, query, result_text_widget):
    results = search_function(directory, query)

    result_text_widget.delete(1.0, tk.END)  # Clear previous results

    if not results:
        messagebox.showinfo("Search Result", "No conversations found for your query.")
    else:
        for filename, content in results.items():
            result_text_widget.insert(tk.END, f"Found in {filename}:\n{content}\n\n")

