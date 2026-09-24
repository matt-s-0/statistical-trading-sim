import tkinter as tk
import ctypes

# methods

# Expands scrollbar when creating new candles every 100ms
def updateScrollSpace(chartCanvas: tk.Canvas) -> None:
    chartCanvas.configure(scrollregion=chartCanvas.bbox("all"))
    Root.after(100, lambda: updateScrollSpace(chartCanvas))

# vars
ColumnWidth = 40
CanvasColumnSpacing = 20

# Create window & configure it
Root = tk.Tk()
Root.geometry("800x600")
# Root.overrideredirect(True)

# Title bar
TitleBar = tk.Frame(Root, bg="#2e2e2e", relief="raised", bd=0)
TitleBar.pack(fill="x", side="top")

TitleLabel = tk.Label(TitleBar, text="Test title bar", bg="#2e2e2e", fg="white")
TitleLabel.pack(side="left", padx=10, pady=5)

CloseButton = tk.Button(
    TitleBar, 
    text="X",
    command=Root.destroy, 
    bg="#2e2e2e", 
    fg="white", 
    bd=0, 
    activebackground="red", 
    activeforeground="white",
    cursor="hand2"
)
CloseButton.pack(side="right", padx=5, pady=5)

# Side bar
SideBar = tk.Frame(Root, width=80, height=610, background="#2a2a2a")
SideBar.pack(anchor="w", side="left")

# Main frame
MainFrame = tk.Frame(Root, bg="#1f1f1f")
MainFrame.pack(fill="both", expand=True)

# A canvas allows rectangles and other shapes to be created, which is useful for making candles
chartCanvas = tk.Canvas(MainFrame, background="#1f1f1f", highlightthickness=0)
chartCanvas.pack(fill="both", expand=True)

# Creates a scrollbar so you can scroll horizontally to see candlesticks that are out of view
scrollbar = tk.Scrollbar(MainFrame, orient="horizontal", command=chartCanvas.xview)
scrollbar.pack(side="bottom", fill="x")

# Sets the scrollbar to scroll the chart canvas
chartCanvas.configure(xscrollcommand=scrollbar.set)

# Makes it so that when your mouse is over the canvas you can use the scrollbar
chartCanvas.bind("<Shift-MouseWheel>", lambda event: chartCanvas.xview_scroll(-1 * (event.delta // 120), "units"))

for i in range(30):
    x1 = i* (ColumnWidth + CanvasColumnSpacing)
    x2 = x1 + ColumnWidth

    chartCanvas.create_rectangle(x1, 0, x2, 50, outline="white")


# Window dragging using ctypes so I can use native windows title bar dragging,
# which runs much more efficiently than a custom tkinter set up
user32 = ctypes.windll.user32

WM_NCLBUTTONDOWN = 0x00A1
HTCAPTION = 0x0002

def startDrag(event):
    user32.ReleaseCapture()

    Root.after(1, lambda: user32.PostMessageW(hwnd, WM_NCLBUTTONDOWN, HTCAPTION, 0))

TitleBar.bind("<Button-1>", startDrag)
TitleLabel.bind("<Button-1>", startDrag)

# Start updating the canvas scroll
updateScrollSpace(chartCanvas)

Root.update_idletasks()

# Get the window handle
hwnd = Root.winfo_id()

# Get the top level window hwnd
GA_Root = 2
hwnd = user32.GetAncestor(hwnd, GA_Root)

# Windows window API style vars so I can remove the title bar & resizing without removing native title bar dragging & the taskbar icon
# https://learn.microsoft.com/en-us/windows/win32/winmsg/window-styles
# https://learn.microsoft.com/en-us/windows/win32/winmsg/extended-window-styles
GWL_STYLE = -16
WS_CAPTION = 0x00C00000
WS_THICKFRAME = 0x00040000
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000
WS_SYSMENU = 0x00080000

# Get the current style
style = user32.GetWindowLongW(hwnd, GWL_STYLE)

# Removes title bar
style &= ~WS_CAPTION
style &= ~WS_THICKFRAME

# Applies the new style
user32.SetWindowLongW(hwnd, GWL_STYLE, style)

# Forces windows to recalculate the window
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOZORDER = 0x0004
SWP_FRAMECHANGED = 0x0020

user32.SetWindowPos(
    hwnd,
    0,
    0, 0, 0, 0,
    SWP_NOMOVE |
    SWP_NOSIZE |
    SWP_NOZORDER |
    SWP_FRAMECHANGED
)


Root.mainloop()