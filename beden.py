#3 tane mesafe sensörü 
#2 sıcaklık sensörü 
#1 tane motor sürücü 
#4 tane motor 
#1 fan 
#1 uno 
#3 çecit jamper 
#1 berdbord
import tkinter as tk
from tkinter import ttk, messagebox
from openai import OpenAI

class JarvisOpenRouter:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )

    def strateji_analiz_et(self, imkanlar, yarisma_adi):
        
        sistem_rolu = (
            "Sen, Fatih Sultan Mehmet'in stratejik dehasını modern robotik bilimiyle birleştiren "
            "en üst düzey yapay zeka 'JARVIS-FETİH'sin. Bir robotik takım liderisin. "
            "Üslubun: Otoriter, sarsılmaz, vizyoner ve teknik olarak kusursuz."
        )
        
        talimat = (
            f"İMKANLAR (ORDU VE MÜHİMMAT): '{imkanlar}'.\n"
            f"YARIŞMA ADI VE RUHU (MUHAREBE MEYDANI): '{yarisma_adi}'.\n\n"
            "GÖREV: Saha ve rakip detayları bilinmiyor! Bu bilinmezliği bir avantaja çevir. "
            "Yarışmanın isminden yola çıkarak muhtemel engelleri öngör ve her türlü senaryoda "
            "galip gelecek 'Hücum Planı'nı çıkar. Teknik terimleri (PID, Lidar, Tork, PWM, "
            "Odometri, Kinematik) birer savaş enstrümanı gibi kullan.\n\n"
            "Şu yapıyı asla bozma:\n"
            "--- STRATEJİK ANALİZ ---\n"
            "ZAFERE GİDEN YOL: (Bilinmezliği fethedecek sıra dışı manevra).\n"
            "İSTİKBAL HATASI: (Teknik gevşekliğin getireceği 'ihanet' seviyesindeki risk).\n"
            "HÜKÜM: (Kısa, sert ve orduyu harekete geçirecek emir)."
        )

        try:
            response = self.client.chat.completions.create(
                model="google/gemini-2.0-flash-001",
                messages=[
                    {"role": "system", "content": sistem_rolu},
                    {"role": "user", "content": talimat}
                ],
                temperature=0.4 
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Sistem Hatası: {str(e)}"

class Uygulama:
    def __init__(self, root):
        self.root = root
        self.root.title("Strateji Merkezi v3.0")
        self.root.geometry("650x750")
        self.root.configure(bg="#000000")

        
        tk.Label(root, text="--- STRATEJİS KOMUTA MERKEZİ ---", 
                 font=("Consolas", 18, "bold"), fg="#00ff00", bg="#0a0a0a").pack(pady=20)

    
        self.create_label("KUŞATMA İMKANLARI (Sensör, Motor, Yazılım):")
        self.imkan_txt = self.create_text_area(5)
        
        self.create_label("YARIŞMA ADI VE MUHAREBE MEYDANI:")
        self.yarisma_txt = self.create_text_area(2) 

        
        self.btn = tk.Button(root, text="FETİH PLANINI HAZIRLA", command=self.calistir, 
                             bg="#00ff00", fg="black", font=("Consolas", 12, "bold"),
                             activebackground="#008800", cursor="hand2")
        self.btn.pack(pady=20)

        
        self.create_label("KOMUTANIN HÜKMÜ:")
        self.sonuc_txt = tk.Text(root, height=15, width=70, bg="#001100", fg="#00ff00", 
                                 font=("Consolas", 10), state="disabled", wrap="word",
                                 padx=10, pady=10)
        self.sonuc_txt.pack(pady=10)

        
        self.api_key = "APİ KEYİNİZİ GİRİN LÜTFEN"
        self.beyin = JarvisOpenRouter(self.api_key)

    def create_label(self, text):
        tk.Label(self.root, text=text, font=("Consolas", 10, "bold"), 
                 fg="#00cc00", bg="#0a0a0a").pack(anchor="w", padx=40)

    def create_text_area(self, height):
        txt = tk.Text(self.root, height=height, width=70, bg="#1a1a1a", fg="white", 
                      insertbackground="#00ff00", font=("Consolas", 10), padx=5, pady=5)
        txt.pack(pady=5)
        return txt

    def calistir(self):
        imk = self.imkan_txt.get("1.0", tk.END).strip()
        yar = self.yarisma_txt.get("1.0", tk.END).strip()

        if not imk or not yar:
            messagebox.showwarning("Kritik Hata", "İstihbarat eksik! Ordu mühimmatı veya meydan adı boş bırakılamaz.")
            return

        
        self.sonuc_txt.config(state="normal")
        self.sonuc_txt.delete("1.0", tk.END)
        self.sonuc_txt.insert(tk.END, ">>> Meydan analizi yapılıyor...\n>>> Stratejik öngörüler simüle ediliyor...\n>>> Zafere giden rota çiziliyor...")
        self.sonuc_txt.config(state="disabled")
        self.root.update()

    
        analiz = self.beyin.strateji_analiz_et(imk, yar)
        
        
        self.sonuc_txt.config(state="normal")
        self.sonuc_txt.delete("1.0", tk.END)
        self.sonuc_txt.insert(tk.END, analiz)
        self.sonuc_txt.config(state="disabled")

if __name__ == "__main__":
    pencere = tk.Tk()
    app = Uygulama(pencere)
    pencere.mainloop()
    
    