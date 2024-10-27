# RUSSIAN ROULETTE (English)
The concept of the game is very simple: the program holds a number between 0 and 11, and you try to guess it. If you can't guess it, the system32 file, which is necessary for Windows to function, gets deleted. But don’t worry, when you open the application, it actually asks you if you really want to play or not.
## How Does It Work
```
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # If not an administrator, restart with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)
```
This part of the code is used to run the code as an administrator.



# RUSSIAN ROULETTE (Türkçe)
Oyunun olayı çok basit: Program 0 ile 11 arasında bir sayı tutuyor ve siz bu sayıyı tahmin etmeye çalışıyorsunuz. Eğer bilemezseniz, Windows'un çalışması için gerekli olan system32 dosyası siliniyor. Ama endişelenmeyin, uygulamayı açtığınızda gerçekten oynamak isteyip istemediğinizi soruyor.
