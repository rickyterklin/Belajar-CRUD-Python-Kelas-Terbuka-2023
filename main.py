import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_oprasi = os.name
    match sistem_oprasi:  # untuk mengclear teriminal
        case "posix": os.system("clear") # digunakan untuk linuk
        case "nt" : os.system("cls") # digunakan untuk windows

    print("Selamat Datang di Program")
    print("Database Perpustakaan")
    print("=====================")

    # Check Database itu ada atau tidak
    CRUD.init_console()

    while(True):
        match sistem_oprasi:  # untuk mengclear teriminal
            case "posix": os.system("clear") # digunakan untuk linuk
            case "nt" : os.system("cls") # digunakan untuk windows

        print("Selamat Datang di Program")
        print("Database Perpustakaan")
        print("=====================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan Opsi: ")


        match user_option:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()
        
        
        is_done = input("Apakah Sudah selesai ? (y/n)")
        if is_done == "y" or is_done =="Y":
            break

    print("Akhir dari program") 