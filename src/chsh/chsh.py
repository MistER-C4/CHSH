#Code for calculating the CHSH game results
import tkinter as tk
from tkinter import simpledialog
import ctypes
import random

def center_window(window, width, height):
    """"Centers a Tkinter window on the screen."""
    window.update_idletasks()  # make sure size info is ready

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

for i in range(2):
    """Create a GUI to reveal the referee's chosen bits one at a time and get the players' bits via input dialogs."""
    referee_bit = random.randint(0, 1)
    def toggle_visibility():
        if label.cget("text") == "•":
            label.config(text=referee_bit)
            toggle_btn.config(text="Hide")
        else:
            label.config(text="•")
            toggle_btn.config(text="Reveal")

    root = tk.Tk()
    root.title("Hidden Bit")

    tk.Label(root, text="Secret bit:").pack(pady=5)

    # concealed by default
    label = tk.Label(root, text="•", font=("Arial", 24))
    label.pack(pady=10)

    toggle_btn = tk.Button(root, text="Reveal", command=toggle_visibility)
    toggle_btn.pack(pady=5)

    center_window(root, 250, 150)

    root.mainloop()

    if i == 0:
        referee_bitA = referee_bit
        alice_bit = simpledialog.askinteger(title="Alice's bit", prompt="Enter Alice's bit (0 or 1):")
        if alice_bit != 0 and alice_bit != 1:
            raise ValueError("Alice's bit must be 0 or 1")
    elif i == 1:
        referee_bitB = referee_bit
        bob_bit = simpledialog.askinteger(title="Bob's bit", prompt="Enter Bob's bit (0 or 1):")
        if bob_bit != 0 and bob_bit != 1:
            raise ValueError("Bob's bit must be 0 or 1")
    #print(referee_bit)

def c_game(RA, RB, A, B):
    """Calculates the result of the CHSH game."""
    referee_result = RA*RB
    player_result = A ^ B
    print(referee_result, player_result)
    if referee_result == player_result:
        print("Congratualtions! You win the CHSH game!")
    elif referee_result != player_result:
        print("Sorry, you lost the CHSH game.")

result = c_game(referee_bitA, referee_bitB, alice_bit, bob_bit)
print("Referee bits:", referee_bitA, referee_bitB, "Alice's bit:", alice_bit, "Bob's bit:", bob_bit)