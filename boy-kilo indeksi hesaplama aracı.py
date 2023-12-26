import tkinter
window = tkinter.Tk()
window.title("ENDEKS HESAPLAYICI")
window.config(pady=30,padx=30)
def endeks_hesaplama():
   boy = boy_input.get()
   kilo = kilo_input.get()

   if kilo == "" or boy == "":
      endeks_sonucu.config(text="boy veya kilonuzu giriniz!")
   else:

           endeks = float(kilo) / (float(boy) / 100) ** 2
           tamsonuc_endeks = endeks_tamsonuc(endeks)
           endeks_sonucu.config(text=tamsonuc_endeks)


def endeks_tamsonuc(endeks):
    tamsonuc_endeks = f" endeksiniz: {endeks}.  "
    if endeks <= 16:
        tamsonuc_endeks *= "çok zayıfsın"
    elif 16 < endeks <= 17:
        tamsonuc_endeks += "zayıfsın"
    elif 17 < endeks <= 18.5:
        tamsonuc_endeks += "orta kilodasın"
    elif 18.5 < endeks <= 25:
        tamsonuc_endeks += "ortanın üstü kilodasın"
    elif 25 < endeks <= 30:
        tamsonuc_endeks += "şişmansın"
    elif 30 < endeks <= 35:
        tamsonuc_endeks += "obez 1"
    elif 35 < endeks <= 40:
        tamsonuc_endeks += "obez 2"
    return tamsonuc_endeks








kilo_input_label = tkinter.Label(text="kilonuzu girin (kg)")
kilo_input_label.pack()
kilo_input = tkinter.Entry(width=10)
kilo_input.pack()

boy_input_label = tkinter.Label(text="boyunuzu girin (cm)")
boy_input_label.pack()
boy_input = tkinter.Entry(width=10)
boy_input.pack()

hesaplama_butonu = tkinter.Button(text="hesapla", command=endeks_hesaplama)
hesaplama_butonu.pack()

endeks_sonucu = tkinter.Label()
endeks_sonucu.pack()

window.mainloop()