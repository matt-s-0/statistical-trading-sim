import tkinter as tk

# Create window & configure it
root = tk.Tk()
root.geometry("800x600")
root.overrideredirect(True)
root.resizable(False,False)

# Title bar
titleBar = tk.Frame(root, bg="#2e2e2e", relief="raised", bd=0)
titleBar.pack(fill="x", side="top")

titleLabel = tk.Label(titleBar, text="Test title bar", bg="#2e2e2e", fg="white")
titleLabel.pack(side="left", padx=10, pady=5)

closeButton = tk.Button(
    titleBar, 
    text="X",
    command=root.destroy, 
    bg="#2e2e2e", 
    fg="white", 
    bd=0, 
    activebackground="red", 
    activeforeground="white",
    cursor="hand2"
)
closeButton.pack(side="right", padx=5, pady=5)

# Side bar
sideBar = tk.Frame(root, width=80, height=575, background="#2a2a2a")
sideBar.pack(anchor='w', side='left')

# Main frame
mainFrame = tk.Frame(root, bg="#1f1f1f")
mainFrame.pack(fill="both", expand=True)

label = tk.Label(mainFrame, text="Test text", bg="#1f1f1f", fg="white", font=("Helvetica", 16))
label.pack(expand=True)

# Window dragging
# Shows an error in the IDE but does not cause an error while running
titleBar.bind("<Button-1>", lambda event: setattr(titleBar, 'offset', (event.x, event.y)))
titleBar.bind("<B1-Motion>", lambda event: root.geometry(f"+{root.winfo_pointerx() - titleBar.offset[0]}+{root.winfo_pointery() - titleBar.offset[1]}"))

titleLabel.bind("<Button-1>", lambda event: setattr(titleBar, 'offset', (event.x, event.y)))
titleLabel.bind("<B1-Motion>", lambda event: root.geometry(f"+{root.winfo_pointerx() - titleBar.offset[0]}+{root.winfo_pointery() - titleBar.offset[1]}"))

# Note for future don't put anything below this or it won't run I think
root.mainloop()