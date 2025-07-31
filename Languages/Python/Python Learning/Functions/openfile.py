from tkinter import filedialog as fd

path: str = fd.askopenfilename(title='Select a file')
print(path)
