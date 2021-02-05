def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    mensaje = generate_fortune()
    numeros = generate_lucky_numbers(how_many_lucky_numbers)
    print("\n",mensaje,"\n",numeros,"\nconcatenando")
    #full_mensaje = mensaje + numeros
    #print (full_mensaje)
    return numeros



    print("\n {} \n {} \nconcatenando".format(mensaje, numeros))


Bruno Barba (brbarba)
bruno.barba@gmail.com

1 root     root     2998986437632 Feb  3 23:10 t10.ATA_____ST3000DM0012D1CH166__________________________________W1F2KAWF:


vmkfstools -z /vmfs/devices/disks/t10.ATA_____ST3000DM0012D1CH166__________________________________W1F2KAWF
"/vmfs/volumes/snap-15b16fbc-Internal/SATA_bay/HGST_RDM_1.vmdk"

vmkfstools -z /vmfs/devices/disks/t10.ATA_____ST3000DM0012D1CH166__________________________________W1F2KAWF "/vmfs/volumes/snap-15b16fbc-Internal/Disks/HGST_RDM_1.vmdk"
