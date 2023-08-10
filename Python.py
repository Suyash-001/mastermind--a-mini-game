# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:38:37 2020

@author: J
"""
import tkinter as tk
import sys

class s:
    def k():
        def I():
            B = C.get()
            D = A.get()
            if D in [""]:
                root11 = tk.Tk()
                tk.Label(root11, text="oops! There is no key. Please put a valid key").pack()
                tk.Button(root11, text="OK", height=1, width=2, command=root11.destroy).pack()
            else:
                for i in range(len(D)):
                    if D[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        root12 = tk.Tk()
                        tk.Label(root12, text="The entered key is not valid, please enter a valid key").pack()
                        tk.Button(root12, text="OK", height=1, width=2, command=root12.destroy).pack()
                        root12.mainloop()
                        break
                    elif D[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        break
                if len(D) == 4:
                    l4 = []
                    l5 = []
                    l6 = []
                    for i in range(len(D)):
                        if D.count(D[i]) > 1:
                            l4.append(D[i])
                        else:
                            l5.append(D[i])
                        l6.append(D[i])
                    if l4 == []:
                        root16 = tk.Tk()
                        T = tk.Text(root16, height=10, width=40)
                        T.pack()
                        root16.protocol("WM_DELETE_WINDOW", root16.withdraw)
                        if B == D:
                            key="You guessed the key",D
                            root13 = tk.Tk()
                            root16.destroy()
                            tk.Label(root13, text="CONGRATULATIONS", font="Arial 30 bold").pack()
                            tk.Label(root13, text=key, font="arial 20").pack()
                            tk.Button(root13, text="OK", command=sys.exit).pack()
                        else:
                            B = C.get()
                            root16=tk.Tk()
                            root16.deiconify()
                            count = 0
                            count2 = 0
                            for i in range(4):
                                if D[i] == B[i]:
                                    count += 1
                            for i in range(4):
                                if D[i] in B:
                                    count2 += 1
                            N = D, "Exist:", count2, "position", count, "\n"
                            T.insert(tk.END, N)
                            root16.withdraw()
                    else:
                        root14 = tk.Tk()
                        tk.Label(root14, text="Repeated digits not allowed, please enter a valid key").pack()
                        tk.Button(root14, text="OK", command=root14.destroy).pack()
                elif len(D) not in [0, 4]:
                    A.delete(0, tk.END)
                    D = ""
                    root15 = tk.Tk()
                    tk.Label(root15, text="Key is incorrect, please enter a 4 digit code").pack()
                    tk.Button(root15, text="OK", command=root15.destroy).pack()
        root2 = tk.Tk()
        tk.Label(root2, text="Enter The Code:", font="Arial 30 bold", justify="center").pack()
        A = tk.Entry(root2, width=15, font="Arial 15")
        A.pack()
        tk.Button(root2, text="Submit", command=I).pack()
        root2.protocol("WM_DELETE_WINDOW", lambda: [root2.destroy()])
        root2.mainloop()

class big():

    def g():
        B = C.get()
        if B in [""]:
            root3 = tk.Tk()
            tk.Label(root3, text="oops! There is no key. Please put a key").pack()
            tk.Button(root3, text="OK", height=1, width=2, command=root3.destroy).pack()
        else:
            for i in range(len(B)):
                if B[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    root5 = tk.Tk()
                    tk.Label(root5, text="The entered key is not valid, please enter a valid key").pack()
                    tk.Button(root5, text="OK", height=1, width=2, command=root5.destroy).pack()
                    root5.mainloop()
                    break
                elif B[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    pass
            if len(B) == 4:
                l = []
                l2 = []
                l3 = []
                for i in range(len(B)):
                    if B.count(B[i]) > 1:
                        l.append(B[i])
                    else:
                        l2.append(B[i])
                    l3.append(B[i])
                if l == []:
                    root8 = tk.Tk()
                    tk.Label(root8, text="Key format is correct, pass the game to second player and press ok").pack()
                    tk.Button(root8, text="OK", command=lambda: [root8.destroy(), root.withdraw(), s.k()]).pack()
                    return B

                else:
                    root10 = tk.Tk()
                    tk.Label(root10, text="Repeated digits not allowed, please enter a valid key").pack()
                    tk.Button(root10, text="OK", command=root10.destroy).pack()
            elif len(B) not in [0, 4]:
                B = ""
                root9 = tk.Tk()
                tk.Label(root9, text="Key is incorrect, please enter a 4 digit code").pack()
                tk.Button(root9, text="OK", command=root9.destroy).pack()

    def h():
        if C.get() in [""]:
            root4 = tk.Tk()
            tk.Label(root4, text="oops! There is no key. Please put a valid key").pack()
            tk.Button(root4, text="OK", height=1, width=2, command=root4.destroy).pack()


root = tk.Tk()
tk.Label(root, text="What Is The Key?(Numbered, 4 digits, no repeated digits)", font="Arial 20 bold",
         justify="center").pack()
C = tk.Entry(root, width=15, font="Arial 15", )
C.pack()
B = C.get()
tk.Button(root, text="Submit", height=1, width=5, command=big.g).pack()
root.protocol("WM_DELETE_WINDOW", big.h)
root.mainloop()




