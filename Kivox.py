from forms.login import Login
import util.conexion as db

def main():
    db.createAdmin()
    Login()

if __name__ == '__main__':
    main()