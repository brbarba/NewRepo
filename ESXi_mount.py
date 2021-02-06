ssh root@172.16.1.62 -p 22

ls -l /vmfs/devices/disks

vmkfstools -z /vmfs/devices/disks/t10.ATA_____ST3000DM0012D1CH166__________________________________W1F2KAWF
"/vmfs/volumes/snap-15b16fbc-Internal/SATA_bay/HGST_RDM_1.vmdk"

vmkfstools -z /vmfs/devices/disks/t10.ATA_____ST4000DM0042D2CV104__________________________________ZFN3KMZE "/vmfs/volumes/snap-15b16fbc-Internal/Disks/HGST_RDM_1.vmdk"



t10.ATA_____ST3000DM0082D2DM166__________________________________Z504EJ6X
vmkfstools -z /vmfs/devices/disks/t10.ATA_____ST3000DM0082D2DM166__________________________________Z504EJ6X "/vmfs/volumes/snap-15b16fbc-Internal/Disks/NAS3TB_RDM_1.vmdk"


# Add a new SCSI controller
# mount the new HDD to the VM
# change the HDD to SCSI controller 1 0:1
# change Disk Mode to virtual
# change to Independent - persistent
